from fxEngine.strategy.exceptions import StrategyRegistrationError
from fxEngine.utils.mb_connector import MbConnector
import json


class StrategyRegistration(object):
    """Responsibility: Register itself into message broker
            and create the queues needed for the execution of the
            strategy"""

    def __init__(self, msg):
        try:
            self.conn = MbConnector.get_connection()
        except Exception, e:
            raise StrategyRegistrationError(str(e))
        self.msg = msg

    def _parse_msg(self):
        cod = self.msg.pop('code')
        cod.pop('script')
        self.msg = json.dumps(cod)

    def publish_strategy(self):
        self._parse_msg()
        channel = self.conn.channel()
        channel.basic_publish(exchange='E_register_strategy',
                              routing_key='',
                              body=self.msg)
        channel.close()
