import datetime
import numpy as np
import bcolz
from fxEngine.data.pair import Pair
import random

DEMO_PAIRS = ['DATE', 'EURUSD', 'USDYUA', 'ARSMEX', 'BOLYEN',
              'USUARS', 'CUBUSD', 'USDURU', 'YENEUR']

PAIR_NAMES = DEMO_PAIRS[1:]
PAIRS = [Pair(x) for x in DEMO_PAIRS[1:]]

TICK_EXAMPLE = {u'tick': {u'AssetType': u'FxSpot', u'Uic': 16, u'LastUpdated':
                          u'2017-02-12T09:32:09.967000Z', u'Quote': {u'Bid': 7.43505, u'Mid': 7.435365, u'ErrorCode':
                                                                     u'None', u'Amount': 100000, u'DelayedByMinutes': 0, u'Ask': 7.43568, u'RFQState': u'None',
                                                                     u'PriceTypeAsk': u'Indicative', u'PriceTypeBid': u'Indicative'}},
                u'ohba': []
                # u'timestamp': datetime.datetime.today()
                }


class DemoLoader(object):

    def ingest(self):
        LEN = 50
        mock_arrays = self._get_mock_arrays(LEN)
        return bcolz.ctable(columns=mock_arrays, names=DEMO_PAIRS,
                            mode='w', expectedlen=LEN)

    def _get_mock_arrays(self, _len):
        base = datetime.datetime.today()
        date_list = [base - datetime.timedelta(days=_len)
                     for x in range(0, _len)]
        eur_dol = np.random.rand(_len, 4)
        dol_yua = np.random.rand(_len, 4)
        ars_mex = np.random.rand(_len, 4)
        bol_yen = np.random.rand(_len, 4)
        uru_ars = np.random.rand(_len, 4)
        cub_dol = np.random.rand(_len, 4)
        dol_uru = np.random.rand(_len, 4)
        yen_eur = np.random.rand(_len, 4)
        return [date_list, eur_dol, dol_yua, ars_mex, bol_yen, uru_ars,
                cub_dol, dol_uru, yen_eur]

    def current_tick(self):
        tick = []
        tick.append(datetime.datetime.today())
        for pair in DEMO_PAIRS[1:]:
            tick.append(self._set_random_tick_values())
        return tick

    def _set_random_tick_values(self):
        tick = TICK_EXAMPLE
        bid = random.uniform(5.5, 8.9)
        ask = random.uniform(bid - 2, bid)
        tick['tick']['Quote']['Bid'] = bid
        tick['tick']['Quote']['Mid'] = (bid + ask) / 2
        tick['tick']['Quote']['Ask'] = ask
        tick['tick']['Quote']['Amount'] = random.randint(10000, 800000)
        # tick['datetime'] = datetime.datetime.today()
        return tick
