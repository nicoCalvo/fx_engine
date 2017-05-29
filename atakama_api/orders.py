from fxEngine.order.order_router_client import OrderRouter
from fxEngine.order.exceptions import (
    InvalidPairOrder,
    InvalidDueDate,
    InvalidPriceOrder
)
import json


def validate_params(function):
        def validate(*args):
            pair = args[0]
            price = args[1]
            # due_date = args[2]
            if pair in OrderManager.strategy.traded_pairs:
                self._logger.info('Pair not selected for trading')
                raise InvalidPairOrder(pair)
            if not isinstance(price, float):
                raise InvalidPriceOrder(pair)
                self._logger.info('Invalid Price order')
            # today = OrderManager.clock.new_date
            # if due_date <= today:
            #     raise InvalidDueDate(due_date)
            function(*args)


class OrderManager(object):

    def __init__(self, _id):
        '''
        This class handles all operations related to orders.
        Using current strategy's portfolio status, the  order manager
        is able to validate requested action and, if valid, place the
        order in the order scheduler

        Parameters:
        ----------

        Attributes:
        ----------
        order_router: order router client

        '''
        self.order_router = OrderRouter(_id)
        self._orders = []
        self._logger = ''
        self._context = ''

    def get_open_orders(self):
        '''
        TODO: define order_router return and how
        data will be showed to devs
        '''
        orders = self.order_router.get_open_orders()
        return orders

    def cancel_all_open_orders(self):
        self.perf_tracker.get_portfolio()
        self.order_router.cancel_orders()

    def cancel_pair_orders(self, pair):
        if pair in self.pairs:
            self.order_router.cancel_pair_orders(self.strategy.id, pair.name)
            raise InvalidPairOrder(pair)

    #@validate_params
    def limit_order(self, pair, price, due_date=None):

        due_date = due_date or ''
        limit_order = dict(type='limit', pair=pair, price=price)
        self._orders.append(limit_order)
        # self.log.write('LIMIT ORDER: ' + pair.name + '  DATE: ' + due_date)

        #self.order_router.limit_order(self.strategy.id, pair, price, due_date)

    # @validate_params
    def stop_order(self, pair, price, due_date=None):
        due_date = due_date or ''
        stop_order = dict(order)
        #self.log.write('STOP ORDER: ' + pair.name + '  DATE: ' + due_date)
        
    def _publish_orders(self):
        cash = self._context.portfolio.value
        amount = sum([x['price'] if x['type'] == 'limit' else 0 for x in self._orders] )

        if cash > amount:
            # publish orders
            if self._orders:
                self._logger.info('ORDERS PLACED: ' + json.dumps(self._orders))
        elif amount > 0:
            self._logger.info('NOT ENOUGH CASH TO TRADE ORDER: ' + str()) 
        # self.order_router.publish_orders(self._orders)
        self._orders = []
