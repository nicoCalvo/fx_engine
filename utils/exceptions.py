

class TradingSymbolForbidden(Exception):

    msg = 'Symbols not allowed for FX trading: '

    def __init__(self, symbols):
        super(TradingSymbolForbidden, self).__init__(self.msg + str(symbols))


class CompileMethodException(Exception):

    base_msg = 'Unable to compile code: '

    def __init__(self, msg):
        super(CompileMethodException, self).__init__(self.base_msg + msg)
