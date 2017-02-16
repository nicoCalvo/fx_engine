from fxEngine.data.pair import Pair
from strategy.strategy_compiler import StrategyCompiler
from strategy.api_strategy import ApiStrategy
from utils.exceptions import (
    TradingSymbolForbidden,
    InvalidCapitalBase
)
from data.data_portal import DataPortal
from performance.performance_tracker import PerformanceTracker
from tests.data_demo_loader import DemoLoader
from simulation_manager import SimulationManager


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
        self._validate_pairs(dto_strategy.fx_pairs)
        self._validate_initial_capital(dto_strategy.capital_base)
        self.api_strategy = ApiStrategy(
            StrategyCompiler(dto_strategy.str_strategy), dto_strategy)
        self._load_strategy()
        self.pairs = [Pair(x) for x in dto_strategy.fx_pairs]

        '''
            Consider creation of StrategyEnvironment
            that holds trading controls and account_controls
            and records all the vars plus namespace and calendar

        '''
    def _validate_pairs(self, pairs):
        forb_fx_pairs = [x for x in pairs if not Pair.is_allowed(x)]
        if forb_fx_pairs:
            raise TradingSymbolForbidden(forb_fx_pairs)

    def _load_strategy(self):
        try:
            self.api_strategy.compile_strategy()
        except:
            raise

    def _validate_initial_capital(self, capital_base):
        if capital_base <= 0:
            raise InvalidCapitalBase()

    def simulate(self, clock):
        perf_tracker = PerformanceTracker(strategy=self.api_strategy)
        data_portal = DataPortal(ingester=DemoLoader(), pairs_list=self.pairs,
                                 observers=perf_tracker)
        data_portal.ingest()
        _clock = clock(data_portal)
        '''
        crear el Blotter con el VolumeShareSlippage

        '''
        # If an env has been provided, pop it

        # TOINVESTIGATE: Difference btw data_frequency and emission_rate
        # TOINVESTIGATE: Identify somehow a new date and trigger methods to be
        # executed on new date

        # El clock determina una fecha nueva
        # Al tener fecha nueva se dispara un manager que las ejecute
        # dividir el strategy compiler y si existe alguna funcion a ser ejecutada cada dia o al cierre de
        # cada dia, pasarsela a un manager e instanciarlo

        self.api_strategy.initialize()
        while self.clock.has_new_tick():
            self.api_strategy.handle_data()
        simulation_manager = SimulationManager(_clock, self.api_strategy)
        simulation_manager.simulate()
        # "CONTINUE IN run_algo.py INIT METHOD TO DECIDE THE CONSTRUCTION OF THE TRADING_SIMULATOR  \
        #  FIND DIFFERENCES BETWEEN TradingEnvironment and DataPortal, does it worth it?"
        # Context: this stupid variable is the environment to execute the algo
        # in zipline refers to self for TradingAlgorithm
