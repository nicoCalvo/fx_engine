import unittest
from fxEngine.strategy.dto_strategy import DTOStrategy
from fxEngine.tests.helper import (
    str_strategy_valid_pair,
    str_strategy_invalid_keys
    )


class TestDTOStrategy(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_json_strategy(self):
        DTOStrategy(**str_strategy_valid_pair)

    def test_invalid_json_strategy(self):
        self.assertRaises(KeyError, DTOStrategy,
                          **str_strategy_invalid_keys)
