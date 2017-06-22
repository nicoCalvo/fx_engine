from ..utils.mb_connector import MbConnector
from ..utils.exceptions import RabbitConnectionError
import json


class OrderRouter(object):

    def __init__(self, strategy_id):
        self.conn = MbConnector.get_connection()

        self.st_id = strategy_id
        self.exchange = 'E_orders_strategy'

    def publish_orders(self, orders):
        channel = self.conn.channel()
        try:
            channel.basic_publish(exchange=self.exchange,routing_key=self.st_id,
                 body=orders)
        except Exception, e:
            channel.basic_publish(
                exchange='E_timeout_exceptions', routing_key='',
                body='STRATEGY: ' + self.st_id + ' - ' + str(e))
            raise RabbitConnectionError()
        channel.close()
