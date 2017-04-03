from fxEngine.strategy.exceptions import StrategyRegistrationError
from fxEngine.utils.mb_connector import MbConnector
import json


class StrategyRegistration(object):
    """Responsibility: Register itself into message broker
            and create the queues needed for the execution of the
            strategy"""

    def __init__(self, dto_strategy):
        try:
            self.conn = MbConnector.get_connection()
        except Exception, e:
            raise StrategyRegistrationError(str(e))
        self.strategy = dto_strategy

    def publish_strategy(self):
        channel = self.conn.channel()
        message = json.dumps(self.strategy.to_json())
        channel.basic_publish(exchange='E_register_strategy',
                              routing_key='',
                              body=message)
        channel.close()
