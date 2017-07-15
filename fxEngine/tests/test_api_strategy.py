from fxEngine.strategy.exceptions import CompileMethodException
import unittest
from fxEngine.strategy.api_strategy import ApiStrategy
from fxEngine.strategy.strategy_compiler import StrategyCompiler
from fxEngine.tests.helper import VALID_STRATEGY, INVALID_STRATEGY


class TestApiStrategy(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_strategy(self):
        api_strategy = ApiStrategy(
            compiler=StrategyCompiler(
                dto_strategy=VALID_STRATEGY),
            dto_strategy=VALID_STRATEGY)
        try:
            api_strategy.compile_strategy()
        except Exception, e:
            self.fail(str(e))

    def test_invalid_strategy(self):
        api_strategy = ApiStrategy(
            compiler=StrategyCompiler(
                dto_strategy=INVALID_STRATEGY),
            dto_strategy=INVALID_STRATEGY)
        self.assertRaises(CompileMethodException,
                          api_strategy.compile_strategy)
