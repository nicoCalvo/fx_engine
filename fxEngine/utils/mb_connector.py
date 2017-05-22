import pika
import os


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
                    time.sleep(1)
                    tries += 1
                else:
                    break
        return self.__instance
