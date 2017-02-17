

class StrategyScheduler(object):

    def __init__(self, strategy):
        self.strategy = strategy
        self._has_new_day = strategy.get('before_new_day', '')
        self._has_new_week = strategy.get('before_new_week', '')
        self._has_new_month = strategy.get('before_new_month', '')

    def before_new_day(self):
    	import pdb
    	pdb.set_trace()
        if self._has_new_day:
            self.strategy.before_new_day()

    def before_new_week(self):
        if self._has_new_week:
            self.strategy.on_new_week()

    def before_new_month(self):
        if self._has_new_month:
            self.strategy.on_new_month()
