from .base_order import BaseOrder


class StopOrder(BaseOrder):

    def __init__(self, symbol, price, amount, order_number):
        super(StopOrder, self).__init__(symbol=symbol, amount=amount,
                                        stop_price=price,
                                        order_number=order_number)

    def is_valid(self, portfolio):
        return self._validate_price_amount(portfolio)
