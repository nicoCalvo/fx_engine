import unittest
from fxEngine.tests.data_demo_loader import DemoLoader
from fxEngine.clock.clock import EternalClock
from mock import Mock
import datetime


class TestEternalClock(unittest.TestCase):

    def setUp(self):
        self.eternal_clock = EternalClock(MockDataPortal())

    def test_is_new_day(self):
        self.assertTrue(self.eternal_clock.has_new_tick())
        self.assertTrue(self.eternal_clock.is_new_day())

    def test_is_new_month(self):
        self.assertTrue(self.eternal_clock.has_new_tick())
        self.assertTrue(self.eternal_clock.is_new_month())

    def test_is_new_week(self):
        self.eternal_clock.has_new_tick()
        self.assertTrue(self.eternal_clock.has_new_tick())
        self.eternal_clock.new_date = self.eternal_clock.new_date + \
            datetime.timedelta(days=3)
        self.assertTrue(self.eternal_clock.is_new_week())


class MockDataPortal(Mock):

    tick = ''
    dl = DemoLoader()

    def has_new_tick(self):
        self.tick = self.dl.current_tick()
        return True

    def get_current_tick(self):
        return self.tick[1:]

    def get_tick_date(self):
        return self.tick[0]
