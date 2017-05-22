from .strategy_context import StrategyContext
from .strategy_sheduler import StrategyScheduler
from ..data.dto import Portfolio

'''
Definir API de datos "data"
Definir API funciones matematicas Inverse price etc
Definir API portfolio

'''


class ApiStrategy(object):
    '''
        Access point to methods, its supposed to exec and
        control execution of each injected method

        Parameters:
        ==========
        compiler: StrategyCompiler obj
        portfolio: Portfolio namedtuple obj with base starting

        Attributes:
        ==========
        strategy: compiled strategy methods
        compiler: Compiler obj
        context: StrategyContext obj. Receives a portfolio dto


    Context: Debe tener un portfolio -- ver que debe tener un portfolio
             Debe contener las variables de entorno

    '''

    def __init__(self, compiler, dto_strategy):
        self._compiler = compiler
        self.dto_strategy = dto_strategy
        self.strategy = ''
        self.context = StrategyContext(self._get_base_portfolio())
        self._scheduler = None
        self.data_api = None
        self._handle_data = None
        self._initialize = None
        self._before_new_day = None
        self._before_new_week = None
        self._before_new_month = None

    def _get_base_portfolio(self):
        return Portfolio(capital_used=0,
                         starting_cash=self.dto_strategy.capital_base,
                         portfolio_value=0, pnl=0, returns=0,
                         cash=0, positions=[],
                         start_date=self.dto_strategy.start_date,
                         positions_value=[])

    def compile_strategy(self):
        try:
            self.strategy = self._compiler.compile()
            self._handle_data = self.strategy['handle_data']
            self._initialize = self.strategy['initialize']
        except:
            raise

    def initialize(self):
        self._initialize(self.context)

    def handle_data(self):
        self._handle_data(self.context, self.data_api)

    def set_portfolio(self, portfolio):
        self.context.portfolio = portfolio

    def get_portfolio(self):
        return self.context.portfolio

    def get_scheduler(self):
        return StrategyScheduler(self)

    def on_new_day(self):
        self._before_new_day(self.context, self.data_api)

    def on_new_week(self):
        self._before_new_week(self.context, self.data_api)

    def on_new_month(self):
        self._before_new_month(self.context, self.data_api)

    def set_internal_variables(self, clock):
        clock_setter = self.strategy['set_clock']
        clock_setter(clock, self.dto_strategy.id)
