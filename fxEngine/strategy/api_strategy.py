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
        self.context = StrategyContext()
        self._scheduler = None
        self.data_api = None
        self._handle_data = None
        self._initialize = None
        self._before_new_day = None
        self._before_new_week = None
        self._before_new_month = None


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

        self.strategy['order']._publish_orders()

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

    def set_internal_variables(self, clock, data_portal):
        self.strategy['date'].clock = clock
        self.strategy['log'].clock = clock
        self.strategy['order']._logger = self.strategy['log']
        self.strategy['order']._context = self.context
        self.strategy['order']._strategy = self.dto_strategy
        self.strategy['order']._order_adapter.data_portal= data_portal

    def get_order_manager(self):
        return self.strategy['order']