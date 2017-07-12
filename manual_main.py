from fxEngine.trading_simulator import TradingSimulator
from fxEngine.tests.helper import RandomStrategy
from fxEngine.strategy.dto_strategy import DTOStrategy


dto_strategy = RandomStrategy.get_strategy('current')
msg ={"date": "2017-06-06 08:51:05", "code": {"asset_class": "fx_spot", "end_date": "06/06/2015", "script": "def initialize(context):\n  \tpass\n\ndef handle_data(context, data):\n    #log.info(data.current())\n    data.history('USDEUR',3)\n    #order.limit_order(pair=['EURUSD'],price=1000)\n    #log.info(context.portfolio.cash)", "capital_base": 10000, "broker": "saxo", "list_symbols": ["EURUSD"], "data_feed": "saxo", "languaje": "Python", "frequency": "daily", "simulation_mode": "backtest", "id": "blas@atakama.io/103/4598661d18d93a349608ae5a069667c2699b570e", "start_date": "06/06/2013"}, "user": {"email": "blas", "name": "blas@atakama.io"}}
trading_simulator = TradingSimulator(dto_strategy, msg)
trading_simulator.run_simulation('limited')