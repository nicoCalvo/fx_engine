from abc import ABCMeta, abstractmethod
import random
import base64


class BaseOrder(object):
    __metaclass__ = ABCMeta

    def __init__(self, symbol, amount, stop_price=0.0, limit_price=0.0,
                 order_number=-1):
        self.symbol = symbol
        self.amount = amount
        self.stop_price = stop_price
        self.limit_price = limit_price
        self.order_id = self._generate_order_id(order_number)

    @abstractmethod
    def is_valid(self, portfolio):
        pass

    def _validate_price_amount(self, portfolio):
        return ((self.limit_price > 0 or self.stop_price > 0)
                and self.amount <= portfolio.cash)

    def __repr__(self):
        return'{' + '"order_type": "{order_type}", "order_id": "{order_id}",\
                "amount": {amount}, "stop_price": {stop_price},\
                "limit_price":{limit_price}, "symbol":"{symbol}"\
                '.format(order_type=self.__class__.__name__,
                         amount=self.amount, stop_price=self.stop_price,
                         limit_price=self.limit_price,
                         order_id=self.order_id, symbol=self.symbol) + '}'

    def _generate_order_id(self, order_number):
        order_number = str(order_number)
        str_random = order_number + '|' + str(random.randint(100, 1000))
        b64_random = base64.b64encode(str_random)
        return b64_random
