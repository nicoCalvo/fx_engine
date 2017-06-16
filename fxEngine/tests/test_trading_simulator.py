import unittest
import mock
from fxEngine.trading_simulator import TradingSimulator
from fxEngine.utils.exceptions import TradingSymbolForbidden
from fxEngine.strategy.exceptions import CompileMethodException
from fxEngine.tests.helper import (
    INVALID_STRATEGY,
    VALID_STRATEGY,
    STRATEGY_VALID_PAIR,
    STRATEGY_INVALID_PAIR
)


def mock_valid_capital(capital):
    pass


def mock_api_strategy(obj, other):
    pass


class TestTradingSimulator(unittest.TestCase):

    def setUp(self):
        pass

    @mock.patch('fxEngine.trading_simulator.TradingSimulator._validate_initial_capital',
                side_effect=mock_valid_capital)
    @mock.patch('fxEngine.trading_simulator.ApiStrategy.__init__',
                side_effect=mock_api_strategy)
    @mock.patch('fxEngine.trading_simulator.TradingSimulator._load_strategy')
    def test_invalid_pairs(self, mock_load_strategy, mock_capital_validator, mock_api_strategy):
        mock_load_strategy.return_value = None
        self.assertRaises(TradingSymbolForbidden,
                          TradingSimulator, STRATEGY_INVALID_PAIR)

    @mock.patch('fxEngine.trading_simulator.TradingSimulator._validate_initial_capital',
                side_effect=mock_valid_capital)
    @mock.patch('fxEngine.trading_simulator.ApiStrategy.__init__',
                side_effect=mock_api_strategy)
    @mock.patch('fxEngine.trading_simulator.TradingSimulator._load_strategy')
    def test_valid_pairs(self, mock_load_strategy, mock_capital_validator, mock_api_strategy):
        mock_load_strategy.return_value = None
        try:
            TradingSimulator(STRATEGY_VALID_PAIR)
        except Exception, e:
            self.fail("Encountered an unexpected exception: " + str(e))

    def test_compile_invalid_strategy(self):
        self.assertRaises(CompileMethodException,
                          TradingSimulator, INVALID_STRATEGY)

    def test_compile_valid_strategy(self):
        try:
            TradingSimulator(VALID_STRATEGY)
        except Exception, e:
            self.fail("Encountered an unexpected exception: " + str(e))
