import unittest
import mock
from collections import namedtuple
from fxEngine.order.order_scheduler import OrderScheduler

Strategy = namedtuple('Strategy','id')


class MockOrderManager(object):

    
    def __init__(self):
        self._strategy = Strategy('test/1/d3eds4')

    def _update_open_orders(self, filled_orders):
        pass


class TestOrderScheduler(unittest.TestCase):

    def setUp(self):
        pass

    @mock.patch('fxEngine.order.order_scheduler.OrderScheduler._get_orders')
    def test_get_empty_filled_orders(self, mock_orders):
        order_scheduler = OrderScheduler(MockOrderManager(), None)
        mock_orders.return_value = '''{"list_filled_orders":[]}'''
        order_scheduler.update()
        self.assertTrue(mock_orders.called)



    @mock.patch('fxEngine.order.order_scheduler.OrderScheduler._get_orders')
    def test_update_order_manager(self, mock_orders):
        order_scheduler = OrderScheduler(MockOrderManager(), None)
        mock_orders.return_value = '''
        {
         "list_filled_orders": [{
          "order_id": "order_2",
          "algorithm_instance_id": "test_algorithm",
          "amount": -120.0,
          "symbol": "USDEUR",
          "date": "2012/12/31 00:10:22",
          "order_type": "market_order",
          "price": 12.2
         }],
         "list_prices": [{
          "symbol": "USDEUR",
          "date": "2012/12/31 00:10:22",
          "asset_class": "fx_spot",
          "price": 12.2
         }]
        }
        '''
        order_scheduler.update()



