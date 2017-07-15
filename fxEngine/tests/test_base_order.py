import unittest
from fxEngine.order.base_order import BaseOrder


class TestBaseOrder(unittest.TestCase):

	def setUp(self):
		pass

	def test_abstract_constructor(self):
		self.assertRaises(TypeError,BaseOrder, 1,0,0)

