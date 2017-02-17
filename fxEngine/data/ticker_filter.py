from .exceptions import InvalidPairError, InvalidPairValueError


class TickerFilter(object):
    UNSET_VALUE = -1

    def __init__(self, tick, filtered_pairs, filtered_values, traded_pairs):
        self._tick = tick
        self.filtered_values = [x.title() for x in filtered_values]
        self.filtered_pairs = filtered_pairs
        self.traded_pairs = traded_pairs
        self._allowed_values = ['Bid', 'Ask', 'Mid', 'Amount']

    def _filter_pairs(self):
        self._validate_filter_pairs()
        pos = [self.traded_pairs.index(x) for x in self.filtered_pairs]
        self._tick = map(self._tick.__getitem__, pos)

    def _validate_filter_pairs(self):
        if not set(self.filtered_pairs).issubset(set(self.traded_pairs)):
            raise InvalidPairError(str(self.filtered_pairs))

    def _filter_values(self):

        self._validate_filter_values()
        tick = []
        pos_value = [self._allowed_values.index(
            x) for x in self.filtered_values]
        for x in self._tick:
            tick_quote = x['tick']['Quote']
            parsed_tick = self._parse_tick(tick_quote, pos_value)
            tick.append(parsed_tick)
        self._tick = tick

    def _validate_filter_values(self):
        if not set(self.filtered_values).issubset(set(self._allowed_values)):
            raise InvalidPairValueError(str(self.filtered_values))

    def _parse_tick(self, tick, pos_value):
        pair_values = [self.UNSET_VALUE for x in self._allowed_values]
        for pos in pos_value:
            pair_values[pos] = tick[self._allowed_values[pos]]
        return pair_values

    def filter(self):
        if self.filtered_pairs:
            self._filter_pairs()
        if self.filtered_values:
            self._filter_values()
        return self._tick
