import unittest
from fxEngine.order.order_adapter import OrderAdapter
import mock
import json


class MockDataPortal(mock.Mock):

    current_tick = [{"ask": 7.44185, "bid": 7.44135, "medium": 7.4416, "symbol": "EURDKK", "time": "2010/01/04 00:00:00"},
                    {"ask": 1.44146, "bid": 1.44126, "medium": 1.44136, "symbol": "USDEUR", "time": "2010/01/04 00:00:00"}]


class TestOrderAdapter(unittest.TestCase):
    new_orders = [{"order_type": "LimitOrder", "order_id": "MHw1MDM=", "amount": 3, "stop_price": 0.0,
                   "limit_price": 2, "symbol":"USDEUR"},
                  {"order_type": "LimitOrder", "order_id": "MXwyODE=", "amount": 999,
                   "stop_price": 0.0, "limit_price": 555,"symbol":"EURDKK"}]

    def setUp(self):
        pass

    def test_adapt_ticker(self):
        order_adapter = OrderAdapter()
        order_adapter.data_portal = MockDataPortal()
        ticker = order_adapter._adapt_ticker()
        self.assertTrue('price' in ticker[0])
        medium = round((MockDataPortal.current_tick[0]['bid'] +
                        MockDataPortal.current_tick[0]['ask']) / 2, 4)
        self.assertTrue('price' in ticker[0])
        self.assertEquals(ticker[0]['price'], medium)

    def test_get_order_messages_no_cancel(self):
        order_adapter = OrderAdapter()
        order_adapter.data_portal = MockDataPortal()
        orders_msg = order_adapter.get_order_messsage(self.new_orders, [])
        orders_msg = json.loads(orders_msg)
        self.assertTrue(not orders_msg['canceled_orders'])
        self.assertEquals(len(orders_msg['new_orders']), 2)

    def test_get_order_messages_cancel_orders(self):
        order_adapter = OrderAdapter()
        order_adapter.data_portal = MockDataPortal()
        canceled_orders = [{"order_type": "LimitOrder", "order_id": "MHwxNTI=",
                            "amount": 3, "stop_price": 0.0,
                            "limit_price": 2,
                            "symbol":"USDEUR"}]
        
        orders_msg = order_adapter.get_order_messsage(
            self.new_orders, canceled_orders)
        orders_msg = json.loads(orders_msg)
        self.assertTrue(orders_msg['canceled_orders'])
        self.assertEquals(len(orders_msg['new_orders']), 2)
