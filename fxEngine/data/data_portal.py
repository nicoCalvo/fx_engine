import json
from datetime import datetime
import pandas as pd


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


class DataPortal(Observable):

    def __init__(self, ingester=None, pairs=None):
        super(DataPortal, self).__init__()
        self._pairs_names = pairs
        self.ingester = ingester
        self.data_bundle = ''
        self.current_tick = ''

    def ingest(self):
        self.data_bundle = self.ingester.ingest()

    def get_pairs_names_list(self):
        return self.data_bundle.cols.names[1:]

    def get_slice(self, pairs, ticks):
        ind = self.data_bundle.major_axis[0:ticks]
        pairs = pairs if isinstance(pairs, list) else [pairs]
        return self.data_bundle[pairs].ix[:,ind,:]

    def single_pair(self, pair, ticks):
        return self.data_bundle[pair].ix[0:int(ticks)]


    def _add_new_history_bar(self, bar):
        '''
        put the tick into data_bundle and check size
        applying LIFO to the queue

        '''
        date = bar[0]['time']
        pairs = [x['symbol'] for x in bar]
        dates = [x for x in self.data_bundle.major_axis]
        dates.insert(0,date)
        del dates[-1]
        self.data_bundle = self.data_bundle.reindex(major_axis=dates)

        pairs_data = {}
        for pair in pairs:
            pairs_data[pair] = []
        date = bar[0]['time']
        for pair_bar in bar:
            self.data_bundle[pair_bar['symbol']].ix[date]['open_bid']  = pair_bar['open_bid']
            self.data_bundle[pair_bar['symbol']].ix[date]['open_ask']  = pair_bar['open_ask']
            self.data_bundle[pair_bar['symbol']].ix[date]['low_bid']   = pair_bar['low_bid']
            self.data_bundle[pair_bar['symbol']].ix[date]['low_ask']   = pair_bar['low_ask']
            self.data_bundle[pair_bar['symbol']].ix[date]['high_bid']  = pair_bar['high_bid']
            self.data_bundle[pair_bar['symbol']].ix[date]['high_ask']  = pair_bar['high_ask']
            self.data_bundle[pair_bar['symbol']].ix[date]['close_bid'] = pair_bar['close_bid']
            self.data_bundle[pair_bar['symbol']].ix[date]['close_ask'] = pair_bar['close_ask']

        

    def has_new_tick(self):
        self.get_current_tick()
        if self.current_tick:
            self.notify_observers()
            return True
        return False

    def get_first_tick(self):
        data = json.loads(self.ingester.current_tick())
        self.current_tick = data['ticker']
        if data['bar']:
            self._add_new_history_bar(data['bar'])
            


    def get_current_tick(self):
        data = json.loads(self.ingester.current_tick())
        self.current_tick = data['ticker']
        if data['bar']:
            self._add_new_history_bar(data['bar'])
        return self.current_tick  # Jumps timestamp

    def get_tick_date(self):
        return datetime.strptime(self.current_tick[0]['time'], '%Y/%m/%d %H:%M:%S')
