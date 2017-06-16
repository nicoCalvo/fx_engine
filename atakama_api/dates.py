import datetime


class Date(object):

    def __init__(self):
        self.clock = ''

    def get_date(self):
        return self.clock.new_date.strftime('%Y-%m-%d %H:%M:%S')

    def add_days(self, days):
        return self.clock.new_date - datetime.timedelta(days=days)
