from ..utils.mb_connector import MbConnector
from ..utils.exceptions import RabbitConnectionError
import time
import json
import logging

LOGGER = logging.getLogger(__name__)


class DataRetriever(object):
    """docstring for DataRtriever"""

    def __init__(self, _id):
        self._id = str(_id)
        self.conn = MbConnector.get_connection()
        self.queue_tick = 'Q_portfolio_strategy_' + str(_id)
        self.queue_ingest = 'Q_ingest2_strategy_' + str(_id)

    def current_tick(self):
        LOGGER.info('CONSUMING TICK')
        body = None
        count = 0
        max_count = 20
        channel = self.conn.channel()
        while not body and count < max_count:
            try:
                method_frame, header_frame, body = channel.basic_get(
                    queue=self.queue_tick, no_ack=True)
            except:
                channel = self.conn.channel()
                pass
            if not body:
                count += 1
                time.sleep(1)
        if count == max_count and not body:
            LOGGER.info('TICKER NOT FOUND')
            raise RabbitConnectionError('Retrieving tick: ' + self._id)
        channel.close()
        LOGGER.info('TICKER OK')
        LOGGER.info(body)
        if not isinstance(body, dict):
            body = json.loads(body)
        return body

    def ingest(self):
        return json.loads(self.get_bundle())

    def get_bundle(self):
        LOGGER.info('CONSUMING INGEST')
        count = 0
        max_count = 20
        body = None
        channel = self.conn.channel()
        print 'INGESTING'
        while not body and count < max_count:
            try:
                method_frame, header_frame, body = channel.basic_get(
                    queue=self.queue_ingest, no_ack=True)
            except:
                channel = self.conn.channel()
            if not body:
                time.sleep(2)
                count += 1

        if count == max_count and not body:
            LOGGER.info('DIDNT GET ANY MESSAGE!')
            channel = self.conn.channel()
            channel.basic_publish(
                exchange='E_timeout_exceptions', routing_key='',
                body='UNABLE TO PERFORM INGEST ' + self.queue_ingest)
            raise RabbitConnectionError()

            raise RabbitConnectionError('Retrieving ingest: ' + self._id)
        LOGGER.info('INGEST OK')
        return body
