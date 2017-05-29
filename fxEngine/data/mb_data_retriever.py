from ..utils.mb_connector import MbConnector
from ..utils.exceptions import RabbitConnectionError
import time


class DataRetriever(object):
    """docstring for DataRtriever"""

    def __init__(self, _id):
        self._id = str(_id)
        self.conn = MbConnector.get_connection()
        self.queue_tick = 'Q_tick_strategy_' + str(_id)
        self.queue_ingest = 'Q_ingest_strategy_' + str(_id)
        

    def current_tick(self):
        body = None
        count = 0
        max_count = 20
        channel = self.conn.channel()
        while not body and count < max_count:
            try:
                method_frame, header_frame, body = channel.basic_get(queue=self.queue_tick, no_ack=True)
            except:
                channel = self.conn.channel()
                pass
            if not body:
                count += 1
                time.sleep(1)

        if count == max_count and not body:
            raise RabbitConnectionError('Retrieving tick: ' + self._id)
        channel.close()
        return body

    def ingest(self):
        return 
        count = 0
        max_count = 10

        body = None
        while not body and count < max_count:
            method_frame, header_frame, body = self.channel.basic_get(queue=self.queue_ingest, no_ack=True)
            time.sleep(1)
            count += 1
        if count == 30 and not body:
            raise RabbitConnectionError('Retrieving tick: ' + self._id)
        return body

        # return bcolz.ctable(columns=mock_arrays, names=DEMO_PAIRS,
#                             mode='w', expectedlen=LEN)

        



# class DemoLoader(object):
#     tick_counter = 0

#     def ingest(self):
#         LEN = 50
#         mock_arrays = self._get_mock_arrays(LEN)
#         return bcolz.ctable(columns=mock_arrays, names=DEMO_PAIRS,
#                             mode='w', expectedlen=LEN)

#     def _get_mock_arrays(self, _len):
#         base = datetime.datetime.today()
#         date_list = [base - datetime.timedelta(days=_len)
#                      for x in range(0, _len)]
#         eur_dol = np.random.rand(_len, 4)
#         dol_yua = np.random.rand(_len, 4)
#         ars_mex = np.random.rand(_len, 4)
#         bol_yen = np.random.rand(_len, 4)
#         uru_ars = np.random.rand(_len, 4)
#         cub_dol = np.random.rand(_len, 4)
#         dol_uru = np.random.rand(_len, 4)
#         yen_eur = np.random.rand(_len, 4)
#         return [date_list, eur_dol, dol_yua, ars_mex, bol_yen, uru_ars,
#                 cub_dol, dol_uru, yen_eur]

#     def (self):
#         self.tick_counter += 1
#         tick = []
#         if self.tick_counter > 10:
#             self.tick_counter = 0
#             date = datetime.datetime.now() + datetime.timedelta(days=1)
#             tick.append(date)
#         else:
#             tick.append(datetime.datetime.today())
#         for pair in DEMO_PAIRS[1:]:
#             tick.append(self._set_random_tick_values())
#         return tick

#     def _set_random_tick_values(self):
#         tick = TICK_EXAMPLE
#         bid = random.uniform(5.5, 8.9)
#         ask = random.uniform(bid - 2, bid)
#         tick['tick']['Quote']['Bid'] = bid
#         tick['tick']['Quote']['Mid'] = (bid + ask) / 2
#         tick['tick']['Quote']['Ask'] = ask
#         tick['tick']['Quote']['Amount'] = random.randint(10000, 800000)
#         # tick['datetime'] = datetime.datetime.today()
#         return tick
