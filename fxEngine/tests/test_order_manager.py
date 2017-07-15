import unittest
from atakama_api.orders import OrderManager
from fxEngine.order.limit_order import LimitOrder
from fxEngine.order.market_order import MarketOrder
import mock
from collections import namedtuple

Strategy = namedtuple('Strategy', 'traded_pairs')
Portfolio = namedtuple('Portfolio', 'cash')

class MockOrderAdapter(mock.Mock):

    def __init__(self):
        pass

    def get_order_messsage(self, new_orders, canceled_orders):
        pass

class MockOrderRouter(mock.Mock):

    def __init__(self, id):
        pass


    def publish_orders(self, orders):
        pass

    def cancel_all_open_orders(self):
        pass

class MockLogger(mock.Mock):

    def __init__(self):
        pass

    def error(self, msg):
        pass

    def info(self, msg):
        pass


class MockContextPortfolio(object):

    def __init__(self):
        self.portfolio = Portfolio(100)



class TestOrderManager(unittest.TestCase):

    @mock.patch('atakama_api.orders.OrderRouter', side_effect=MockOrderRouter)
    @mock.patch('atakama_api.orders.OrderAdapter', side_effect=MockOrderAdapter)
    def setUp(self, mock_adapter, mock_order_router):
        self.order_manager = OrderManager('test_id')
        self.order_manager._context = MockContextPortfolio()
        self.order_manager._logger = MockLogger()
        self.order_manager._order_router = MockOrderRouter('test_id')
        self.order_manager._strategy = Strategy(traded_pairs=['USDEUR','EURDKK'])
        self.assertTrue(mock_adapter.called)
        self.assertTrue(mock_order_router.called)


    def test_valid_limit_order(self):
        self.order_manager.limit_order('USDEUR', 2,3)
        limit_order = self.order_manager._new_orders[0]
        self.assertTrue(isinstance(limit_order, LimitOrder))
        self.order_manager._new_orders[:] = []
    
    def test_invalid_pair_limit_order(self):
        self.order_manager._new_orders[:] = []
        self.order_manager.limit_order('ASDASD', 2,3)
        self.assertFalse(self.order_manager._new_orders)

    def test_market_order(self):
        self.order_manager.market_order('USDEUR', 1200)

        self.assertTrue(isinstance(self.order_manager._new_orders[0],
                                   MarketOrder))


    def test_update_open_orders(self):
        self.order_manager._new_orders[:] = []
        self.order_manager.limit_order('USDEUR', -2,-23)
        filled_orders = [{
          "order_id": "order_2",
          "algorithm_instance_id": "test_algorithm",
          "amount": -120.0,
          "symbol": "USDEUR",
          "date": "2012/12/31 00:10:22",
          "order_type": "market_order",
          "price": 12.2
        }]
        
        order_id = self.order_manager._new_orders[0].order_id
        filled_orders[0]['order_id'] = order_id
        self.order_manager._publish_orders()
        self.order_manager._update_open_orders(filled_orders)
        self.assertTrue(not self.order_manager._open_orders)

    def test_cancel_open_orders(self):
        self.order_manager._new_orders[:] = []
        self.order_manager.limit_order('USDEUR', 2,3)
        self.order_manager._publish_orders()
        self.assertTrue(self.order_manager._open_orders)
        self.order_manager.cancel_all_open_orders()
        self.assertTrue(not self.order_manager._open_orders)
        self.assertTrue(self.order_manager._canceled_orders)


    def test_cancel_pair_orders(self):
        self.order_manager._new_orders[:] = []
        self.order_manager.limit_order('USDEUR', 2,3)
        self.order_manager.limit_order('EURDKK', 555,999)
        self.order_manager._publish_orders()
        self.assertEquals(len(self.order_manager._open_orders), 2)
        self.order_manager.cancel_pair_orders('USDEUR')
        self.assertEquals(len(self.order_manager._canceled_orders), 1)

    