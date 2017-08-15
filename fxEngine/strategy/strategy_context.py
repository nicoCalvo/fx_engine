import json
from ..data.dto import Portfolio, Position


class Observer(object):

    def update(self, new_portfolio):
        pass


class StrategyContext(object):

    def __init__(self):
        '''
            This class provides an execution environment and it can
            be modified dinamically during the execution of the strategy.
            By prodiving a context, all variables can be defined and accessed
            during the execution on each tick
        Parameters:
        ----------

            None

        '''

        self.current_cash = None
        self.portfolio = None
        self._positions = {}
        self._closed_positions = dict(aggregated={}, closed={})

    def __dir__(self):
        return ['portfolio', 'current_cash']

    def __repr__(self):
        return '''StrategyContext:
                        Attributes:
                                current_cash
                                portfolio object'''

    def __dict__(self):
        return '''{'portfolio': {portfolio}, 'current_cash': {cash}}'''.format(portfolio=self.portfolio,
                                                                               cash=self.current_cash)

    def update(self, new_portfolio):
        if not isinstance(new_portfolio, dict):
            new_portfolio = json.loads(new_portfolio)
        self._update_portfolio(new_portfolio['portfolio'])
        self._update_positions(new_portfolio['positions'])
        self.current_cash = new_portfolio['current_cash']

    def _update_portfolio(self, new_portfolio):
        self.portfolio = Portfolio(new_portfolio['value'],
                                   new_portfolio['open_positions'])


    def _update_positions(self, new_positions):
        if not isinstance(new_positions, dict):
            new_positions = json.loads(new_positions)
        if new_positions['aggregated']:
            aggregated_ids = {}
            for id, pos_aggregated in new_positions['aggregated'].iteritems():
                aggregated_ids[pos_aggregated['symbol']] = id
            for pos in self._positions:
                self._closed_positions['aggregated'][pos.id] = [[aggregated_ids[pos.symbol],
                                new_positions['aggregated'][aggregated_ids[pos.symbol]]['place_date']]]
            self._positions = {}  
        
        if new_positions['open']:
            for id, open_position in new_positions['open'].iteritems():
                self._positions[id] = Position(id, open_position['amount'],
                                               open_position['place_date'],
                                               open_position['symbol'],
                                                open_position['profit'])
        for ix, pos in self._positions.iteritems():
            if ix == new_positions['closed']:
                self._positions.pop(ix)
                self._closed_positions['closed'][ix] = pos

    def is_position_open(self, pos):
        return (pos.id in self._closed_positions['closed'] or
                pos.id in self._closed_positions['aggregated'])
    


