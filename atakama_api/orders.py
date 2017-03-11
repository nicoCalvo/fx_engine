from fxEngine.order.order_router_client import OrderRouter
from fxEngine.order.exceptions import (
    InvalidPairOrder,
    InvalidDueDate,
    InvalidPriceOrder
)


class OrderManager(object):
    STRATEGY = ''
    CLOCK = ''

    def __init__(self):
        '''
        This class handles all operations related to orders.
        Using current strategy's portfolio status, the  order manager
        is able to validate requested action and, if valid, place the
        order in the order scheduler

        Parameters:
        ----------

        Attributes:
        ----------
        STRATEGY: DTOStrategy
        CLOCK: current simulation clock
        order_router: order router client

        '''
        self.order_router = OrderRouter()
        self.log = open('orders.log', 'w')

    def validate_params(function):
        def validate(*args):
            pair = args[0]
            price = args[1]
            due_date = args[2]
            if pair in OrderManager.strategy.traded_pairs:
                raise InvalidPairOrder(pair)
            if not isinstance(price, float):
                raise InvalidPriceOrder(pair)
            today = OrderManager.clock.new_date
            if due_date <= today:
                raise InvalidDueDate(due_date)
            function(*args)

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

    @validate_params
    def limit_order(self, pair, price, due_date=None):
        due_date = due_date or ''
        self.log.write('LIMIT ORDER: ' + pair.name + '  DATE: ' + due_date)
        self.order_router.limit_order(self.strategy.id, pair, price, due_date)

    @validate_params
    def stop_order(self, pair, price, due_date=None):
        due_date = due_date or ''
        self.log.write('STOP ORDER: ' + pair.name + '  DATE: ' + due_date)
        self.order_router.limit_order(self.strategy.id, pair_name,
                                      price, due_date)

    
