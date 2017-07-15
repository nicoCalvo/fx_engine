import unittest
from fxEngine.clock.clock import EternalClock
from mock import Mock
from datetime import (
    datetime,
    timedelta)

class TestEternalClock(unittest.TestCase):

    def setUp(self):
        self.eternal_clock = EternalClock(MockDataPortal())

    def test_is_new_day(self):
        self.eternal_clock.get_first_tick()
        self.assertTrue(self.eternal_clock.has_new_tick())
        self.eternal_clock.has_new_tick()
        self.assertTrue(not self.eternal_clock.is_new_day())

    def test_is_new_month(self):
        self.assertTrue(self.eternal_clock.has_new_tick())
        self.assertTrue(self.eternal_clock.is_new_month())

    def test_is_new_week(self):
        self.eternal_clock.has_new_tick()
        self.assertTrue(self.eternal_clock.has_new_tick())
        self.eternal_clock.new_date = self.eternal_clock.new_date + \
            timedelta(days=3)
        self.assertTrue(self.eternal_clock.is_new_week())




class MockDataPortal(Mock):

    current_tick = [{"ask": 7.44185, "bid": 7.44135, "medium": 7.4416,
                "           symbol": "EURDKK", "time": "2010/01/04 00:00:00"}, 
                           {"ask": 1.44146, "bid": 1.44126, "medium": 1.44136,
                           "symbol": "USDEUR", "time": "2010/01/04 00:00:00"}]

    def has_new_tick(self):
        return True

    def get_current_tick(self):
        current_date = datetime.strptime(self.current_tick[0]['time'],
                                         '%Y/%m/%d %H:%M:%S')
        current_date = current_date + timedelta(days=1)
        self.current_tick[0]['time'] = datetime.strftime(current_date,
                                                    '%Y/%m/%d %H:%M:%S')
        return self.tick

    def get_tick_date(self):
        return datetime.strptime(self.current_tick[0]['time'],
                                 '%Y/%m/%d %H:%M:%S')

