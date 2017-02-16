from fxEngine.strategy.exceptions import CompileMethodException
import unittest
from fxEngine.strategy.api_strategy import ApiStrategy
from fxEngine.strategy.strategy_compiler import StrategyCompiler
from fxEngine.tests.helper import VALID_STRATEGY, INVALID_STRATEGY


class TestApiStrategy(unittest.TestCase):

    def setUp(self):
        pass

    # @mock.patch('strategy.api_compiler.StrategyCompiler')
    def test_valid_strategy(self):
        # mock_compiler.return_value=None
        api_strategy = ApiStrategy(
            compiler=StrategyCompiler(
                str_strategy=VALID_STRATEGY.str_strategy),
            dto_strategy=VALID_STRATEGY)
        try:
            api_strategy.compile_strategy()
        except Exception, e:
            self.fail(str(e))
        #(CompileMethodException, api_strategy.compile_strategy)
        # api_strategy.

    def test_invalid_strategy(self):
        api_strategy = ApiStrategy(
            compiler=StrategyCompiler(
                str_strategy=INVALID_STRATEGY.str_strategy),
            dto_strategy=INVALID_STRATEGY)
        self.assertRaises(CompileMethodException,
                          api_strategy.compile_strategy)
