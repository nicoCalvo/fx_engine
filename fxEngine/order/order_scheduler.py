import json
from fxEngine.utils.mb_connector import MbConnector
import time

class Observer(object):

    def update(self):
        pass



class OrderScheduler(Observer):
    Q_orders = 'Q.fx_engine.filled_orders.st.'

    def __init__(self, order_manager,mb_connection=None):
        self.order_manager = order_manager
        self.mb_connection = mb_connection or MbConnector.get_connection()
        self.queue = self.Q_orders + order_manager._strategy.id

    def update(self):
        self._update_order_manager()


    def _get_orders(self):
        count = 0
        max_count = 10
        body = None
        channel = self.mb_connection.channel()
        while not body and count < max_count:
            try:
                method_frame, header_frame, body = channel.basic_get(
                    queue=self.queue_ingest, no_ack=True)
            except:
                channel = self.mb_connection.channel()
            if not body:
                time.sleep(1)
                count += 1

        if count == max_count and not body:
            channel = self.mb_connection.channel()
            channel.basic_publish(
                exchange='E_timeout_exceptions', routing_key='',body='FxEngine.OrderScheduler')
            raise RabbitConnectionError()

            raise RabbitConnectionError('Retrieving ingest: ' + self._id)
        return body

    def _update_order_manager(self):
        order_msg = json.loads(self._get_orders())
        filled_orders = order_msg['list_filled_orders']
        self.order_manager._update_open_orders(filled_orders)








