

class SimulationManager(object):

    def __init__(self, clock, strategy, scheduler):
        self.clock = clock
        self.strategy = strategy
        self.scheduler = scheduler

    def simulate(self):
        while self.clock.has_new_tick():
            self._run_scheduled_functions()

    def run_scheduled_functions(self):
        if self.clock.is_new_day():
            self.scheduler.before_new_day()
        if self.clock.is_new_week():
            self.scheduler.before_new_week()
        if self.clock.is_new_month():
            self.scheduler.before_new_month()
