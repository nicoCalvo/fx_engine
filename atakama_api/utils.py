import six
import abc
import pika
import os
import time
import json
from datetime import datetime


@six.add_metaclass(abc.ABCMeta)
class Logger(object):

    @abc.abstractmethod
    def info(self, msg):
        pass


class LocalLogger(Logger):
    FILENAME = 'demo_log.log'

    def __init__(self):
        self.file = open(self.FILENAME, 'w')

    def info(self, msg):
        self.file.write('INFO: ' + msg + '\n')

    def __del__(self):
        self.file.close()


class RealLogger(Logger):
    E_ST_LOG = 'E_standard_log'

    def __init__(self, _id):
        self.channel = MbConnector.get_connection().channel()
        self.strategy_id = _id

    def info(self, msg):
        # time.sleep(2)
        date = self.clock.new_date.strftime('%Y-%m-%d %H:%M:%S')if isinstance(self.clock.new_date, datetime) else '1901-01-01' #.strftime('%Y-%m-%d %H:%M:%S')
        msg = dict(simulation_date=date, message=msg)
        self.channel.basic_publish(exchange=self.E_ST_LOG,
                                   routing_key=str(self.strategy_id),
                                   body=json.dumps(msg))

    def __del__(self):
        self.channel.close()


class MbConnector(object):
    __instance = ''
    host = os.environ.get('RABBIT_HOST', 'localhost')
    port = os.environ.get('RABBIT_PORT', 5672)
    virtual_host = os.environ.get('RABBIT_VHOST', "/")
    credentials = pika.PlainCredentials(
        username=os.environ.get('RABBIT_USERNAME', 'tonyg'),
        password=os.environ.get('RABBIT_PASSWORD', 'changeit'))

    @classmethod
    def get_connection(self):
        if not self.__instance:
            max_tries = 5
            tries = 0
            while tries < max_tries:
                try:
                    self.__instance = pika.BlockingConnection(
                        pika.ConnectionParameters(host=self.host, port=int(self.port),
                                                  credentials=self.credentials,
                                                  virtual_host=self.virtual_host,
                                                  socket_timeout=3000))
                except Exception, e:
                    # logging.info('Unable to connect to Rabbit- ' + str(e))
                    time.sleep(1)
                    tries += 1
                else:
                    break
        return self.__instance