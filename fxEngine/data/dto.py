'''
DTO: Data Transfer Object

Each data structured is wrapped into methodless class
in order to comply OOP design rules

nameduples are the DTO built-in class for such purpose
'''

from collections import namedtuple


Position = namedtuple(
    'Position', 'sid amount cost_basis, last_sale_price, last_sale_date')
Portfolio = namedtuple(
    'Portfolio', 'capital_used starting_cash portfolio_value pnl returns cash positions start_date positions_value')


# TODO: Define how valid pairs will be available (each data feed could
# have their owns)

ValidPairs = namedtuple('ValidPairs', 'EURUSD, ARSMEX, YENUSD, USDEUR')
