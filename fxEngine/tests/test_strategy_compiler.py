from fxEngine.strategy.exceptions import CompileMethodException
import unittest
from fxEngine.strategy.strategy_compiler import StrategyCompiler
# from fxEngine.strategy.dto_strategy import DTOStrategy
from fxEngine.tests.helper import RandomStrategy
from fxEngine.tests.helper import (
    INVALID_STRATEGY,
    VALID_STRATEGY
    )

class TestStrategyCompiler(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_strategy(self):
        api_compiler = StrategyCompiler(dto_strategy=VALID_STRATEGY)
        nsp = api_compiler.compile()
        self.assertIsNotNone(nsp['OrderManager'])
        self.assertIsNotNone(nsp['handle_data'])
        self.assertIsNotNone(nsp['initialize'])

    def test_invalid_strategy(self):
        api_compiler = StrategyCompiler(dto_strategy=INVALID_STRATEGY)
        self.assertRaises(CompileMethodException, api_compiler.compile)
        