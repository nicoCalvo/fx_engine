from utils.exceptions import CompileMethodException
import unittest
from strategy.api_compiler import StrategyCompiler


class TestStrategyCompiler(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_strategy(self):
        valid_st = 'def valid():\n   return 1'
        api_compiler = StrategyCompiler(str_strategy=valid_st)
        nsp = api_compiler.compile()
        self.assertEquals(nsp['valid'](), 1)

    def test_invalid_strategy(self):
        invalid_st = 'definvalid(): \n asdas'
        api_compiler = StrategyCompiler(str_strategy=invalid_st)
        self.assertRaises(CompileMethodException, api_compiler.compile)
        