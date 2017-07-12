import six
import abc
import pika
import os
import time
import json
from datetime import datetime
from fxEngine.utils.mb_connector import MbConnector

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


class AtakamaLogger(Logger):
    E_ST_LOG = 'E_standard_log'
    MAX_LENGTH_LOG = 500
    WARNING_SHRINK_MESSAGE = 'MESSAGE SIZE > 500. MESSAGE SHRINKED'

    def __init__(self, _id):
        self.conn = MbConnector.get_connection()
        self.strategy_id = _id

    def info(self, msg):
        msg str(msg)
        channel = self.conn.channel()
        date = self.clock.new_date.strftime('%Y-%m-%d %H:%M:%S')if isinstance(self.clock.new_date, datetime) else '1901-01-01' #.strftime('%Y-%m-%d %H:%M:%S')
        
        if len(msg) > self.MAX_LENGTH_LOG:
            msg = msg[:self.MAX_LENGTH_LOG]
            try:
                msg = dict(simulation_date=date, message=self.WARNING_SHRINK_MESSAGE)
                channel.basic_publish(exchange=self.E_ST_LOG,
                                      routing_key=str(self.strategy_id),
                                      body=json.dumps(msg))
            except Exception, e:
                print '\n\n\n\n'
                print 'SE ROMPIOOOO  '+ str(e)

        msg = dict(simulation_date=date, message=str(msg))
        try:
            channel.basic_publish(exchange=self.E_ST_LOG,
                                       routing_key=str(self.strategy_id),
                                       body=json.dumps(msg))
        except Exception, e:
            print '\n\n\n\n'
            print 'SE ROMPIOOOO  '+ str(e)
