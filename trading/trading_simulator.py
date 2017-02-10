from data.symbols import Symbol
# from strategy.strategy import Strategy
from strategy.api_compiler import StrategyCompiler
from strategy.api_method import ApiStrategy
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

    def __init__(self, str_strategy, symbols, id_strategy, capital_base):
        self.namespace = {}

        self.api_method = ApiStrategy(str_strategy, StrategyCompiler(str_strategy))
        self.strategy = self._load_strategy(str_strategy)
        forb_symbols = self._validate_symbols(symbols)
        if forb_symbols:
            raise TradingSymbolForbidden(forb_symbols)
        self.symbols = [Symbol(x) for x in symbols]
        self.trading_environment = TradingEnvironment()
        self.capital_base = self._validate_initial_capital(capital_base)

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
        sim_params = self.create_simulation_parameters
        '''
        crear el Blotter con el VolumeShareSlippage

        '''
        # If an env has been provided, pop it
    

    def create_simulation_parameters(year=2006, start=None, end=None,
                                     capital_base=float("1.0e5"),
                                     num_days=None,
                                     data_frequency='daily',
                                     emission_rate='daily',
                                     trading_calendar=None):

        if not trading_calendar:
            trading_calendar = get_calendar("NYSE")

        if start is None:
            start = pd.Timestamp("{0}-01-01".format(year), tz='UTC')
        elif type(start) == datetime:
            start = pd.Timestamp(start)

        if end is None:
            if num_days:
                start_index = trading_calendar.all_sessions.searchsorted(start)
                end = trading_calendar.all_sessions[start_index + num_days - 1]
            else:
                end = pd.Timestamp("{0}-12-31".format(year), tz='UTC')
        elif type(end) == datetime:
            end = pd.Timestamp(end)

        sim_params = SimulationParameters(
            start_session=start,
            end_session=end,
            capital_base=capital_base,
            data_frequency=data_frequency,
            emission_rate=emission_rate,
            trading_calendar=trading_calendar,
        )

        return sim_params
           










































   
