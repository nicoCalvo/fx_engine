from utils.exceptions import CompileMethodException
import unittest
from strategy.api_method import ApiMethod
from strategy.api_compiler import StrategyCompiler


class TestApiMethod(unittest.TestCase):

    def setUp(self):
        pass

    # @mock.patch('strategy.api_compiler.StrategyCompiler')
    def test_valid_strategy(self):
    	# mock_compiler.return_value=None

        valid_st = 'def valid()\n   return 1'
        api_method = ApiMethod(str_strategy=valid_st,
                               compiler=StrategyCompiler(str_strategy=valid_st))
        (CompileMethodException, api_method.compile_strategy)

    def test_invalid_strategy(self):
        invalid_st = 'def invalid() asdas'
        api_method = ApiMethod(str_strategy=invalid_st,
                               compiler=StrategyCompiler(str_strategy=invalid_st))
        self.assertRaises(CompileMethodException, api_method.compile_strategy)

    # @mock.patch('trading.trading_simulator.TradingSimulator._load_strategy')
    # def test_invalid_symbols(self, mock_loader):
    #     invalid_symbols = ['XXX/AAA']
    #     self.assertRaises(TradingSymbolForbidden, TradingSimulator,
    #                       str_strategy='', symbols=invalid_symbols,
    #                       id_strategy=3)

    # @mock.patch('trading.trading_simulator.TradingSimulator._validate_symbols')
    # def test_valid_strategy(self):
    #     strategy = 'def hola():\n    print 1'
    #     ts = TradingSimulator(
    #         str_strategy=strategy, symbols='', id_strategy=3)
    #     res = ts._load_strategy()

    # def test_invalid_strategy(self):
    #     strategy = ''
