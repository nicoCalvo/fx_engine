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
                # publish orders
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

            # host = os.environ.get('RABBIT_HOST', 'localhost')
            # port = os.environ.get('RABBIT_PORT', 5672)
            # virtual_host = os.environ.get('RABBIT_VHOST', "/")
            # credentials = pika.PlainCredentials(
            #     username=os.environ.get('RABBIT_USERNAME', 'tonyg'),
            #     password=os.environ.get('RABBIT_PASSWORD', 'changeit'))
            # max_tries = 5
            # tries = 0
            # self.clock = ''
            # while tries < max_tries:
            #     try:
            #         conn = pika.BlockingConnection(
            #             pika.ConnectionParameters(host=host, port=int(port),
            #                                       credentials=credentials,
            #                                       virtual_host=virtual_host,
            #                                       socket_timeout=3000))
            #     except Exception, e:
            #         # logging.info('Unable to connect to Rabbit- ' + str(e))
            #         time.sleep(1)
            #         tries += 1
            #     else:
            #         break
            # channel = conn.channel()
            # channel.basic_publish(exchange='E_standard_log',
            #                       routing_key=self.strategy.dto_strategy.id,
            #                       body=str(e))
            # conn.close()
            # pass
        # self.strategy.tear_down()

    def _run_scheduled_functions(self):
        self.scheduler.run_scheduled(self.clock)
