

class TradingSymbolForbidden(Exception):

    msg = 'Symbols not allowed for FX trading: '

    def __init__(self, symbols):
        super(TradingSymbolForbidden, self).__init__(self.msg + str(symbols))
