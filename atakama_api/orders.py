
from fxEngine.order.order_router_client import OrderRouter
from fxEngine.order.order_adapter import OrderAdapter
from fxEngine.data.dto import Portfolio
from fxEngine.order.exceptions import (
    InvalidPairOrder,
    InvalidDueDate,
    InvalidPriceOrder
)
from fxEngine.order.limit_order import LimitOrder
from fxEngine.order.stop_order import StopOrder
from fxEngine.order.market_order import MarketOrder
import json


class OrderManager(object):
    MAX_PLACE_ORDERS = 5
    MAX_OPEN_ORDERS = 100

    def __init__(self, _id):
        '''
        This class handles all operations related to orders.
        Using current strategy's portfolio status, the  order manager
        is able to validate requested action and, if valid, place the
        order in the order scheduler

        Parameters:
        ----------
            _order_router: OrderRouter
            _strategy: Dto strategy
            _looger: Logger
            _context : StrategyContext
            _order_adapter: OrderAdapter
            _open_orders: [] List of Orders opened and scheduled
            _new_orders: Orders placed, ready to be validated and sent to the
            OrderScheduler

        Attributes:
        ----------
        order_router: order router client
        nested structure:


        pair:
             open_orders:
                    id (interno)

                    placed date
                    amount
                    type


        positions:
            pair:
                aggregated: [position]

        '''
        self._counter = 0
        self._counter_new_orders = 0
        self._order_router = OrderRouter(_id)
        self._open_orders = []
        self._new_orders = []
        self._strategy = None
        self._logger = None
        self._context = None
        self._order_adapter = OrderAdapter()
        self._canceled_orders = []
        self._rejected_orders = []

    def get_open_orders(self):
        return self._open_orders

    def cancel_all_open_orders(self):
        self._canceled_orders = []  # Avoid cancel same order if cancel_pair_orders was used
        self._canceled_orders = self._open_orders
        self._open_orders = []

    def cancel_pair_orders(self, pair):
        if pair not in self._strategy.traded_pairs:
            self._logger.error('TRADED PAIR NOT IN LIST: {}'.format(pair))

        cancel_orders = [
            order for order in self._open_orders if order.symbol == pair]
        for order in cancel_orders:
            if order not in self._canceled_orders:
                self._canceled_orders.append(order)

    def limit_order(self, pair, amount, price, due_date=None):
        due_date = due_date or ''
        if pair not in self._strategy.traded_pairs:
            self._logger.error('TRADED PAIR NOT IN LIST: {}'.format(pair))
            return
        if self._counter_new_orders > self.MAX_PLACE_ORDERS:
            self._logger('MAX PLACING ORDERS REACHED - UNABLE TO PROCESS ORDER : {order}'.format(
                str(LimitOrder(pair, amount, price, self._counter))))
            return
        self._new_orders.append(LimitOrder(pair, amount, price, self._counter))
        self._counter += 1
        self._counter_new_orders += 1

    def stop_order(self, pair, amount, price, due_date=None):
        due_date = due_date or ''
        if pair not in self._strategy.traded_pairs:
            self._logger.error('TRADED PAIR NOT IN LIST: {}'.format(pair))
            return
        if self._counter_new_orders > self.MAX_PLACE_ORDERS:
            self._logger('MAX PLACING ORDERS REACHED - UNABLE TO PROCESS ORDER : {order}'.format(
                str(StopOrder(pair, amount, price, self._counter))))
            return
        self._new_orders.append(
            StopOrder(pair, amount, price, self._counter))
        self._counter += 1
        self._counter_new_orders += 1

    def market_order(self, pair, amount, due_date=None):
        due_date = due_date or ''
        if pair not in self._strategy.traded_pairs:
            self._logger.error('TRADED PAIR NOT IN LIST: {}'.format(pair))
            return
        if self._counter_new_orders > self.MAX_PLACE_ORDERS:
            self._logger('MAX PLACING ORDERS REACHED - UNABLE TO PROCESS ORDER : {order}'.format(
                str(MarketOrder(pair, amount, self._counter))))
            return
        else:
            self._new_orders.append(MarketOrder(pair, amount, self._counter))
            self._counter += 1
            self._counter_new_orders += 1

    def order_counter_position(self, pair, amount):
        self._new_orders.append(MarketOrder(pair, amount, self._counter))

    def _publish_orders(self):

        if not all([x.is_valid(self._context.portfolio) for x in self._new_orders]):
            invalid_orders = self._get_invalid_orders()
            self._rejected_orders += invalid_orders
            self._notify_invalid_orders(invalid_orders)
        orders = self._order_adapter.get_order_messsage(
            self._new_orders, self._canceled_orders)
        print 'PUBLISHING ORDERS: {orders} - Exchange: {ex}'.format(orders=orders, ex='E_new_orders_strategy')
        self._order_router.publish_orders(orders or "[]")
        [self._open_orders.append(x) for x in self._new_orders]
        self._new_orders = []
        self._canceled_orders = []

    def _get_invalid_orders(self):
        invalid_orders = []
        for pos, order in enumerate(self._new_orders):
            if not order.is_valid(self._context.portfolio):
                invalid_orders.append(str(order))
                del self._new_orders[pos]
        return invalid_orders

    def _update_open_orders(self, filled_orders):
        filled_orders_id = [x['order_id'] for x in filled_orders]
        for pos, order in enumerate(self._open_orders):
            if order.order_id in filled_orders_id:
                del self._open_orders[pos]

    def _notify_invalid_orders(self, invalid_orders):
        pass

    def get_rejected_orders(self):
        return self._rejected_orders

    def __repr__(self):
        return 'OrderManager'

    def __dict__(self):
        return 'OrderManager'
