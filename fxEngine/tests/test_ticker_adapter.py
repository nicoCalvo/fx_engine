import unittest
import mock
from fxEngine.data.ticker_adapter import TickerAdapter
from fxEngine.data.ticker_filter import TickerFilter
import pandas as pd

class TestTickerAdapter(unittest.TestCase):
	ticker = current_tick = [{"ask": 7.44185, "bid": 7.44135, "medium": 7.4416, "symbol": "EURDKK", "time": "2010/01/04 00:00:00"}, {"ask": 1.44146, "bid": 1.44126, "medium": 1.44136, "symbol": "USDEUR", "time": "2010/01/04 00:00:00"}]

	def setUp(self):
		pass

	def test_get_ticker_single_pair_single_value(self):
		ticker_adapter = TickerAdapter()
		ask = ticker_adapter.get_ticker(self.ticker, ['USDEUR'], ['ask'])
		self.assertTrue(isinstance(ask, float))

	def test_get_ticker_single_pair_many_values(self):
		ticker_adapter = TickerAdapter()
		ticker = ticker_adapter.get_ticker(self.ticker, ['USDEUR'], TickerFilter._allowed_values)
		ticker.index.values.tolist()
		self.assertTrue(isinstance(ticker, pd.Series))
		self.assertEquals(ticker.index.values.tolist(), TickerFilter._allowed_values)


	def test_get_ticker_many_pairs_many_values(self):
		ticker_adapter = TickerAdapter()
		ticker = ticker_adapter.get_ticker(self.ticker, ['USDEUR','EURDKK'], TickerFilter._allowed_values)
		self.assertTrue(isinstance(ticker, pd.DataFrame))
		self.assertEquals(ticker.columns.values.tolist(), TickerFilter._allowed_values)
		self.assertEquals(ticker.index.values.tolist(), ['USDEUR','EURDKK'])



	def test_get_ticker_many_pairs_single_value(self):
		ticker_adapter = TickerAdapter()
		ticker = ticker_adapter.get_ticker(self.ticker, ['USDEUR','EURDKK'], [TickerFilter._allowed_values[0]])
		self.assertTrue(isinstance(ticker, pd.Series))
		self.assertEquals(ticker.index.values.tolist(),  ['USDEUR','EURDKK'])

