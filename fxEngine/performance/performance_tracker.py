from ..data.dto import Portfolio, Position, Order
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
        self._retrieve_new_portfolio()

    def _retrieve_new_portfolio(self):
        '''
        AS OF NOW, IT RETURN A MockedPortfolio
        '''

        return Portfolio(9999, 100000, 3456, 0.0, 123, 33345, [Position(
        2, 34, 54, 56, 78), Position(2, 34, 54, 56, 78)], '2012-03-04',
        42423)
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

        # body = '{"portfolio_value":100000,"cash":8000, "returns": 32342, "positions_value":12334534, "positions":[{"pair":"EURUSD", "amount":12000},{"pair":"USDCAD", "amount":3500}]}'
  #       body = ''' {
  #   "date": "2013-06-07",
  #   "portfolio_value": "7700",
  #   "portfolio_return": "123",
  #   "portfolio_returns_std": "535",
  #   "portfolio_beta": "45645",
  #   "portfolio_returns_std": "34534",
  #   "portfolio_std": "45645",
  #   "portfolio_sharpe": "4322",
  #   "portfolio_cumulative_returns": "1111",
  #   "portfolio_max_drawdown": "567567",
  #   "portfolio_sharpe": "87867876",
  #   "positions":[
  #     {
  #       "position_id": "dasd12",
  #       "date_updated": "2013-06-07",
  #       "symbol":"USDCAD",
  #       "amount": "2300",
  #       "value": "2342323"
  #     }
  #   ],
  #   "open_orders":[
  #   ]
  # }'''
        portfolio = json.loads(body)
        positions_list = []
        for position in portfolio['positions']:
            positions_list.append(Position(**position))

        new_portfolio = Portfolio(value=portfolio['portfolio_value'],
                                  returns=portfolio['portfolio_return'],
                                  return_std=portfolio[
                                      'portfolio_returns_std'],
                                  beta=portfolio['portfolio_beta'], std=portfolio[
            'portfolio_std'],
            sharpe=portfolio['portfolio_sharpe'],
            cumulative_returns=portfolio[
            'portfolio_cumulative_returns'],
            max_drawdown=portfolio[
                                      'portfolio_max_drawdown'],
            positions=positions_list)

        self.strategy.context.portfolio = new_portfolio
        open_orders = []
        for order in portfolio['open_orders']:
            open_orders.append(Order(id=order['order_id'], date=order[
                               'date'], symbol=order['symbol'], amount=order['amount']))

        self.strategy.context._open_orders = open_orders
        # self.portfolio = json.loads(body)
