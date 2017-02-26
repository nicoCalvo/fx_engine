from .exceptions import InvalidPairError, InvalidPairValueError


class TickerFilter(object):
    UNSET_VALUE = -1

    def __init__(self, traded_pairs):
        '''
        Filters the raw ticket as it comes from dataportal and parses it
        into a lists of lists with index position as indicative of pair
        and for values

        The TickerFilter cares of a new ticket
        consists in filtering the ticket according
        the values/pairs requested

        '''
        self._tick = ''
        self.filtered_values = ''
        self.filtered_pairs = ''
        self.traded_pairs = traded_pairs
        self._allowed_values = ['Bid', 'Ask', 'Mid', 'Amount']

    def _filter_pairs(self):
        self._validate_filter_pairs()
        pos = [x for x in range(len(self.traded_pairs))]
        if self.filtered_pairs[0]:
            pos = [self.traded_pairs.index(x) for x in self.filtered_pairs]

        self._tick = map(self._tick.__getitem__, pos)

    def _validate_filter_pairs(self):
        if self.filtered_pairs[0] and not \
                set(self.filtered_pairs).issubset(set(self.traded_pairs)):
            raise InvalidPairError(str(self.filtered_pairs))

    def _filter_values(self):
        self._validate_filter_values()
        tick = []
        pos_value = [x for x in range(len(self._allowed_values))]
        if self.filtered_values[0]:
            pos_value = [self._allowed_values.index(
                x) for x in self.filtered_values]
        for x in self._tick:
            tick_quote = x['tick']['Quote']
            parsed_tick = self._parse_tick(tick_quote, pos_value)
            tick.append(parsed_tick)

        self._tick = tick

    def _validate_filter_values(self):
        if self.filtered_values[0] and not \
                set(self.filtered_values).issubset(set(self._allowed_values)):
            raise InvalidPairValueError(str(self.filtered_values))

    def _parse_tick(self, tick, pos_value):
        pair_values = [self.UNSET_VALUE for x in self._allowed_values]
        for pos in pos_value:
            pair_values[pos] = tick[self._allowed_values[pos]]
        return pair_values

    def filter(self, tick, pairs, values):
        
        self.filtered_values = [x.title() for x in values]
        self.filtered_pairs = pairs
        self._tick = tick
        if self.filtered_pairs:
            self._filter_pairs()
        if self.filtered_values:
            self._filter_values()
        return self._tick
