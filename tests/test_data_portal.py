from data.data_portal import DataPortal
import unittest
import numpy as np
import bcolz


LEN = 50000


DEMO_PAIRS = ['eur_dol', 'dol_yua', 'ars_mex', 'bol_yen',
              'uru_ars', 'cub_dol', 'dol_uru', 'yen_eur']


class TestDataPortal(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_ingest(self):
        dp = DataPortal(ingester=DemoLoader(), pairs_names_list=DEMO_PAIRS)
        dp.ingest()


class DemoLoader(object):

    def ingest(self):
        eur_dol = np.random.rand(LEN, 4)  # np.empty([LEN, 4])
        dol_yua = np.random.rand(LEN, 4)
        ars_mex = np.random.rand(LEN, 4)
        bol_yen = np.random.rand(LEN, 4)
        uru_ars = np.random.rand(LEN, 4)
        cub_dol = np.random.rand(LEN, 4)
        dol_uru = np.random.rand(LEN, 4)
        yen_eur = np.random.rand(LEN, 4)
        # self.load_data((eur_dol, dol_yua, ars_mex,
        #                        bol_yen, uru_ars, cub_dol, dol_uru, yen_eur))
        return bcolz.ctable(columns=[eur_dol, dol_yua, ars_mex, bol_yen, uru_ars,
                                     cub_dol, dol_uru, yen_eur], names=DEMO_PAIRS, mode='w', expectedlen=LEN)
