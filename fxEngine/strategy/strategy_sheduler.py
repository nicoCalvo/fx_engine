

class StrategyScheduler(object):

    def __init__(self, api_strategy):
        '''
        This class is responsible for parsing scheduled methods
        to be run in a specific moment.
        It has execution control based on current clock's date


        Attributes:
        ----------
        api_strategy:   APIStrategy obj
        _has_new_day :  Bool
        _has_new_week:  Bool
        _has_new_month: Bool

        '''
        self.api_strategy = api_strategy
        self._set_scheduled_functions()
        self._has_new_day = self.api_strategy._before_new_day != ''
        self._has_new_week = self.api_strategy._before_new_week != ''
        self._has_new_month = self.api_strategy._before_new_month != ''

    def _set_scheduled_functions(self):
        self.api_strategy._before_new_day = self.api_strategy.strategy.get(
            'on_new_day', '')
        self.api_strategy._before_new_week = self.api_strategy.strategy.get(
            'on_new_week', '')
        self.api_strategy._before_new_month = self.api_strategy.strategy.get(
            'on_new_month', '')

    def run_scheduled(self, clock):
        '''
        using current clock's date, checks if
        there's a scheduled function and run it
        '''
        if clock.is_new_day() and self._has_new_day:
            self.api_strategy.on_new_day()
        if clock.is_new_week() and self._has_new_week:
            self.api_strategy.on_new_week()
        if clock.is_new_month() and self._has_new_month:
            self.api_strategy.on_new_month()
