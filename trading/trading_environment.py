


class TradingEnvironment(object):
	'''
	Maintains the context of the running strategy

	'''

	def __init__(self, portfolio=Portfolio(), data_portal=DataPortal(),symbols):
		self.portfolio = portfolio
		self.data_portal= data_portal
		self.symbol_list = symbols
		self.perf_tracker = PerformanceTracker()
