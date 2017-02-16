from ..data.dto import Portfolio, Position


class Observer(object):

    def update(self):
        pass


class PerformanceTracker(Observer):

    def __init__(self, strategy):
        self.strategy = strategy

    def update(self):
        '''
        RETRIEVE UPDATED PORTFOLIO
        AND SET IT TO STRATEGY
        '''
        self.strategy.portfolio = self._retrieve_portfolio()

    def _retrieve_portfolio(self):
        '''
        AS OF NOW, IT RETURN A MockedPortfolio
        '''
        return Portfolio(9999, 100000, 3456, 0.0, 123, 33345, [Position(
            2, 34, 54, 56, 78), Position(2, 34, 54, 56, 78)], '2012-03-04', 42423)
