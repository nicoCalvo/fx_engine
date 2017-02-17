from fxEngine.data.data_api import DataAPI
from fxEngine.data.data_portal import DataPortal
from fxEngine.tests.data_demo_loader import DemoLoader, PAIRS, DEMO_PAIRS
import unittest


class TestDataAPI(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_ingest(self):
        dp = DataPortal(ingester=DemoLoader(), pairs=PAIRS)
        dp.ingest()
        pairs_names = [x.name for x in PAIRS]
        data_api = DataAPI(data_portal=dp, traded_pairs=pairs_names)
        data_api.current(pairs=pairs_names[0], values='ask')
        #data_api.test('ASD')

    # def test_valid_ingest(self):
    #     dp = DataPortal(ingester=DemoLoader(), pairs=PAIRS)
    #     dp.ingest()
    #     pairs_names = [x.name for x in PAIRS]
    #     data_api = DataAPI(data_portal=dp, traded_pairs=pairs_names)
    #     data_api.current(pairs=pairs_names[0], values=['bid','ask'])
    #     #data_api.test('ASD')

    #  def test_valid_ingest(self):
    #     dp = DataPortal(ingester=DemoLoader(), pairs=PAIRS)
    #     dp.ingest()
    #     pairs_names = [x.name for x in PAIRS]
    #     data_api = DataAPI(data_portal=dp, traded_pairs=pairs_names)
    #     data_api.current(pairs=pairs_names[0], values=['bid','ask'])
    #     #data_api.test('ASD')

    #  def test_valid_ingest(self):
    #     dp = DataPortal(ingester=DemoLoader(), pairs=PAIRS)
    #     dp.ingest()
    #     pairs_names = [x.name for x in PAIRS]
    #     data_api = DataAPI(data_portal=dp, traded_pairs=pairs_names)
    #     data_api.current(pairs=pairs_names[0], values=['bid','ask'])
    #     #data_api.test('ASD')
