from data.symbols import Symbol
from utils.exceptions import (
    TradingSymbolForbidden)


class TradingSimulator(object):

    def __init__(self, str_strategy, symbols, id_strategy):
        self.strategy = self.__load_strategy(str_strategy)
        
        is_valid, forb_symbols = self._validate_symbols(symbols)
        if not is_valid:
            raise TradingSymbolForbidden(forb_symbols)

        self.symbols = Symbol

    def _validate_symbols(self, symbols):

        forbidden_symbols = [x for x in symbols if x[
            0] in Symbol.is_allowed(x[0])]

        return True, [] if not forbidden_symbols else False, forbidden_symbols

    def __load_strategy(self, strategy):
        pass