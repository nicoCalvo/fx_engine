

class Symbol(object):
    __slots__ = ('allowed_symbols')
    allowed_symbols = ['USD/EUR', 'ARS/USD']

    def __init__(self):
        pass

    @classmethod
    def is_allowed(self, symbol):
        return symbol in self.allowed_symbols
