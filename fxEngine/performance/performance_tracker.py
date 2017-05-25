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
        not_message = True
        max_count = 10
        counter = 0
        while not_message and counter < max_count:
            (method, properties, body) = self.channel.basic_get(
                queue=self.queue, no_ack=True)
            if body:
                not_message = False
            else:
                counter += 1
                time.sleep(1)
        if not body and counter == max_count:
            self.channel.basic_publish(
                exchange=self.exchange, routing_key='', body=self.excep_msg)
            raise RabbitConnectionError()
            '''
            publish alert!

            '''
        self.portfolio = json.loads(body)


