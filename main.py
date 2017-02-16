#
# Copyright 2017 Atakama
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fxEngine.trading_simulator import TradingSimulator
from fxEngine.strategy.dto_strategy import DTOStrategy
import json


## MAIN SIMULATION PROOF

'''
crear json con DTOStrategy

'''
import pdb
pdb.set_trace()
valid_st = json.loads('''{"id":"320" ,"capital_base":"9000", "start_date":"2012-03-05","end_date":"1900-01-01","pairs_list":["EURUSD", "ARSMEX"] ,"frecuency":"intraday", "script":"from data.pair import Pair\ndef initialize(context):\n    context.benchmarkSecurity = symbol('IWM')\n    print 'HOLA MUNDO!'\n    schedule_function(func=regular_allocation,\n                      date_rule=date_rules.week_start(),\n                      time_rule=time_rules.market_open(),\n                      half_days=True\n                      )\n    #schedule_function(func=reset_stoploss,\n    #                  date_rule=date_rules.month_start(),\n    #                  time_rule=time_rules.market_open(minutes=1),\n    #                  half_days=True\n    #                  )\n    context.days = 0\n    context.cached_universe = None\n    schedule_function(bookkeeping)\n    set_slippage(slippage.FixedSlippage(spread=0.00))\n}\n    context.stocks = 6\n                          \n    context.stop_price = {}\n    context.stop_pct = 0.98\n\ndef reset_stoploss(context, data):\n    context.stop_price = {}\n    \ndef set_stoploss(context, data):\n    longs = context.longs.index\n    shorts = context.shorts.index\n    \n    for sid in longs:\n        if sid in data:\n            if sid in context.stop_price:\n                context.stop_price[sid] = max(context.stop_price[sid], context.stop_pct * data[sid].price)\n            else:\n                context.stop_price[sid] = context.stop_pct * data[sid].price\n\n    for sid in shorts:\n        if sid in data:\n            if sid in context.stop_price:\n                context.stop_price[sid] = min(context.stop_price[sid], data[sid].price / context.stop_pct)\n            else:\n                context.stop_price[sid] = data[sid].price / context.stop_pct\n\ndef handle_data(context, data):\n    print data\n    Pair('EUR/USD')\n#    if len(context.longs) and len(context.shorts):\n#       print 'HOLA MUNDO2!'\n#       execute_stop(context, data)\n    pass\n"}''')
        
dto_strategy = DTOStrategy(**valid_st)
trading_simulator = TradingSimulator()


