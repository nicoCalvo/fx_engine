import pika
import os


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


con = MbConnector.get_connection()
print id(con)
con2 = MbConnector.get_connection()
print id(con2)
assert id(con) == id(con2)
