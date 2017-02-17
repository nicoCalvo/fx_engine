import pandas as pd


class TickerAdapter(object):
    UNSET_VALUE = -1

    def __init__(self, ticker, pairs):
        self.ticker = ticker
        self.pairs = pairs

    #TODO convert numbers to decimal or something to avoid loosing data
    def get_ticker(self):
        if len(self.ticker) == 1:
            return self._single_pair()
        return self._many_pairs()

    def _single_pair(self):
        ticker = self.ticker[0]
        values = [x for x in ticker if x > - self.UNSET_VALUE]
        if values:
            return self._single_pair_many_values()
        return self._single_pair_single_value(ticker)

    def _many_pairs(self):
        pass

    def _single_pair_single_value(self, ticker):
        return [x for x in ticker if x > - self.UNSET_VALUE]

    def _single_pair_many_values(self):
        return [x for x in ticker if x > - self.UNSET_VALUE]

    def _many_pairs_many_values(self):
        pass

    def _many_pairs_single_value(self):
        index ='' # Get pair names
        pd.Series(np.random.randn(5), index=index)

