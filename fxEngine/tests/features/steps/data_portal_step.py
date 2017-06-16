import pyximport
pyximport.install()
from fxEngine.data.data_portal import DataPortal
from fxEngine.data.data_api import DataAPI
from fxEngine.tests.data_demo_loader import DemoLoader
import ast

# Tiene que instanciarse un data api y
# probar todo el modulo
# con el ticker filter y adapter

@given('a data with {pairs} pairs')
def load_portal(context, pairs):
    context.pairs = ast.literal_eval(pairs)
    context.data_portal = DataPortal(ingester=DemoLoader(), pairs=context.pairs)
    context.data_api = DataAPI(data_portal=context.data_portal,
                               traded_pairs=context.pairs)


@step('we ingest the history')
def ingest(context):
    context.data_portal.ingest()


@step('we ask for current tick with pair {pair} and value {value}')
def current(context, pair, value):
    context.value = context.data_api.current(pair, value)


@step('we see a single float value')
def get_pair(context):
    assert isinstance(context.value, float)
