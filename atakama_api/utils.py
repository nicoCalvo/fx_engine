import six
import abc


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
    FILENAME = 'demo_log.log'

    def __init__(self):
        self.file = open(self.FILENAME, 'w')

    def info(self, msg):
        self.file.write('INFO: ' + msg + '\n')

    def __del__(self):
        self.file.close()
