import pika
import os
import time

class MbConnector(object):
    host = os.environ.get('RABBIT_HOST', 'localhost')
    port = int(os.environ.get('RABBIT_PORT', 5672))
    virtual_host = os.environ.get('RABBIT_VHOST', "/")
    credentials = pika.PlainCredentials(
        username=os.environ.get('RABBIT_USERNAME', 'tonyg'),
        password=os.environ.get('RABBIT_PASSWORD', 'changeit'))

    @classmethod
    def get_connection(self):
        max_tries = 5
        tries = 0
        while tries < max_tries:
            try:
                _instance = pika.BlockingConnection(
                    pika.ConnectionParameters(host=self.host, port=int(self.port),
                                              credentials=self.credentials,
                                              virtual_host=self.virtual_host,
                                              socket_timeout=3000))
            except Exception, e:
                time.sleep(1)
                tries += 1
            else:
                break
        return _instance
