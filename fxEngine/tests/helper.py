from fxEngine.strategy.dto_strategy import DTOStrategy
# DTOStrategy(**str_strategy_valid_script)
str_strategy_invalid_pair = {"id": "2","broker": "Saxo",  "data_feed":"Saxo",  "mode": "local", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR", "BOLPAR"], "start_date": "2015-10-03",
                             "script": "f\n\n\ndef initialize(context):\n   context.i = 0 \n\n\ndef handle_data(context, data):\n    print data\n    print data.__dict__\n    order(symbol(\'AAPL\'), 10)\n      record(AAPL=data.current(symbol(\'AAPL\'), \'price\'))\n"}
str_strategy_valid_pair = {"id": "2", "broker": "Saxo", "data_feed":"Saxo" ,"mode": "local", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR"], "start_date": "2015-10-03",
                           "script": "\n\n\ndef initialize(context):\n   context.i = 0 \n\n\ndef handle_data(context, data):\n    print data\n    print data.__dict__\n    order(symbol(\'AAPL\'), 10)\n"}

str_strategy_invalid_script = {"id": "2", "broker": "Saxo", "data_feed":"Saxo", "mode": "local", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR"], "start_date": "2015-10-03",
                               "script": "NOT A VALID STRATEGY"}

str_strategy_valid_script = {"id": "2", "broker": "Saxo", "data_feed":"Saxo","mode": "local", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR"], "start_date": "2015-10-03",
                             "script": "\n\n\ndef initialize(context):\n   context.i = 0 \n\n\ndef handle_data(context, data):\n    print data\n    print data.__dict__\n    order(symbol(\'AAPL\'), 10)\n"}

current_data_test = {"id": "9","broker": "Saxo",  "data_feed":"Saxo", "mode": "local", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["EURUSD", "ARSMEX"], "start_date": "2015-10-03",
                     "script": "\ndef initialize(context):\n    context.i = 4\n\n\ndef handle_data(context, data):\n    order.limit_order(pair='EURUSD', price=1300)\n    context.i += 1\n    \n"}


scheduler_test = {"id": "9", "broker": "Saxo", "data_feed":"Saxo", "mode": "local", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR", "ARSMEX"], "start_date": "2015-10-03",
                  "script": "\n\n\ndef initialize(context):\n    context.i = 4\n    context.days = 0\n    context.months = 0\n\n\ndef handle_data(context, data):\n    pass\n\n\ndef before_new_day(context, data):\n    context.days += 1\n\ndef before_new_month(context, data):\n    context.months += 1"}

scheduler_plus_simpleai_test = {"id": "9","broker": "Saxo", "data_feed":"Saxo" ,"mode": "local", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR", "ARSMEX"], "start_date": "2015-10-03",
                                "script": "from atakama_api.dates import Dates\nfrom simpleai.search import SearchProblem, astar\n\n\nGOAL = 'HELLO WORLD'\n\nclass HelloProblem(SearchProblem):\n    def actions(self, state):\n        if len(state) < len(GOAL):\n            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')\n        else:\n            return []\n\n    def result(self, state, action):\n        return state + action\n\n    def is_goal(self, state):\n        return state == GOAL\n\n    def heuristic(self, state):\n        # how far are we from the goal?\n        wrong = sum([1 if state[i] != GOAL[i] else 0\n                    for i in range(len(state))])\n        missing = len(GOAL) - len(state)\n        return wrong + missing\n\n\ndef initialize(context):\n    context.i = 4\n    context.days = 0\n    context.months = 0\n    context.problem = HelloProblem(initial_state='')\n\n\ndef handle_data(context, data):\n    pass\n\n\ndef before_new_day(context, data):\n    context.days += 1\n    result = astar(context.problem)\n    f = open('resultado.log','w')\n    f.write(result.state)\n    f.write('     ')\n    f.write(str(result.path()))\n    f.close()\n\ndef before_new_month(context, data):\n    context.months += 1"}


# VALID_STRATEGY = DTOStrategy(**str_strategy_valid_script)
INVALID_STRATEGY = DTOStrategy(**str_strategy_invalid_script)
STRATEGY_VALID_PAIR = DTOStrategy(**str_strategy_valid_pair)
STRATEGY_INVALID_PAIR = DTOStrategy(**str_strategy_invalid_pair)


CURRRENT_DATA = DTOStrategy(**current_data_test)
SCHED_TEST = DTOStrategy(**scheduler_test)
SIMPLEAI_SCHED_TEST = DTOStrategy(**scheduler_plus_simpleai_test)


class RandomStrategy(object):
    strategies = dict(current=CURRRENT_DATA, sched=SCHED_TEST,
                      simpleai=SIMPLEAI_SCHED_TEST)

    @classmethod
    def get_strategy(cls, name):
        return cls.strategies[name]
