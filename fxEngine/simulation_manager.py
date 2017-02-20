

class SimulationManager(object):

    def __init__(self, clock, strategy, scheduler):
        self.clock = clock
        self.strategy = strategy
        self.scheduler = scheduler

    def simulate(self):
    	'''
		las funciones scheduled reciben como parametro el nombre de la funcion a ejecutar y los parametros
		El scheduler le pasa a cada funcion a ejecutar el self.strategy asi ejecuta la funcion que se 
		pasa como nombre del parametro, y los parametros
		SOY DIOS
		
    	'''

    	# @@ VER COMO HAGO CON EL TICK DE DATOS
    	# @@ VER QUE ES EL OBJECTO data PASADO A handle_data 
        self.strategy.initialize()
        self.clock.get_first_tick()
        self.strategy.handle_data()
        while self.clock.has_new_tick():
            self._run_scheduled_functions()
            self.strategy.handle_data()

        #self.strategy.tear_down()


    def _run_scheduled_functions(self):

        if self.clock.is_new_day():
            self.scheduler.before_new_day()
        if self.clock.is_new_week():
            self.scheduler.before_new_week()
        if self.clock.is_new_month():
            self.scheduler.before_new_month()
