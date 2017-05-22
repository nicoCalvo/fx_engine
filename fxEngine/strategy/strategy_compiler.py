from six import exec_
from .exceptions import CompileMethodException
from fxEngine.strategy.strategy_template import TemplateStrategy
from atakama_api.utils import MbConnector


class StrategyCompiler(object):

    def __init__(self, dto_strategy, namespace={}):
        self.dto_strategy = dto_strategy
        self.str_strategy = dto_strategy.str_strategy
        self.namespace = namespace

    def compile(self):
        template = TemplateStrategy(
            self.str_strategy, 'local', self.dto_strategy.id)
        strategy = template.build_strategy()
        try:
            compiled_str = compile(strategy, '<string>', 'exec')
            exec_(compiled_str, self.namespace)
        except Exception, e:
            conn = MbConnector.get_connection()
            channel = conn.channel()
            channel.basic_publish(exchange='E_standard_log',
                                  routing_key=self.dto_strategy.id,
                                  body=str(e) + '---- ' + strategy)
            conn.close()
            raise CompileMethodException(str(e))
        return self.namespace


