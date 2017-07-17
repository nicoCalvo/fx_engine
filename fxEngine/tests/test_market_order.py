import unittest
from fxEngine.order.market_order import MarketOrder
from fxEngine.order.base_order import BaseOrder
from collections import namedtuple
import json

Portfolio = namedtuple('Portfolio','cash')


class TestMarketOrder(unittest.TestCase):
	KEYS_REPR = ['order_id', 'limit_price', 'amount', 'stop_price', 'order_type', 'symbol']

	def setUp(self):
		pass

	def test_inheritance(self):
		symbol='USDEUR'
		amount = 100
		order_number = 0
		limit_order = MarketOrder(symbol, amount, order_number)
		self.assertTrue(isinstance(limit_order, BaseOrder))


	def test_valid_amount(self):
		symbol='USDEUR'
		portfolio = Portfolio(200)
		amount = 100
		order_number = 0
		limit_order = MarketOrder(symbol, amount, order_number)
		self.assertTrue(limit_order.is_valid(portfolio))

		

	def test_repr(self):
		symbol='USDEUR'
		amount = 300
		order_number = 0
		limit_order = MarketOrder(symbol, amount, order_number)
		res = str(limit_order)
		res_j = json.loads(res)
		keys = [x for x, y in res_j.items()]
		self.assertEquals(set(keys), set(self.KEYS_REPR))
