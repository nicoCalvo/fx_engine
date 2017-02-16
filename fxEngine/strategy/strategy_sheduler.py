

class StrategyScheduler(object):

    def __init__(self, strategy):
        self.strategy = strategy
        self.before_new_day = self.strategy.get('before_new_day', '')
        self.on_new_week = self.strategy.get('on_new_week', '')
        self.on_new_month = self.strategy.get('on_new_month', '')
