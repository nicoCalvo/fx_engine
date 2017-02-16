from fxEngine.data.data_portal import DataPortal
from fxEngine.tests.data_demo_loader import DemoLoader, DEMO_PAIRS
import unittest
from mock import Mock
import datetime



class TestDataPortal(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_ingest(self):
        dp = DataPortal(ingester=DemoLoader(), pairs_names_list=DEMO_PAIRS)
        dp.ingest()
        tick = dp.get_current_tick()
        self.assertEquals(len(tick), len(DEMO_PAIRS))
        self.assertIs(tick[0].__class__, datetime.datetime)

    def test_notify(self):
        mock_observer = MockObserver()
        dp = DataPortal(ingester=DemoLoader(), pairs_names_list=[])
        dp.register_observer(mock_observer)
        dp.notify_observers()
        self.assertEquals(mock_observer.base_value, mock_observer.new_value)

    def test_valid_pair_names(self):
        dp = DataPortal(ingester=DemoLoader(), pairs_names_list=DEMO_PAIRS)
        dp.ingest()
        self.assertEquals(DEMO_PAIRS, dp.get_pairs_names_list())


class MockObserver(Mock):
    base_value = 0
    new_value = 4

    def update(self):
        self.base_value = self.new_value

