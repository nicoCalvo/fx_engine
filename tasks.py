from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from fxEngine.trading_simulator import TradingSimulator
import json
from fxEngine.strategy.dto_strategy import DTOStrategy
import pika
# set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'developer_dashboard.settings')

RABBIT_USERNAME = os.environ.get("RABBIT_USERNAME", "tonyg")
RABBIT_PASSWORD = os.environ.get("RABBIT_PASSWORD", "changeit")
RABBIT_HOST = os.environ.get("RABBIT_HOST", "localhost")
RABBIT_PORT = os.environ.get("RABBIT_PORT", "5672")
RABBIT_VHOST = os.environ.get("RABBIT_VHOST", "/")

broker_url = "amqp://{RABBIT_USERNAME}:{RABBIT_PASSWORD}@{RABBIT_HOST}:{RABBIT_PORT}/{RABBIT_VHOST}".format(
    RABBIT_USERNAME=RABBIT_USERNAME,
    RABBIT_PASSWORD=RABBIT_PASSWORD,
    RABBIT_HOST=RABBIT_HOST, RABBIT_PORT=RABBIT_PORT,
    RABBIT_VHOST=RABBIT_VHOST)

app = Celery('fx_engine', broker=broker_url,)

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.


@app.task
def mytask(message_received):
    dto_strategy = DTOStrategy(**json.loads(message_received))
    print '##########################################'
    print dto_strategy.id
    print '##########################################'

    trading_simulator = TradingSimulator(dto_strategy)
    trading_simulator.run_simulation('limited')
