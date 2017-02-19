from fxEngine.strategy.dto_strategy import DTOStrategy

str_strategy_invalid_pair = {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR", "BOLPAR"], "start_date": "2015-10-03",
                                          "script": "f\n\n\ndef initialize(context):\n   context.i = 0 \n\n\ndef handle_data(context, data):\n    print data\n    print data.__dict__\n    order(symbol(\'AAPL\'), 10)\n      record(AAPL=data.current(symbol(\'AAPL\'), \'price\'))\n"}
str_strategy_valid_pair = {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR"], "start_date": "2015-10-03",
                                        "script": "\n\n\ndef initialize(context):\n   context.i = 0 \n\n\ndef handle_data(context, data):\n    print data\n    print data.__dict__\n    order(symbol(\'AAPL\'), 10)\n"}

str_strategy_invalid_script = {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR"], "start_date": "2015-10-03",
                                   "script": "NOT A VALID STRATEGY"}

str_strategy_valid_script= {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR"], "start_date": "2015-10-03",
                            "script": "\n\n\ndef initialize(context):\n   context.i = 0 \n\n\ndef handle_data(context, data):\n    print data\n    print data.__dict__\n    order(symbol(\'AAPL\'), 10)\n"}

write_to_file = {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR"], "start_date": "2015-10-03",
                            "script": "\n\n\ndef initialize(context):\n   context.i = 0\n   f = open('out.log','w')\n   f.write(str(context))\n   f.close()\n\n\ndef handle_data(context, data):\n    context.i += 1\n    order(symbol(\'AAPL\'), 10)\n"}

atakama_api = {"id": "2", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR", "ARSMEX"], "start_date": "2015-10-03",
                            "script": "from atakama_api.dates import Dates\n\n\ndef initialize(context):\n    context.i = 4\n    context.dates = Dates(['2012-03-04','2012-05-04'])\n\ndef handle_data(context, data):\n    context.i += 1\n    context.dates.write_dates()\n\n"}


current_data_test = {"id": "9", "end_date": "2016-10-06", "capital_base": 9999999, "simulation_type": "backtest", "frequency": "daily", "pairs_list": ["USDEUR", "ARSMEX"], "start_date": "2015-10-03",
                            "script": "from atakama_api.dates import Dates\n\n\ndef initialize(context):\n    context.i = 4\n    context.dates = Dates(['2012-03-04','2012-05-04'])\n\ndef handle_data(context, data):\n    f = open('hola.log', 'a')\n    f.write(str(data.current()))\n    f.write(str(data.current('USDEUR')))\n    f.write(str(data.current('','ask')))\n    f.write(str(data.current('',['ask', 'bid'])))\n    context.i += 1\n    context.dates.write_dates()\n\n"}





VALID_STRATEGY = DTOStrategy(**str_strategy_valid_script)
INVALID_STRATEGY = DTOStrategy(**str_strategy_invalid_script)
STRATEGY_VALID_PAIR = DTOStrategy(**str_strategy_valid_pair)
STRATEGY_INVALID_PAIR = DTOStrategy(**str_strategy_invalid_pair)

WRITETOFILE = DTOStrategy(**write_to_file)
ATAKAMA_API = DTOStrategy(**atakama_api)
CURRRENT_DATA = DTOStrategy(**current_data_test)



class RandomStrategy(object):
	strategies = dict(tofile=WRITETOFILE, atakama_api=ATAKAMA_API, current =CURRRENT_DATA)

	@classmethod
	def get_strategy(cls, name):
		return cls.strategies[name]
