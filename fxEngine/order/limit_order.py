from .base_order import BaseOrder


class LimitOrder(BaseOrder):

    def __init__(self, symbol, price, amount, order_number):
        super(LimitOrder, self).__init__(symbol=symbol, limit_price=price,
                                         amount=amount,
                                         order_number=order_number)

    def is_valid(self, portfolio):
        return self._validate_price_amount(portfolio)
