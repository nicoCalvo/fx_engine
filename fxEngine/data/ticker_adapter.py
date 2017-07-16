import pandas as pd


class TickerAdapter(object):
    UNSET_VALUE = -1

    def __init__(self):
        self.ticker = None
        self.pairs = None
        self.values = None

    # TODO convert numbers to decimal or something to avoid losing data
    def get_ticker(self, ticker, pairs, values=None):
        # pairs must be list instance!
        self.ticker = ticker
        self.pairs = pairs
        self.values = values
        '''
        This method follows zipline's guidelines described in its "current" implementation
        only that instead of wildcard returns, every different parse return is splitted in
        its own method  
        http://www.zipline.io/appendix.html?highlight=current#zipline.protocol.BarData.current
        '''
        if len(self.pairs) == 1:
            return self._parse_single_pair()
        return self._parse_many_pairs()

    def _parse_single_pair(self):

        '''
        first we need to clean out all UNSET_VALUES in the ticker so
        we can determine if its a single or multiple value ticker
        '''
        # self.ticker = self.ticker[0]
        # for val in self.values:
        #     ticker[self.pairs[0]].pop
        # self.ticker = [x for x in self.ticker if x > self.UNSET_VALUE]

        if len(self.values) > 1 :
            return self._single_pair_many_values()
        return self._single_pair_single_value()

    def _parse_many_pairs(self):

        if len(self.values) > 1:
            return self._many_pairs_many_values()
        return self._many_pairs_single_value()

    def _single_pair_single_value(self):
        '''
        Parses the single value located in the ticker filtering unset values

        Parameter
        --------
        ticker: single element list with BAMA (Bid, Ask, Mid, Amount)

        Returns
        -------
        value : float or int
             The return type is based
            on the ``value`` requested. If the field is one of 'Bid', 'Ask',
            or 'Mid', the value will be a float. 
        '''
        # TODO: Check if this poor workaround fits and if amount is always int
        # IMPLICIT CASTING SEEMS TO SOLVE ANY CAST ISSUE. BUT IT CAN FAIL
        return [x for x in self.ticker if x['symbol'] == self.pairs[0]][0][self.values[0]]

    def _single_pair_many_values(self):
        '''
         pandas Series is returned whose indices are the fields,
         and whose values are scalar values for this asset for each field
        '''
        ticker = []
        pair =[x for x in self.ticker if x['symbol'] == self.pairs[0]][0]
        for val in self.values:
            ticker.append(pair[val])
        return pd.Series(ticker, index=self.values)

    def _many_pairs_many_values(self):
        '''
        pandas DataFrame is returned, indexed by asset.
        The columns are the requested fields,
        filled with the scalar values for each asset for each field
        '''

        _ticker_list = []
        for pair in self.pairs:
            tick = []
            pair_values = [x for x in self.ticker if x['symbol'] == pair][0]
            for val in self.values:
                tick.append(pair_values[val])
            _ticker_list.append(tick)

        return pd.DataFrame(_ticker_list, index=self.pairs, columns=self.values)



    def _many_pairs_single_value(self):
        '''
        Pandas Series is returned whose indices are the pairs,
        and whose values are scalar values for each asset for the given field.
        '''
        values = []
        for pair in self.pairs:
            pair_values = [x for x in self.ticker if x['symbol'] == pair][0]
            values.append(pair_values[self.values[0]])
        return pd.Series(values, index=self.pairs)
