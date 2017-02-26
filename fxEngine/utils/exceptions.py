

class TradingSymbolForbidden(Exception):

    msg = 'Symbols not allowed for FX trading: '

    def __init__(self, symbols):
        super(TradingSymbolForbidden, self).__init__(self.msg + str(symbols))


class InvalidCapitalBase(Exception):

    base_msg = 'Initial capital must be > 0 '

    def __init__(self):
        super(InvalidCapitalBaseException, self).__init__(self.base_msg)



class InvalidPairError(Exception):

    base_msg = 'Requested pair is not included in the simulation: '

    def __init__(self, msg):
        super(InvalidPairError, self).__init__(self.base_msg + msg)
