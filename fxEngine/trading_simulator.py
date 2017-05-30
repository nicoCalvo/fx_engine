# import pyximport
# pyximport.install()
# from fxEngine.data.pair import Pair
from fxEngine.strategy.strategy_compiler import StrategyCompiler
from fxEngine.strategy.api_strategy import ApiStrategy
from fxEngine.utils.exceptions import (
    TradingSymbolForbidden,
    InvalidCapitalBase
)
from data.data_portal import DataPortal
from fxEngine.performance.performance_tracker import PerformanceTracker
from fxEngine.strategy.registration import StrategyRegistration
from fxEngine.data.mb_data_retriever import DataRetriever
from simulation_manager import SimulationManager
from fxEngine.clock.clock import FactoryClock
from fxEngine.data.data_api import DataAPI


# from fxEngine.tests.data_demo_loader import DemoLoader

class TradingSimulator(object):
    '''
    TradingSimulator is the main class that defines, creates and
    customize the context for a strategy to be run

    Parameters:
    ==========

    str_strategy: The literal string of code (strategy) to be compiled and run
    symbols: List of FX assets that will be part of the strategy
    id_strategy: External ID assigned for this strategy
    '''

    def __init__(self, dto_strategy):
        self.traded_pairs = dto_strategy.traded_pairs
        self._validate_pairs()
        self._validate_initial_capital(dto_strategy.capital_base)
        self.api_strategy = ApiStrategy(
            StrategyCompiler(dto_strategy), dto_strategy)
        self._load_strategy()

    def _validate_pairs(self):
        # FIXME: Cant be repeated pairs
        # forb_fx_pairs = [
        #     x for x in self.traded_pairs if not Pair.is_allowed(x)]
        # if forb_fx_pairs:
        #     raise TradingSymbolForbidden(forb_fx_pairs)
        pass

    def _load_strategy(self):
        try:
            self.api_strategy.compile_strategy()
        except:
            raise

    def _validate_initial_capital(self, capital_base):
        if capital_base <= 0:
            raise InvalidCapitalBase()

    def run_simulation(self, clock_type):
        self.__register_strategy()
        data_portal = self._prepare_data_portal()
        clock = FactoryClock.get_clock(clock_type, data_portal)
        self.api_strategy.set_internal_variables(clock)
        '''
        intialize variables with params and check ig already instatiated objects
        has reference inside the compiled code
        '''
        data_api = DataAPI(data_portal=data_portal,
                           traded_pairs=self.traded_pairs)
        self.api_strategy.data_api = data_api

        scheduler = self.api_strategy.get_scheduler()
        simulation_manager = SimulationManager(
            clock, self.api_strategy, scheduler)
        simulation_manager.simulate()

    def _prepare_data_portal(self):
        perf_tracker = PerformanceTracker(strategy=self.api_strategy)
        _id = self.api_strategy.dto_strategy.id
        data_portal = DataPortal(
            ingester=DataRetriever(_id), pairs=self.traded_pairs)
        # data_portal = DataPortal(
            # ingester=DemoLoader(), pairs=self.traded_pairs)

        data_portal.register_observer(perf_tracker)
        data_portal.ingest()
        return data_portal

    def __register_strategy(self):
        st_reg = StrategyRegistration(self.api_strategy.dto_strategy)
        st_reg.publish_strategy()
