from atakama_api.utils import MbConnector
import json
from performance.performance_tracker import RabbitConnectionError

class SimulationManager(object):

    def __init__(self, clock, strategy, scheduler):
        self.clock = clock
        self.strategy = strategy
        self.scheduler = scheduler

    def simulate(self):
        '''
            TODO: Define if any "teardown" method will be need
            to perform some
            closing calculations and metrics
        '''
        try:
            self.strategy.initialize()
            self.clock.get_first_tick()
            self.strategy.handle_data()
            while self.clock.has_new_tick():
                self._run_scheduled_functions()
                self.strategy.handle_data()
        except RabbitConnectionError:
            conn = MbConnector.get_connection()
            channel = conn.channel()
            msg = dict(message='RUNTIME ERROR: '+ ' - ' + 'INTERNAL ERROR. PLEASE TRY AGAIN', simulation_date='1901-01-01')
            channel.basic_publish(exchange='E_standard_log',
                                  routing_key=self.strategy.dto_strategy.id,
                                  body=json.dumps(msg))
            pass

        except Exception, e:
            print '\n\n\n'
            print 'se rompio todo: ' + str(e)
            print '\n\n\n'
            conn = MbConnector.get_connection()
            channel = conn.channel()
            msg = dict(message='RUNTIME ERROR: ' + ' - ' + str(e), simulation_date='1901-01-01')
            channel.basic_publish(exchange='E_standard_log',
                                  routing_key=self.strategy.dto_strategy.id,
                                  body=json.dumps(msg))

            pass

          

    def _run_scheduled_functions(self):
        self.scheduler.run_scheduled(self.clock)
