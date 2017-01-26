from data.symbols import Symbol
from strategy.strategy import Strategy
from utils.exceptions import (
    TradingSymbolForbidden
    )


class TradingSimulator(object):

    def __init__(self, str_strategy, symbols, id_strategy):
        self.strategy = self._load_strategy(str_strategy)
        forb_symbols = self._validate_symbols(symbols)
        if forb_symbols:
            raise TradingSymbolForbidden(forb_symbols)
        self.symbols = [Symbol(x) for x in symbols]

    def _validate_symbols(self, symbols):

        forbidden_symbols = [x for x in symbols if not Symbol.is_allowed(x)] 

        return forbidden_symbols

    def _load_strategy(self, str_ategy):
        #TODO: Define methods to be loaded such as handle_data, initialize inside str_ategy
        '''

        '''
        compiled_str = compile(str_ategy, '', 'exec')
        exec(compiled_str)
        strategy = Strategy()
        strategy.algo = algo
        strategy.algomas = algomas
        foo()
        return strategy