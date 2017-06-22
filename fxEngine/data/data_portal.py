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
        # TODO: validate requested pair in self._pairs_names
        if len(pairs) == 1:
            return self.single_pair(pairs[0], ticks)
            pass
        return self.data_bundle[pairs][-ticks:]

    def single_pair(self, pair, ticks):
        raw_data = self.data_bundle[pair][-ticks:]
        data = [x for x in raw_data]
        return pd.DataFrame(data=data, columns=['open_bid', 'open_ask', 'low_bid', 'low_ask', 'high_bid', 'high_ask', 'close_bid', 'close_ask'])

    def _add_new_history_bar(self, bar):
        '''
        put the tick into data_bundle and check size
        applying LIFO to the queue

        '''
        self.data_bundle = self.data_bundle.drop([self.data_bundle.ix[-1].name])
        pairs = [x['symbol'] for x in bar]

        pairs_data = {}
        for pair in pairs:
            pairs_data[pair] = []

        for pair_bar in bar:
            data = [pair_bar['open_bid'], pair_bar['open_ask'],
                    pair_bar['low_bid'], pair_bar['low_ask'],
                    pair_bar['high_bid'], pair_bar['high_ask'],
                    pair_bar['close_bid'], pair_bar['close_ask']]
            pairs_data[pair_bar['symbol']].append(data)

        dict_to_frame = {}
        for key, pair in pairs_data.iteritems():
            dict_to_frame[key] = pd.Series(pair, index=[bar[0]['time']])

        new_frame = pd.DataFrame(dict_to_frame)
        frames = [ new_frame, self.data_bundle]
        self.data_bundle = pd.concat(frames)

    def has_new_tick(self):
        self.get_current_tick()
        if self.current_tick:
            self.notify_observers()
            return True
        return False

    def get_current_tick(self):
        data = json.loads(self.ingester.current_tick())
        self.current_tick = data['ticker']
        if data['bar']:
            self._add_new_history_bar(data['bar'])
        return self.current_tick  # Jumps timestamp

    def get_tick_date(self):
        return datetime.strptime(self.current_tick[0]['time'], '%Y/%m/%d %H:%M:%S')
