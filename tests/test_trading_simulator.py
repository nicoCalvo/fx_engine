'''
to be run from 
'''
import unittest
import mock
from trading.trading_simulator import TradingSimulator
from utils.exceptions import TradingSymbolForbidden


class TestTradingSimulator(unittest.TestCase):

    def setUp(self):
        pass

    @mock.patch('trading.trading_simulator.TradingSimulator._load_strategy')
    def test_valid_symbols(self, mock_loader):
        valid_symbols = ['USD/EUR']
        ts = TradingSimulator(
            str_strategy='', symbols=valid_symbols, id_strategy=3)
        symbol_list = [x.name for x in ts.symbols]
        self.assertEquals(symbol_list, valid_symbols)

    @mock.patch('trading.trading_simulator.TradingSimulator._load_strategy')
    def test_invalid_symbols(self, mock_loader):
        invalid_symbols = ['XXX/AAA']
        self.assertRaises(TradingSymbolForbidden, TradingSimulator,
                          str_strategy='', symbols=invalid_symbols,
                          id_strategy=3)

    @mock.patch('trading.trading_simulator.TradingSimulator._validate_symbols')
    def test_valid_strategy(self, mock_validate_symbols):
        mock_validate_symbols.return_value = []
        strategy = 'def hola():\n    print 1'
        ts = TradingSimulator(
            str_strategy=strategy, symbols='', id_strategy=3)
        self.assertTrue(isinstance(ts,TradingSimulator))
        
    def test_invalid_strategy(self):
        strategy = ''
