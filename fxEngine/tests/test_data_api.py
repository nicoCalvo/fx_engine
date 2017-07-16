from fxEngine.data.data_api import DataAPI
from fxEngine.data.data_portal import DataPortal
from fxEngine.tests.mocks.data_retriever import MockDataRetriever
from fxEngine.data.ticker_filter import TickerFilter
import unittest
import pandas as pd
import mock


class MockDataPortal(mock.Mock):

    current_tick = [{"ask": 7.44185, "bid": 7.44135, "medium": 7.4416,
                     "symbol": "EURDKK", "time": "2010/01/04 00:00:00"}, 
                    {"ask": 1.44146, "bid": 1.44126, "medium": 1.44136,
                     "symbol": "USDEUR", "time": "2010/01/04 00:00:00"}]

    def has_new_tick(self):
        return True

    def get_current_tick(self):
        current_date = datetime.strptime(self.current_tick[0]['time'],
                                         '%Y/%m/%d %H:%M:%S')
        current_date = current_date + timedelta(days=1)
        self.current_tick[0]['time'] = datetime.strftime(current_date,
                                                    '%Y/%m/%d %H:%M:%S')
        return self.tick

    def get_tick_date(self):
        return datetime.strptime(self.current_tick[0]['time'],
                                 '%Y/%m/%d %H:%M:%S')


class TestDataAPI(unittest.TestCase):
    PAIRS = ['USDEUR', 'EURDKK']
    def setUp(self):
        pass

    def test_single_value_ask(self):
        data_api = DataAPI(data_portal=MockDataPortal(), traded_pairs=self.PAIRS)
        value = data_api.current(pairs=self.PAIRS[0], values='ask')
        self.assertIsInstance(value, float)
        self.assertEquals(MockDataPortal.current_tick[1]['ask'], value)


    def test_single_value_bid(self):
        data_api = DataAPI(data_portal=MockDataPortal(), traded_pairs=self.PAIRS)
        value = data_api.current(pairs=self.PAIRS[1], values='bid')
        self.assertIsInstance(value, float)
        self.assertEquals(MockDataPortal.current_tick[0]['bid'], value)


    def test_single_pair_many_values(self):

        data_api = DataAPI(data_portal=MockDataPortal(), traded_pairs=self.PAIRS)
        req_values = ['ask', 'bid']
        value = data_api.current(pairs=self.PAIRS[0], values=req_values)
        self.assertIsInstance(value, pd.Series)
        self.assertEquals(value.index.values.tolist(), ['ask', 'bid'])


    def test_many_pair_single_value(self):
        data_api = DataAPI(data_portal=MockDataPortal(), traded_pairs=self.PAIRS)
        value = data_api.current(pairs=self.PAIRS, values='ask')
        self.assertIsInstance(value, pd.Series)
        self.assertEquals(value.index.values.tolist(), self.PAIRS)

    def test_many_pair_many_values(self):
        data_api = DataAPI(data_portal=MockDataPortal(), traded_pairs=self.PAIRS)
        req_values = ['ask', 'bid', 'medium']
        value = data_api.current(pairs=self.PAIRS, values=req_values)
        self.assertIsInstance(value, pd.DataFrame)
        self.assertEquals(value.columns.values.tolist(), req_values)
        self.assertEquals(value.index.values.tolist(), ['USDEUR','EURDKK'])
        

    def test_nopairs_novalues(self):
        data_api = DataAPI(data_portal=MockDataPortal(), traded_pairs=self.PAIRS)
        value = data_api.current()
        self.assertIsInstance(value, pd.DataFrame)
        self.assertEquals(value.columns.values.tolist(), ['bid', 'ask', 'medium'])
        self.assertEquals(value.index.values.tolist(), ['USDEUR','EURDKK'])


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
        pairs = MockDataRetriever.PAIRS
        dp = DataPortal(ingester=MockDataRetriever('test'), pairs=pairs)
        dp.ingest()
        data_api = DataAPI(data_portal=dp, traded_pairs=pairs)
        value = data_api.history(pairs=pairs[0], ticks=2)
        self.assertTrue(pairs[0] in value)
        self.assertEquals(len(value), 1)
        self.assertEquals(len(value[pairs[0]]), 2)
