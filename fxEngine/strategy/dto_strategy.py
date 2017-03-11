import pandas as pd


class DTOStrategy(object):

    def __init__(self, **kwargs):
        '''
        Provides an single interface for strategy Data Transfer Object
        '''
        self.capital_base = kwargs['capital_base']
        self.id = kwargs['id']
        self.start_date = pd.Timestamp(kwargs['start_date'])
        self.end_date = pd.Timestamp(kwargs['end_date'])
        self.frequency = kwargs['frequency']
        self.traded_pairs = kwargs['pairs_list']
        self.str_strategy = kwargs['script']
        self.simulation_mode = kwargs['mode']
