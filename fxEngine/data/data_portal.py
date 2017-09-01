import json
from datetime import datetime
import pandas as pd
import logging

LOGGER = logging.getLogger(__name__)


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

    def notify_observers(self, data):
        [x.update(data) for x in self.observers]


class DataPortal(Observable):
    BAR_COLUMNS = ['open_bid', 'open_ask', 'low_bid',
                   'low_ask', 'high_bid', 'high_ask',
                   'close_bid', 'close_ask']

    def __init__(self, ingester=None, pairs=None):
        super(DataPortal, self).__init__()
        self._pairs_names = pairs
        self.ingester = ingester
        self.data_bundle = ''
        self.current_tick = ''

    def ingest(self):
        raw_bundle = self.ingester.ingest()
        pairs_data = {}
        for pair in self._pairs_names:
            pairs_data[pair] = []
        dates = []

        for bar in raw_bundle:
            dates.append(bar[0]['time'])
            for pair_bar in bar:
                if pair_bar['symbol'] in self._pairs_names:
                    data = [pair_bar['open_bid'], pair_bar['open_ask'],
                            pair_bar['low_bid'], pair_bar['low_ask'],
                            pair_bar['high_bid'], pair_bar['high_ask'],
                            pair_bar['close_bid'], pair_bar['close_ask']]
                    pairs_data[pair_bar['symbol']].append(data)
        pn = pd.Panel(major_axis=dates, minor_axis=self.BAR_COLUMNS)
        for symbol, data_frame in pairs_data.iteritems():
            pn[symbol] = pd.DataFrame(data_frame, index=dates,
                                      columns=self.BAR_COLUMNS)
        self.data_bundle = pn

    def get_pairs_names_list(self):
        return self.data_bundle.cols.names[1:]

    def get_slice(self, pairs, ticks):
        ind = self.data_bundle.major_axis[0:ticks]
        pairs = pairs if isinstance(pairs, list) else [pairs]
        return self.data_bundle[pairs].ix[:, ind, :]

    def single_pair(self, pair, ticks):
        return self.data_bundle[pair].ix[0:int(ticks)]

    def _add_new_history_bar(self, bar):
        date = bar[0]['time']
        dates = [x for x in self.data_bundle.major_axis]
        dates.insert(0, date)
        del dates[-1]
        self.data_bundle = self.data_bundle.reindex(major_axis=dates)
        date = bar[0]['time']
        for pair_bar in bar:
            if pair_bar['symbol'] in self._pairs_names:
                self.data_bundle[pair_bar['symbol']].set_value(
                    date, 'open_bid', pair_bar['open_bid'])
                self.data_bundle[pair_bar['symbol']].set_value(
                    date, 'open_ask', pair_bar['open_ask'])
                self.data_bundle[pair_bar['symbol']].set_value(
                    date, 'low_bid', pair_bar['low_bid'])
                self.data_bundle[pair_bar['symbol']].set_value(
                    date, 'low_ask', pair_bar['low_ask'])
                self.data_bundle[pair_bar['symbol']].set_value(
                    date, 'high_bid', pair_bar['high_bid'])
                self.data_bundle[pair_bar['symbol']].set_value(
                    date, 'high_ask', pair_bar['high_ask'])
                self.data_bundle[pair_bar['symbol']].set_value(
                    date, 'close_bid', pair_bar['close_bid'])
                self.data_bundle[pair_bar['symbol']].set_value(
                    date, 'close_ask', pair_bar['close_ask'])

    def has_new_tick(self):
        self.get_current_tick()
        if self.current_tick:
            # self.notify_observers()
            return True
        return False

    def get_current_tick(self):
        data = self.ingester.current_tick()
        if not isinstance(data, dict):
            data = json.loads(data)
        ticker_bar = data.pop('tick')
        self.current_tick = ticker_bar['ticker']
        self.notify_observers(data)
        if 'bar' in ticker_bar:
            self._add_new_history_bar(ticker_bar['bar'])
        return self.current_tick

    def get_tick_date(self):
        return datetime.strptime(self.current_tick[0]['time'], '%Y/%m/%d %H:%M:%S')
