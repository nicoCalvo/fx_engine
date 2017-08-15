'''
DTO: Data Transfer Object

Each data structured is wrapped into methodless class
in order to comply OOP design rules

nameduples are the DTO built-in class for such purpose
'''

from collections import namedtuple


Position = namedtuple(
    'Position', 'id amount place_date symbol profit')

Portfolio = namedtuple(
    'Portfolio', 'value returns return_std beta std sharpe cumulative_returns max_drawdown positions')

Portfolio = namedtuple(
	'Portfolio', 'value, symbol_positions_value')

# TODO: Define how valid pairs will be available (each data feed could
# have their owns)

Order = namedtuple('Order', 'id date symbol amount' )
