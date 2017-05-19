import six
import abc
import pika
import os


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
    STRATEGY_ID = ''

    def __init__(self):
        self.channel = MbConnector.get_connection().channel()

    def info(self, msg):
        self.channel.basic_publish(exchange=self.E_ST_LOG,
                                   routing_key=self.STRATEGY_ID,
                                   body=msg)

    def __del__(self):
        self.channel.close()


class MbConnector(object):
    __instance = ''
    host = os.environ.get('RABBIT_HOST', 'localhost')
    port = os.environ.get('RABBIT_PORT', 5672)

    @classmethod
    def get_connection(self):
        if not self.__instance:
            self.__instance = pika.BlockingConnection(
                pika.ConnectionParameters(host=self.host, port=self.port))
        return self.__instance
