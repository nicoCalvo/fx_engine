from .base_order import BaseOrder

class MarketOrder(BaseOrder):

    def __init__(self, symbol, amount, order_number):
        super(MarketOrder, self).__init__(symbol=symbol,amount=amount,
                                        order_number=order_number)

    def is_valid(self, portfolio):
    	return True




