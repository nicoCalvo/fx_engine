from data.pair import Pair
# from strategy.strategy import Strategy
from strategy.api_compiler import StrategyCompiler
from strategy.api_method import ApiStrategy
from strategy.dto_strategy import DTOStrategy
from utils.exceptions import (
    TradingSymbolForbidden,
    InvalidCapitalBase
)
from data.data_portal import DataPortal
from zip_performance.tracker import PerformanceTracker
from .trading_environment import TradingEnvironment


class TradingSimulator(object):
    '''
    TradingSimulator is the main class that defines, creates and
    customize the context for an strategy to be run ( Algorithm alike in zipline)

    Parameters:
    ==========

    str_strategy: The literal string of code (strategy) to be compiled and run
    symbols: List of FX assets that will be part of the strategy
    id_strategy: External ID assigned for this strategy
    '''

    def __init__(self, dto_strategy):
        self.namespace = {}

        self.api_method = ApiStrategy(StrategyCompiler(dto_strategy.str_strategy))

        self.strategy = self._load_strategy()
        forb_fx_pairs = self._validate_symbols(dto_strategy.fx_pairs)
        if forb_fx_pairs:
            raise TradingSymbolForbidden(forb_fx_pairs)
        self.pairs = [Pair(x) for x in dto_strategy.fx_pairs]
        self.trading_environment = TradingEnvironment()
        self.capital_base = self._validate_initial_capital(dto_strategy.capital_base)

        '''
            Consider creation of StrategyEnvironment that holds trading controls and account_controls
            and records all the vars plus namespace and calendar

        '''
        # List of trading controls to be used to validate orders.
        self.trading_controls = []

        # List of account controls to be checked on each bar.
        self.account_controls = []
    
        self._recorded_vars = {}
        self.namespace = {} # Me hace ruido, no tiene cohesion con la clase


        #TODO: Decide if its going to be needed a Calendar for Fx

        self.trading_calendar = kwargs.pop(
            'trading_calendar',
            get_calendar("NYSE")
        )


    def _validate_pairs(self, pairs):
        return[x for x in pairs if not Pair.is_allowed(x)]

    def _load_strategy(self):
        # TODO: Define methods to be loaded such as handle_data,initialize inside str_ategy
        # FIXME: under exec_ method, determine the need and purpose of passing
        # a namespace as third param: exec_(comp_str, namespace)
        try:
            self.api_method.compile_strategy()
        except:
            raise

    def _validate_initial_capital(capital_base):
        if capital_base <= 0:
            raise InvalidCapitalBase()
        return capital_base

    def simulate(self):
        '''
        Calendar con los trading days
        Mergear los datos historicos de los assets con el calendar
        recorrer por cada "tick" del calendar
        

        '''
        # self.symbols = ['ars_eur', 'eur_dol', 'ars_mex', 'dol_mex'] Just for test, can be deleted without problem

        data_portal = DataPortal(ingester=None, pairs_list=self.symbols,
                                 calendar=None)
        data_portal.ingest()

        perf_tracker = PerformanceTracker()
        sim_params = self._create_simulation_parameters()

        '''
        crear el Blotter con el VolumeShareSlippage

        '''
        # If an env has been provided, pop it
    
   
        # TOINVESTIGATE: Difference btw data_frequency and emission_rate

        "CONTINUE IN run_algo.py INIT METHOD TO DECIDE THE CONSTRUCTION OF THE TRADING_SIMULATOR  \
         FIND DIFFERENCES BETWEEN TradingEnvironment and DataPortal, does it worth it?"
         #Context: this stupid variable is the environment to execute the algo
         # in zipline refers to self for TradingAlgorithm

        sim_params = SimulationParameters(
            start_session=start,
            end_session=end,
            capital_base=capital_base,
            data_frequency=data_frequency,
            emission_rate=emission_rate, # WTF?? This is not used EVERRR
            trading_calendar=self.trading_calendar,
        )
        return sim_params
           










































   
