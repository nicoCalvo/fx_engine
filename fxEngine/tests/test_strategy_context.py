import unittest
import json
from fxEngine.strategy.strategy_context import StrategyContext
from fxEngine.data.dto import Position

class TestStrategyContext(unittest.TestCase):


	def setUp(self):
		pass

	def test_new_portfolio(self):
		new_portfolio = json.loads(get_portfolio_no_positions())
		st_context = StrategyContext()
		st_context._update_portfolio(new_portfolio['portfolio'])

	def test_new_positions(self):
		st_context = StrategyContext()
		mock_already_open_pos = already_open = ['order_1a', 'order_1b']
		pos_list = []
		pairs = ["USDEUR", "EURDKK"]
		symbol = True
		for pos in mock_already_open_pos:
			pos_list.append(Position(pos, 300,"2017/08/10 00:06:00",pairs[symbol], 234.23 ))
			symbol =  not symbol
		st_context.positions = pos_list
		
		st_context._update_positions(get_positions())

	def test_instropection(self):
		st_context = StrategyContext()
		res =  dir(st_context)
		self.assertEquals(set(res),set(['portfolio','current_cash']))

	def test_new_portfolio_and_positions(self):
		st_context = StrategyContext()
		new_portfolio = get_full_portfolio()
		st_context.update(new_portfolio)
		self.assertEquals(st_context._closed_positions['aggregated'], {})
		self.assertEquals(st_context._closed_positions['closed'], {})
		self.assertEquals(st_context.portfolio.value, 987)






























def get_positions():

	'''
	This  scenario contemplates the most complicated case.
	The Aggregated Ids were also, at the same transaction,
	closed due to the aggregated matched an incoming position 
	and therefore the aggregated id "CAxNDoxNTowNy42NjY1MDZFVVJES0s="
	shows up on "closed" and not in "open"

	'''
	return {
   "open":{
      "CLONE-order_1a":{
         "short_long":"ask",
         "profit":0.0,
         "counter_symbol":"EURUSD",
         "symbol":"USDEUR",
         "initial_price":2.0210262828,
         "amount":-120.0,
         "current_price":2.0210262828,
         "counter_pair_price":0.4947981174,
         "place_date":"2017/08/10 00:12:00"
      },
      "CAxNDoxNTowNy42NjY0NjFVU0RFVVI=":{
         "short_long":"ask",
         "profit":0.0,
         "counter_symbol":"EURUSD",
         "symbol":"USDEUR",
         "initial_price":2.0210262828,
         "amount":-120.0,
         "current_price":2.0210262828,
         "counter_pair_price":0.4947981174,
         "place_date":"2017/08/10 00:12:00"
      }
   },
   "aggregated":{
      "CAxNDoxNTowNy42NjY1MDZFVVJES0s=":{
         "amount":33.0,
         "symbol":"EURDKK",
         "place_date":"2017/08/10 00:12:00",
         "initial_price":7.8444925859
      },
      "CAxNDoxNTowNy42NjY0NjFVU0RFVVI=":{
         "amount":-120.0,
         "symbol":"USDEUR",
         "place_date":"2017/08/10 00:12:00",
         "initial_price":2.0210262828
      }
   },
   "closed":[
      "order_1a",
      "order_1b",
      "CAxNDoxNTowNy42NjY1MDZFVVJES0s="
   ]
}







def get_portfolio_no_positions():
	return '''{
	   "portfolio":{
	      "value":10000,
	      "open_positions":[

	      ]
	   },
	   "current_cash":10000,
	   
	   "positions":{
	      "open":[

	      ],
	      "aggregated":[

	      ],
	      "closed":[

	      ]
	   }
	}'''


def get_full_portfolio():
	return '''{
	   "portfolio":{
	      "value":987,
	      "open_positions":[
	      ]
	   },
	   "current_cash":10000,
	   "positions":{
		     "open":{
			      "CLONE-order_1a":{
			         "short_long":"ask",
			         "profit":0.0,
			         "counter_symbol":"EURUSD",
			         "symbol":"USDEUR",
			         "initial_price":2.0210262828,
			         "amount":-120.0,
			         "current_price":2.0210262828,
			         "counter_pair_price":0.4947981174,
			         "place_date":"2017/08/10 00:12:00"
			     },
			      "CAxNDoxNTowNy42NjY0NjFVU0RFVVI=":{
			         "short_long":"ask",
			         "profit":0.0,
			         "counter_symbol":"EURUSD",
			         "symbol":"USDEUR",
			         "initial_price":2.0210262828,
			         "amount":-120.0,
			         "current_price":2.0210262828,
			         "counter_pair_price":0.4947981174,
			         "place_date":"2017/08/10 00:12:00"
		      	}
		   },
		   "aggregated":{
		      "CAxNDoxNTowNy42NjY1MDZFVVJES0s=":{
		         "amount":33.0,
		         "symbol":"EURDKK",
		         "place_date":"2017/08/10 00:12:00",
		         "initial_price":7.8444925859
		      },
		      "CAxNDoxNTowNy42NjY0NjFVU0RFVVI=":{
		         "amount":-120.0,
		         "symbol":"USDEUR",
		         "place_date":"2017/08/10 00:12:00",
		         "initial_price":2.0210262828
		      }
		   },
		   "closed":[
		      "order_1a",
		      "order_1b",
		      "CAxNDoxNTowNy42NjY1MDZFVVJES0s="
		   ]
	   }
	}'''


def get_portfolio_with_positions():
	return '''
	{"portfolio": {
		"value": 9999.9968959375,
		"open_positions": 
			"{
			    \"EURDKK\":
			        {
			          \"profit\":-0.0031040625},
			    \"USDEUR\":
			        {
			           \"profit\":0.0}
			 }"
	    },
	 "current_cash": 10000,
	 "ticker": 
	 {"ticker": [{"ask": 1.43291, "bid": 1.43199, "medium": 1.43245, "symbol": "USDEUR", "time": "2010/01/04 00:00:00"}, {"ask": 0.134375, "bid": 0.134388, "medium": 0.134382, "symbol": "DKKUSD", "time": "2010/01/04 00:00:00"}, {"ask": 7.44185, "bid": 7.44115, "medium": 7.4415, "symbol": "EURDKK", "time": "2010/01/04 00:00:00"}], "bar": [{"low_bid": 1.42565, "high_ask": 1.44591, "symbol": "USDEUR", "close_bid": 1.44126, "high_bid": 1.44554, "time": "2010/01/04 00:00:00", "open_bid": 1.43199, "close_ask": 1.44146, "open_ask": 1.43291, "low_ask": 1.42585}, {"low_bid": 0.13441, "high_ask": 0.134366, "symbol": "DKKUSD", "close_bid": 0.134384, "high_bid": 0.134377, "time": "2010/01/04 00:00:00", "open_bid": 0.134388, "close_ask": 0.134375, "open_ask": 0.134375, "low_ask": 0.134391}, {"low_bid": 7.43995, "high_ask": 7.44235, "symbol": "EURDKK", "close_bid": 7.44135, "high_bid": 7.44175, "time": "2010/01/04 00:00:00", "open_bid": 7.44115, "close_ask": 7.44185, "open_ask": 7.44185, "low_ask": 7.44095}]}, "positions": {"open": {"ANOTHER_ORDER": {"short_long": "ask", "profit": 0.0, "counter_symbol": "EURUSD", "symbol": "USDEUR", "initial_price": 1.43291, "amount": -120.0, "current_price": 1.43291, "counter_pair_price": 0.6978805368, "place_date": "2010/01/04 00:00:00"}, "CANCEL_ORDER_1B": {"short_long": "bid", "profit": -0.0031040625, "counter_symbol": "DKKUSD", "symbol": "EURDKK", "initial_price": 7.44115, "amount": 33.0, "current_price": 7.44185, "counter_pair_price": 0.134375, "place_date": "2010/01/04 00:00:00"}}, "aggregated": [], "closed": []}}'''