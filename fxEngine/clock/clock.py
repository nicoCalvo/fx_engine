class Observable(object):
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def notify_observers(self):
        [x.update() for x in self.observers]


class EternalClock(Observable):
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
            self.new_date = self.data_portal.get_tick_date()
            has_tick = True
        return has_tick

    def get_first_tick(self):
        tick = self.data_portal.get_current_tick()
        self.new_date = self.data_portal.get_tick_date()
        self.last_day = self.new_date.day
        self.last_month = self.new_date.month
        return tick

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
        self.__tick_limits = 10000

    def has_new_tick(self):
        if self.__ticks == self.__tick_limits:
            return False
        self.__ticks += 1
        has_tick = False
        if self.data_portal.has_new_tick():
            self.last_date = self.new_date
            self.new_date = self.data_portal.get_tick_date()
            has_tick = True
        return has_tick


class FactoryClock(object):
    clocks = dict(eternal=EternalClock, limited=LimitedClock)

    @classmethod
    def get_clock(cls, type, data_portal):
        clock_instance = ''
        try:
            clock_instance = cls.clocks[type]
        except:
            clock_instance = cls.clocks['eternal']
        return clock_instance(data_portal)
