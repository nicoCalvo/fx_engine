from six import exec_
from .exceptions import CompileMethodException


class StrategyCompiler(object):

    def __init__(self, str_strategy, namespace={}):
        self.str_strategy = str_strategy
        self.namespace = namespace

    def compile(self):
        import pdb
        pdb.set_trace()
        try:
            compiled_str = compile(self.str_strategy, '<string>', 'exec')
            exec_(compiled_str, self.namespace)
        except Exception, e:
            raise CompileMethodException(str(e))
        return self.namespace

    # def get_schedule_functions(self):
    #     sched = []
    #     strategy = []
    #     for line in self.str_strategy.splitlines():
    #         if self._is_scheduled(line):
    #             sched.append(line)
    #         else:
    #             strategy.append(line)
    #     self.str_strategy = ('\n').join(strategy)
    #     self.str_strategy +=  ('\n').join(sched)

    # def _compile_scheduled(self, sched):
    #     for sched_func in sched:
    #         try:
    #             compiled_str = compile(sched_func, '<string>', 'exec')
    #             exec_(compiled_str, self.namespace)
    #         except Exception, e:
    #             raise CompileMethodException(str(e))

    # def _is_scheduled(self, line):
    #     ret = False
    #     for sched_func in self.SCHED_FUNCTIONS:
    #         if line.find(sched_func) > -1:
    #             ret = True
    #     return ret
