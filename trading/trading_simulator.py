from data.symbols import Symbol
# from strategy.strategy import Strategy
from strategy.api_compiler import StrategyCompiler
from strategy.api_method import ApiStrategy
from utils.exceptions import (
    TradingSymbolForbidden
)
from data.data_portal import DataPortal
from zip_performance.tracker import PerformanceTracker



class TradingSimulator(object):
    '''
    TradingSimulator is the main class that defines, creates and
    customize the context for an strategy to be run

    Parameters:
    ==========

    str_strategy: The literal string of code (strategy) to be compiled and run
    symbols: List of FX assets that will be part of the strategy
    id_strategy: External ID assigned for this strategy
    '''

    def __init__(self, str_strategy, symbols, id_strategy):
        self.namespace = {}

        self.api_method = ApiStrategy(str_strategy, StrategyCompiler(str_strategy))
        self.strategy = self._load_strategy(str_strategy)
        forb_symbols = self._validate_symbols(symbols)
        if forb_symbols:
            raise TradingSymbolForbidden(forb_symbols)
        self.symbols = [Symbol(x) for x in symbols]

    def _validate_symbols(self, symbols):
        return[x for x in symbols if not Symbol.is_allowed(x)]

    def _load_strategy(self, str_ategy):
        # TODO: Define methods to be loaded such as handle_data,initialize inside str_ategy
        # FIXME: under exec_ method, determine the need and purpose of passing
        # a namespace as third param: exec_(comp_str, namespace)
        try:
            self.api_method.compile_strategy()
        except:
            raise


    def simulate(self):
        '''
        Calendar con los trading days
        Mergear los datos historicos de los assets con el calendar
        recorrer por cada "tick" del calendar
        

        '''
        data_portal = DataPortal(ingester=None,pairs_list=['ars_eur', 'eur_dol', 'ars_mex', 'dol_mex'], calendar=None)
        data_portal.ingest()

        perf_tracker = PerformanceTracker()












































   
