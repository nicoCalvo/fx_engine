

class Dates(object):

    def __init__(self, dates):
        self.dates = dates
        

    def write_dates(self):
        f = open('dates.log', 'w')
        f.write(str(self.dates))
        f.close()
