from fxEngine.strategy.dto_strategy import DTOStrategy

str_strategy_invalid_pair = {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR", "BOLPAR"], "start_date": "2015-10-03",
                                          "script": "f\n\n\ndef initialize(context):\n   context.i = 0 \n\n\ndef handle_data(context, data):\n    print data\n    print data.__dict__\n    order(symbol(\'AAPL\'), 10)\n      record(AAPL=data.current(symbol(\'AAPL\'), \'price\'))\n"}
str_strategy_valid_pair = {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR"], "start_date": "2015-10-03",
                                        "script": "\n\n\ndef initialize(context):\n   context.i = 0 \n\n\ndef handle_data(context, data):\n    print data\n    print data.__dict__\n    order(symbol(\'AAPL\'), 10)\n"}

str_strategy_invalid_script = {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR"], "start_date": "2015-10-03",
                                   "script": "NOT A VALID STRATEGY"}

str_strategy_valid_script= {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR"], "start_date": "2015-10-03",
                            "script": "\n\n\ndef initialize(context):\n   context.i = 0 \n\n\ndef handle_data(context, data):\n    print data\n    print data.__dict__\n    order(symbol(\'AAPL\'), 10)\n"}


VALID_STRATEGY = DTOStrategy(**str_strategy_valid_script)
INVALID_STRATEGY = DTOStrategy(**str_strategy_invalid_script)
STRATEGY_VALID_PAIR = DTOStrategy(**str_strategy_valid_pair)
STRATEGY_INVALID_PAIR = DTOStrategy(**str_strategy_invalid_pair)