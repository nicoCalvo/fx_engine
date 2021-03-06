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

    @abc.abstractmethod
    def _error(self, msg):
        pass


class LocalLogger(Logger):
    FILENAME = 'demo_log.log'

    def __init__(self):
        self.file = open(self.FILENAME, 'w')

    def info(self, msg):
        self.file.write('INFO: ' + msg + '\n')

    def _error(self, msg):
        self.file.write('ERROR: ' + msg + '\n')

    def __del__(self):
        self.file.close()


class AtakamaLogger(Logger):
    E_ST_LOG = 'E_standard_log'
    E_ST_ERROR_LOG = 'E_error_log'
    MAX_LENGTH_LOG = 500
    WARNING_SHRINK_MESSAGE = 'MESSAGE SIZE > 500. MESSAGE SHRINKED'

    def __init__(self, _id):
        self.conn = MbConnector.get_connection()
        self.strategy_id = _id
        self._counter = 0

    def info(self, msg):
        self._counter += 1
        msg = str(msg)
        channel = self.conn.channel()
        date = self.clock.new_date.strftime('%Y-%m-%d %H:%M:%S')if isinstance(self.clock.new_date, datetime) else '1901-01-01' #.strftime('%Y-%m-%d %H:%M:%S')
        
        if len(msg) > self.MAX_LENGTH_LOG:
            msg = msg[:self.MAX_LENGTH_LOG]
            try:
                msg = dict(simulation_date=date,
                           message=self.WARNING_SHRINK_MESSAGE + msg,
                           counter=self._counter,
                           strategy_id=str(self.strategy_id))
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

    def _error(self, msg):
        self._counter += 1
        msg = str(msg)
        channel = self.conn.channel()
        date = self.clock.new_date.strftime('%Y-%m-%d %H:%M:%S')if isinstance(self.clock.new_date, datetime) else '1901-01-01' #.strftime('%Y-%m-%d %H:%M:%S')
        
        if len(msg) > self.MAX_LENGTH_LOG:
            msg = msg[:self.MAX_LENGTH_LOG]
            try:
                msg = dict(simulation_date=date, message=self.WARNING_SHRINK_MESSAGE, counter=self._counter)
                channel.basic_publish(exchange=self.E_ST_LOG,
                                      routing_key=str(self.strategy_id),
                                      body=json.dumps(msg))
            except Exception, e:
                print '\n\n\n\n'
                print 'SE ROMPIOOOO  '+ str(e)

        msg = dict(simulation_date=date, message=str(msg))
        try:
            channel.basic_publish(exchange=self.E_ST_ERROR_LOG,
                                       routing_key=str(self.strategy_id),
                                       body=json.dumps(msg))
        except Exception, e:
            print '\n\n\n\n'
            print 'SE ROMPIOOOO  '+ str(e)