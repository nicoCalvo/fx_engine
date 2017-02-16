from collections import namedtuple


Position = namedtuple(
    'Position', 'sid amount cost_basis, last_sale_price, last_sale_date')
Portfolio = namedtuple(
    'Portfolio', 'capital_used starting_cash portfolio_value pnl returns cash positions start_date positions_value')

ValidPairs = namedtuple('ValidPairs','EURUSD, ARSMEX, YENUSD, USDEUR')