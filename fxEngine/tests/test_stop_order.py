import unittest
from fxEngine.order.stop_order import StopOrder
from fxEngine.order.base_order import BaseOrder
from collections import namedtuple

Portfolio = namedtuple('Portfolio','cash')


class TestStopOrder(unittest.TestCase):

	def setUp(self):
		pass

	def test_inheritance(self):
		symbol='USDEUR'
		price = 100
		amount = 100
		order_number = 0
		stop_order = StopOrder(symbol, price, amount, order_number)
		self.assertTrue(isinstance(stop_order, BaseOrder))


	def test_valid_amount(self):
		symbol='USDEUR'
		portfolio = Portfolio(200)
		price = 100
		amount = 100
		order_number = 0
		stop_order = StopOrder(symbol, price, amount, order_number)
		self.assertTrue(stop_order.is_valid(portfolio))


	def test_invalid_amount(self):
		symbol='USDEUR'
		portfolio = Portfolio(200)
		price = 100
		amount = 300
		order_number = 0
		stop_order = StopOrder(symbol, price, amount, order_number)
		self.assertTrue(stop_order.is_valid(portfolio))
	
