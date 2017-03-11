import datetime


class Date(object):
    CLOCK = ''
    ALGO = ''

    def __init__(self):
        pass

    def get_date(self):
        return self.CLOCK.new_date.strftime('%Y-%m-%d %H:%M:%S')

    def add_days(self, days):
        return self.CLOCK.new_date - datetime.timedelta(days=days)
