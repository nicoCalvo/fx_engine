from fxEngine.data.data_api import DataAPI
from fxEngine.data.data_portal import DataPortal
# from fxEngine.tests.data_demo_loader import DemoLoader, PAIRS
from fxEngine.tests.mocks.data_retriever import MockDataRetriever
from fxEngine.data.ticker_filter import TickerFilter
import unittest
import pandas as pd




class TestDataAPI(unittest.TestCase):
    PAIRS = ['USDEUR', 'EURDKK']
    def setUp(self):
        pass

    # def test_single_value_ask(self):
    #     dp = DataPortal(ingester=MockDataRetriever('test'), pairs=self.PAIRS)
    #     dp.ingest()
    #     data_api = DataAPI(data_portal=dp, traded_pairs=self.PAIRS)
    #     value = data_api.current(pairs=pairs_names[0], values='ask')
    #     self.assertIsInstance(value, float)

    # def test_single_value_amount(self):
    #     dp = DataPortal(ingester=MockDataRetriever('test'), pairs=self.PAIRS)
    #     dp.ingest()
    #     pairs_names = [x.name for x in PAIRS]
    #     data_api = DataAPI(data_portal=dp, traded_pairs=self.PAIRS)
    #     value = data_api.current(pairs=self.PAIRS[0], values='amount')
    #     self.assertIsInstance(value, int)

    # def test_single_pair_many_values(self):

    #     dp = DataPortal(ingester=MockDataRetriever('test'), pairs=self.PAIRS)
    #     dp.ingest()
    #     data_api = DataAPI(data_portal=dp, traded_pairs=self.PAIRS)
    #     req_values = ['ask', 'bid']
    #     value = data_api.current(pairs=self.PAIRS[0], values=req_values)
    #     self.assertIsInstance(value, pd.Series)
    #     self.assertEquals(set(value.index), set(req_values))

    # def test_many_pair_single_value(self):
    #     dp = DataPortal(ingester=MockDataRetriever('test'), pairs=self.PAIRS)
    #     dp.ingest()
    #     data_api = DataAPI(data_portal=dp, traded_pairs=self.PAIRS)
    #     value = data_api.current(pairs=pairs_names[0:3], values='ask')
    #     self.assertIsInstance(value, pd.Series)
    #     # self.assertEquals(set(value.index), set(pairs_names[0:3]))

    # def test_many_pair_many_values(self):
    #     dp = DataPortal(ingester=MockDataRetriever('test'), pairs=PAIRS)
    #     dp.ingest()
    #     pairs_names = [x.name for x in PAIRS]
    #     data_api = DataAPI(data_portal=dp, traded_pairs=pairs_names)
    #     req_values = ['ask', 'bid', 'mid', 'amount']
    #     filtered_pairs = pairs_names[0:4]
    #     value = data_api.current(pairs=filtered_pairs, values=req_values)
    #     _filter = TickerFilter( pairs_names)
    #     ticker = _filter.filter(dp.current_tick[1:], filtered_pairs, req_values)
    #     data_api_ask = value.loc['EURUSD']['ask']
    #     ticker_ask = ticker[0][0] # El ticker se maneja por posiciones 
    #     pair_pos = pairs_names.index('EURUSD')
        
    #     self.assertIsInstance(value, pd.DataFrame)
    #     self.assertEquals(set(value.index), set(filtered_pairs))

    # def test_nopairs_novalues(self):
    #     dp = DataPortal(ingester=MockDataRetriever('test'), pairs=PAIRS)
    #     dp.ingest()
    #     pairs_names = [x.name for x in PAIRS]
    #     data_api = DataAPI(data_portal=dp, traded_pairs=pairs_names)
    #     value = data_api.current()
    #     self.assertIsInstance(value, pd.DataFrame)
    #     self.assertEquals(len(value.index), len(pairs_names))
    #     self.assertEquals(set(value.columns), set(['Bid', 'Ask', 'Mid', 'Amount']))

    def test_history_single_pair(self):
        pairs = MockDataRetriever.PAIRS
        dp = DataPortal(ingester=MockDataRetriever('test'), pairs=pairs)
        dp.ingest()
        data_api = DataAPI(data_portal=dp, traded_pairs=pairs)
        value = data_api.history(pairs=pairs[0], ticks=2)
        self.assertTrue(pairs[0] in value)
        self.assertEquals(len(value), 1)
        self.assertEquals(len(value[pairs[0]]), 2)


    def test_history_many_pairs(self):
        pass
