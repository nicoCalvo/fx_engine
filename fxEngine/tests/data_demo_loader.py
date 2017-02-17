import datetime
import numpy as np
import bcolz
from fxEngine.data.pair import Pair


DEMO_PAIRS = ['DATE', 'EURUSD', 'USDYUA', 'ARSMEX', 'BOLYEN',
              'USUARS', 'CUBUSD', 'USDURU', 'YENEUR']

PAIRS = [Pair(x) for x in DEMO_PAIRS]


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
            tick.append(np.random.rand(1, 4))
        return tick
