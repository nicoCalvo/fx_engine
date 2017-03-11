

from order_route_client import OrderRouter


class OrderManager(object):

    def __init(self, traded_pairs_list):
        self.order_router = OrderRouter()
        self.pairs = traded_pairs_list

    def get_open_orders(self):
        '''
        TODO: define order_router return and how
        data will be showed to devs
        '''
        orders = self.order_router.get_open_orders()
        return orders

    def cancel_all_open_orders(self):
        self.order_router.cancel_orders()

    def cancel_pair_orders(self, pair):
        self.order_router.cancel_pair_orders(pair.name)

    def limit_order(pair, pips, due_date):
        pass

    def stop_order(pair, price, due_date):
        pass
