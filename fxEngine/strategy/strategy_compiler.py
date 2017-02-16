from six import exec_
from .exceptions import CompileMethodException


class StrategyCompiler(object):

    def __init__(self, str_strategy, namespace={}):
        self.str_strategy = str_strategy
        self.namespace = namespace

    def compile(self):
        try:
            compiled_str = compile(self.str_strategy, '<string>', 'exec')
            exec_(compiled_str, self.namespace)
        except Exception, e:
            raise CompileMethodException(str(e))
        return self.namespace


