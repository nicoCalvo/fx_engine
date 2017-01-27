

class ApiMethod(object):
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
    def __init__(self, str_strategy, compiler):
        self.methods = dict(combine_helper='',
                            combine_positions='', aggregate_positions='')
        self.str_strategy = str_strategy
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
        except:
            raise
        
    def run_method(self, method, params):
        method = self.strategy[method]
        method(params)
