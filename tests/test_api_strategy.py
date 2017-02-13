from utils.exceptions import CompileMethodException
import unittest
from strategy.api_strategy import ApiStrategy
from strategy.strategy_compiler import StrategyCompiler
from data.pair import Pair

class TestApiStrategy(unittest.TestCase):

    def setUp(self):
        pass

    # @mock.patch('strategy.api_compiler.StrategyCompiler')
    def test_valid_strategy(self):
        # mock_compiler.return_value=None

        #valid_st = 'def valid()\n   return 1'
        valid_st = '''from data.pair import Pair\ndef initialize(context):\n    context.benchmarkSecurity = symbol('IWM')\n    print 'HOLA MUNDO!'\n    schedule_function(func=regular_allocation,\n                      date_rule=date_rules.week_start(),\n                      time_rule=time_rules.market_open(),\n                      half_days=True\n                      )\n    #schedule_function(func=reset_stoploss,\n    #                  date_rule=date_rules.month_start(),\n    #                  time_rule=time_rules.market_open(minutes=1),\n    #                  half_days=True\n    #                  )\n    context.days = 0\n    context.cached_universe = None\n    schedule_function(bookkeeping)\n    set_slippage(slippage.FixedSlippage(spread=0.00))\n    set_commission(commission.PerShare(cost=0, min_trade_cost=None))\n    # Sector mappings\n    context.sector_mappings = {\n       101.0: "Basic Materials",\n       102.0: "Consumer Cyclical",\n       103.0: "Financial Services",\n       104.0: "Real Estate",\n       205.0: "Consumer Defensive",\n       206.0: "Healthcare",\n       207.0: "Utilites",\n       308.0: "Communication Services",\n       309.0: "Energy",\n       310.0: "Industrials",\n       311.0: "Technology"\n    }\n    context.stocks = 6\n                          \n    context.stop_price = {}\n    context.stop_pct = 0.98\n\ndef reset_stoploss(context, data):\n    context.stop_price = {}\n    \ndef set_stoploss(context, data):\n    longs = context.longs.index\n    shorts = context.shorts.index\n    \n    for sid in longs:\n        if sid in data:\n            if sid in context.stop_price:\n                context.stop_price[sid] = max(context.stop_price[sid], context.stop_pct * data[sid].price)\n            else:\n                context.stop_price[sid] = context.stop_pct * data[sid].price\n\n    for sid in shorts:\n        if sid in data:\n            if sid in context.stop_price:\n                context.stop_price[sid] = min(context.stop_price[sid], data[sid].price / context.stop_pct)\n            else:\n                context.stop_price[sid] = data[sid].price / context.stop_pct\n\ndef handle_data(context, data):\n    print data\n    Pair('EUR/USD')\n#    if len(context.longs) and len(context.shorts):\n#       print 'HOLA MUNDO2!'\n#       execute_stop(context, data)\n    pass\n'''
        api_strategy = ApiStrategy(
            compiler=StrategyCompiler(str_strategy=valid_st))
        api_strategy.compile_strategy()
        #(CompileMethodException, api_strategy.compile_strategy)
        import pdb
        pdb.set_trace()
        api_strategy.handle_data(data='')
        # api_strategy.

    def test_invalid_strategy(self):
        pass

   

