from data.pair import Pair

class ApiStrategy(object):
    '''
    Access point to methods, its supposed to exec and control execution of each injected method
    Well known methods should be loaded automatically and obliged methods must be implemented

    Others method can be added and compiled

    Parameters:
    ==========

    str_strategy: strategy to be compiled with all methods
    compiler: StrategyCompiler obj

    Attributes:
    ==========
    strategy: compiled strategy

    '''
    def __init__(self,  compiler):
        self.methods = dict(intialize='',
                            handle_date='')
        self.compiler = compiler
        self.strategy = ''

    def add_method(self, methodname, methodstring):
        '''
        '''
        pass

    def rm_method(self, methodname, methodstring):
        pass

    def compile_strategy(self):
        try:
            self.strategy = self.compiler.compile()
            self._handle_data = self.strategy['handle_data']
            self._initialize = self.strategy['initialize']
        except:
            raise
        
    def run_method(self, method, context, data):
        import pdb
        pdb.set_trace()
        method = self.strategy[method]
        return method(context, data)

    def initialize(self, context):
        self._initialize(context)

    def handle_data(self, data):
        import pdb
        pdb.set_trace()
        self._handle_data(self, 'asdadsasdasdasdas')

    def schedule_functions(self):
        pass

