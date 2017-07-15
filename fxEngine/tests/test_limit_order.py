import unittest
from fxEngine.order.limit_order import LimitOrder
from fxEngine.order.base_order import BaseOrder
from collections import namedtuple

Portfolio = namedtuple('Portfolio','cash')


class TestLimitOrder(unittest.TestCase):

	def setUp(self):
		pass

	def test_inheritance(self):
		symbol='USDEUR'
		price = 100
		amount = 100
		order_number = 0
		limit_order = LimitOrder(symbol, price, amount, order_number)
		self.assertTrue(isinstance(limit_order, BaseOrder))


	def test_valid_amount(self):
		symbol='USDEUR'
		portfolio = Portfolio(200)
		price = 100
		amount = 100
		order_number = 0
		limit_order = LimitOrder(symbol, price, amount, order_number)
		self.assertTrue(limit_order.is_valid(portfolio))


	def test_invalid_amount(self):
		symbol='USDEUR'
		portfolio = Portfolio(200)
		price = -1
		amount = 300
		order_number = 0
		limit_order = LimitOrder(symbol, price, amount, order_number)
		self.assertFalse(limit_order.is_valid(portfolio))

