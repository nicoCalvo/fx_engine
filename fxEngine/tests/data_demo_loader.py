import datetime
import numpy as np
import bcolz

DEMO_PAIRS = ['DATE','EURUSD', 'USDYUA', 'ARSMEX', 'BOLYEN',
              'USUARS', 'CUBUSD', 'USDURU', 'YENEUR']

class DemoLoader(object):

    def ingest(self):
        LEN = 50
        base = datetime.datetime.today()
        date_list = [base - datetime.timedelta(days=LEN)
                     for x in range(0, LEN)]
        eur_dol = np.random.rand(LEN, 4)  # np.empty([LEN, 4])
        dol_yua = np.random.rand(LEN, 4)
        ars_mex = np.random.rand(LEN, 4)
        bol_yen = np.random.rand(LEN, 4)
        uru_ars = np.random.rand(LEN, 4)
        cub_dol = np.random.rand(LEN, 4)
        dol_uru = np.random.rand(LEN, 4)
        yen_eur = np.random.rand(LEN, 4)
        return bcolz.ctable(columns=[date_list, eur_dol, dol_yua, ars_mex, bol_yen, uru_ars,
                                     cub_dol, dol_uru, yen_eur], names=DEMO_PAIRS, mode='w', expectedlen=LEN)
