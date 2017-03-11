from six import exec_
from .exceptions import CompileMethodException
from fxEngine.strategy.strategy_template import TemplateStrategy


class StrategyCompiler(object):

    def __init__(self, dto_strategy, namespace={}):
        self.dto_strategy = dto_strategy
        self.str_strategy = dto_strategy.str_strategy
        self.namespace = namespace

    def compile(self):
        template = TemplateStrategy(self.str_strategy, 'local')
        strategy = template.build_strategy()
        try:
            compiled_str = compile(strategy, '<string>', 'exec')
            exec_(compiled_str, self.namespace)
        except Exception, e:
            raise CompileMethodException(str(e))
        return self.namespace
