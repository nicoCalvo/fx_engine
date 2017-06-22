import json


class OrderAdapter(object):
    PRICE_KEYS = ['symbol', 'date', 'asset_class', 'price']

    def __init__(self):
        self.data_portal = None

    def _adapt_ticker(self):
        tick = self.data_portal.current_tick
        symbols = []
        for symbol in tick:
            price_item = dict.fromkeys(self.PRICE_KEYS)
            price_item['symbol'] = symbol['symbol']
            price_item['date'] = symbol['time']
            price_item['asset_class'] = 'fx_spot'
            price_item['price'] = round((symbol['bid'] + symbol['ask']) / 2, 4)
            symbols.append(price_item)
        return  symbols

    def get_order_messsage(self, orders):
        date = self.data_portal.current_tick[0]['time']
        for order in orders:
            order['date'] = date
        prices = self._adapt_ticker()
        return json.dumps(dict(new_orders=orders, new_prices=prices))
