from fxEngine.trading_simulator import TradingSimulator
from fxEngine.tests.helper import RandomStrategy
from fxEngine.strategy.dto_strategy import DTOStrategy


dto_strategy = RandomStrategy.get_strategy('current')
trading_simulator = TradingSimulator(dto_strategy)
trading_simulator.run_simulation('limited')