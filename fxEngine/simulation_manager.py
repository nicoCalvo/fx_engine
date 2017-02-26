

class SimulationManager(object):

    def __init__(self, clock, strategy, scheduler):
        self.clock = clock
        self.strategy = strategy
        self.scheduler = scheduler

    def simulate(self):
    	'''
		TODO: Define if any "teardown" method will be need to perform some
		closing calculations and metrics
    	'''
        self.strategy.initialize()
        self.clock.get_first_tick()
        self.strategy.handle_data()
        while self.clock.has_new_tick():
            self._run_scheduled_functions()
            self.strategy.handle_data()

        #self.strategy.tear_down()


    def _run_scheduled_functions(self):
    	self.scheduler.run_scheduled(self.clock)

