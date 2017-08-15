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
import os
import pika
import json
from fxEngine.strategy.dto_strategy import DTOStrategy
import logging
LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


if __name__ == "__main__":
    host = os.environ.get('RABBIT_HOST', '127.0.0.1')
    port = int(os.environ.get('RABBIT_PORT', 5672))
    virtual_host = os.environ.get('RABBIT_VHOST', "/")
    credentials = pika.PlainCredentials(
        username=os.environ.get('RABBIT_USERNAME', 'tonyg'),
        password=os.environ.get('RABBIT_PASSWORD', 'changeit'))

    con_params = pika.ConnectionParameters(host=host, port=port,
                                           credentials=credentials,
                                           virtual_host=virtual_host,
                                           heartbeat_interval=0)
    try:
        conn = pika.BlockingConnection(con_params)
        channel = conn.channel()
        queue = 'Q_new_py_fxEngine'  # + instance

    except Exception, e:
        print '{"ERROR":"{}"}'.format(str(e))

    def process_strategy(unused_channel, basic_deliver, properties, body):
        LOGGER.info('INCOMING MESSAGE: ' + body)
        message = json.loads(body)
        dto_strategy = DTOStrategy(**message['code'])
        trading_simulator = TradingSimulator(dto_strategy, message)
        trading_simulator.run_simulation('eternal')

    channel.basic_consume(process_strategy, queue, no_ack=True)
    channel.start_consuming()
