from ..data.dto import Portfolio, Position
from ..utils.exceptions import RabbitConnectionError
from ..utils.mb_connector import MbConnector
import time
import json


class Observer(object):

    def update(self):
        pass


class PerformanceTracker(Observer):

    def __init__(self, strategy):
        self.strategy = strategy
        self.queue = 'Q_perfmon_strategy_' + self.strategy.dto_strategy.id
        self.conn = MbConnector.get_connection()
        self.channel = self.conn.channel()
        self.excep_msg = 'Unable to retrieve portfolio'
        self.exchange = 'E_timeout_exceptions'

    def update(self):
        '''
        RETRIEVE UPDATED PORTFOLIO
        AND SET IT TO STRATEGY
        '''
        self.strategy.context.portfolio = self._retrieve_new_portfolio()

    def _retrieve_new_portfolio(self):
        '''
        AS OF NOW, IT RETURN A MockedPortfolio
        '''

        # return Portfolio(9999, 100000, 3456, 0.0, 123, 33345, [Position(
        # 2, 34, 54, 56, 78), Position(2, 34, 54, 56, 78)], '2012-03-04',
        # 42423)
        channel = self.conn.channel()
        not_message = True
        max_count = 20
        counter = 0
        while not_message and counter < max_count:
            try:
                (method, properties, body) = channel.basic_get(
                    queue=self.queue, no_ack=True)
                if body:
                    not_message = False
                else:
                    counter += 1
                    time.sleep(1)
            except:
                channel = self.conn.channel()
                counter += 1
                time.sleep(1)
                pass

        if not body and counter == max_count:
            self.channel.basic_publish(
                exchange=self.exchange, routing_key='', body=self.excep_msg)
            raise RabbitConnectionError()

        # body = '{"portfolio_value":100000,"cash":8000, "returns": 32342, "positions_value":12334534, "open_positions":[{"pair":"EURUSD", "amount":12000},{"pair":"JPYEUR", "amount":3500}]}'

        portfolio = json.loads(body)
        positions_list = []
        for position in portfolio['positions']:
            positions_list.append(Position(**position))

        return Portfolio(value=portfolio['portfolio_value'],
                         returns=portfolio['portfolio_return'],
                         return_std=portfolio['portfolio_returns_std'],
                         beta=portfolio['portfolio_beta'], std=portfolio[
                             'portfolio_std'],
                         sharpe=portfolio['portfolio_sharpe'],
                         cumulative_returns=portfolio[
                             'portfolio_cumulative_returns'],
                         max_drawdown=portfolio['portfolio_max_drawdown'],
                         positions=positions_list)
        # self.portfolio = json.loads(body)
