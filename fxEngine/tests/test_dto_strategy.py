import unittest
from fxEngine.strategy.dto_strategy import DTOStrategy


class TestDTOStrategy(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_json_strategy(self):
        str_strategy = {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": "AAPL", "start_date": "2015-10-03",
                        "script": "\n\n\ndef initialize(context):\n   context.i = 0 \n\n\ndef handle_data(context, data):\n    print data\n    print data.__dict__\n    order(symbol(\'AAPL\'), 10)\n      record(AAPL=data.current(symbol(\'AAPL\'), \'price\'))\n"}
        a = DTOStrategy(**str_strategy)
        self.assertTrue(a.id, str_strategy['id'])
        self.assertTrue(a.traded_pairs, str_strategy['pairs_list'])

    def test_invalid_json_strategy(self):
        invalid_str_strategy = 'NOT A JSON'
        self.assertRaises(TypeError, DTOStrategy,
                          invalid_str_strategy)
