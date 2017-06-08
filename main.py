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
# from fxEngine.tests.helper import RandomStrategy
import os
import pika
import json
from fxEngine.strategy.dto_strategy import DTOStrategy
import logging
import time
import sys
LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

'''
{"date": "2017-05-21 19:56:14", "code": {"end_date": "05/19/2017", "script": "def initialize(context):\n  \tpass\ndef handle_data(context, data):\n    log.info('fecha de hoy: ' + date.get_date())\n", "mode": "backtest", "capital_base": 10000, "broker": "saxo", "data_feed": "saxo", "id": "2", "languaje": "Python", "frequency": "daily", "pairs_list": ["EURCAD", "NZDUSD"], "start_date": "05/19/2017"}, "user": {"email": "blas", "name": "blas@atakama.io"}}
'''


if __name__ == "__main__":
    host = os.environ.get('RABBIT_HOST', '127.0.0.1')
    port = int(os.environ.get('RABBIT_PORT', 5672))
    virtual_host = os.environ.get('RABBIT_VHOST', "/")
    credentials = pika.PlainCredentials(
        username=os.environ.get('RABBIT_USERNAME', 'tonyg'),
        password=os.environ.get('RABBIT_PASSWORD', 'changeit'))

    con_params = pika.ConnectionParameters(host=host, port=port,
                                           credentials=credentials,
                                           virtual_host=virtual_host)
  

    try:
        instance = sys.argv[1]
    except:
        print 'Please provide fxengine instance number'
    try:
        conn = pika.BlockingConnection(con_params)
        channel = conn.channel()
        queue = 'Q_new_py_fxEngine'# + instance
        channel.queue_declare(queue=queue, durable=True)
        channel.queue_bind(queue=queue,
                       exchange='E_new_py_fxEngine',
                       routing_key='Python')

    except Exception, e:
        print 'ERROR'
        print str(e)
    def process_strategy(unused_channel, basic_deliver, properties, body):
        LOGGER.info('INCOMING MESSAGE: ' + body)
        message = json.loads(body)
        dto_strategy = DTOStrategy(**message['code'])
        trading_simulator = TradingSimulator(dto_strategy, message)
        trading_simulator.run_simulation('limited')

    channel.basic_consume(process_strategy, queue,no_ack=True)
    channel.start_consuming()
  
