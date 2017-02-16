

class EternalClock(object):
    WEEKEND_DAYS = 2

    def __init__(self, data_portal):
        self.last_day = 0
        self.last_month = 0
        self.last_week = 0
        self.new_date = ''
        self.last_date = ''
        self.data_portal = data_portal

    def has_new_tick(self):
        has_tick = False
        if self.data_portal.has_new_tick():
            self.last_date = self.new_date
            self.new_date = self.data_portal.get_current_tick()[0]
            has_tick = True
        return has_tick

    def is_new_day(self):
        is_new = False
        if self.last_day != self.new_date.day:
            self.last_day = self.new_date.day
            is_new = True
        return is_new

    def is_new_month(self):
        is_new = False
        if self.last_month != self.new_date.month:
            self.last_month = self.new_date.month
            is_new = True
        return is_new

    def is_new_week(self):
        delta = self.new_date - self.last_date
        return delta.days > self.WEEKEND_DAYS


class LimitedClock(EternalClock):

    def __init__(self, data_portal):
        super(LimitedClock, self).__init__(data_portal)
        self.__ticks = 0
        self.__limit_ticks = 10000

    def has_new_tick(self):
        if self.__ticks == self.__limit_ticks:
            return False
        self.__ticks += 1
        return self.data_portal.has_new_tick()
