import unittest
import mock
from fxEngine.order.order_router_client import OrderRouter

class TestOrderRouter(unittest.TestCase):

	def setUp(self):
		pass



	def test_init_(self):
		order_router = OrderRouter('asda')
		