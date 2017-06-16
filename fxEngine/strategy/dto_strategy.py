import pandas as pd


class DTOStrategy(object):

    def __init__(self, **kwargs):
        '''
        Provides an single interface for strategy Data Transfer Object
        '''
        self.capital_base = int(kwargs['capital_base'])
        self.id = kwargs['id']
        self.start_date = pd.Timestamp(kwargs['start_date'])
        self.end_date = pd.Timestamp(kwargs['end_date'])
        self.frequency = kwargs['frequency']
        self.traded_pairs = kwargs['list_symbols']
        self.str_strategy = kwargs['script']
        self.simulation_mode = kwargs['simulation_mode']
        self.broker = kwargs['broker']
        self.data_feed = kwargs['data_feed']

    def to_json(self):
        return '{"id":"' + self.id + '",' + \
            '"capital_base": "' + str(self.capital_base) + '",' + \
            '"pairs": "' + str(self.traded_pairs) + '",' + \
            '"end_date": "' + self.end_date.strftime("%d/%m/%Y") + '",' + \
            '"start_date": "' + self.start_date.strftime("%d/%m/%Y") + '",' + \
            '"data_feed": "' + self.data_feed + '",' + \
            '"broker": "' + self.broker + '",' + \
            '"environment": "' + self.simulation_mode + '"}'
