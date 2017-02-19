import pandas as pd


class TickerAdapter(object):
    UNSET_VALUE = -1

    def __init__(self, ticker, pairs, values):
        self.ticker = ticker
        self.pairs = pairs
        self.values = values

    # TODO convert numbers to decimal or something to avoid loosing data
    def get_ticker(self):
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
        self.ticker = self.ticker[0]
        self.ticker = [x for x in self.ticker if x > self.UNSET_VALUE]
        if len(self.values) > 1:
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
            or 'Mid', the value will be a float. If the
            ``value`` is 'amount' the ret value will be a int
        '''
        # TODO: Check if this poor workaround fits and if amount is always int
        # IMPLICIT CASTING SEEMS TO SOLVE ANY CAST ISSUE. BUT IT CAN FAIL
        value = self.ticker[0]
        # if value.index('.'):
        #     value = int(value)
        # else:
        #     value = float(value)
        return value

    def _single_pair_many_values(self):
        '''
         pandas Series is returned whose indices are the fields,
         and whose values are scalar values for this asset for each field
        '''
        return pd.Series(self.ticker, index=self.values)

    def _many_pairs_many_values(self):
        '''
        pandas DataFrame is returned, indexed by asset.
        The columns are the requested fields,
        filled with the scalar values for each asset for each field
        '''
        return pd.DataFrame(self.ticker, index=self.pairs, columns=self.values)

    def _many_pairs_single_value(self):
        '''
        Pandas Series is returned whose indices are the pairs,
        and whose values are scalar values for each asset for the given field.
        '''
        values = []
        for pos, tick in enumerate(self.ticker):
            val = [x for x in self.ticker[pos] if x > - self.UNSET_VALUE]
            values.append(val[0])
        return pd.Series(values, index=self.pairs)
