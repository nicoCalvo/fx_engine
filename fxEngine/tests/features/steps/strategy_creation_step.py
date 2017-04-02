from behave import given, when, then, step
from fxEngine.tests.helpers.factory import StrategyFactory
from fxEngine.trading_simulator import TradingSimulator


@given('a "{st_type}" strategy')
def st_creation(context, st_type):
    st_type = st_type.split(' ')
    st_type = ('_').join(st_type)
    context.strategy = StrategyFactory.get(st_type)


@step('we set {amount} as capital base')
def set_amount(context, amount):
    context.strategy.capital_base = int(amount)


@step('we run it')
def run_it(context):
    try:
        context.trade_sim = TradingSimulator(context.strategy)
    except Exception, e:
        context.excep = e


@step('we see a {message} exception')
def execp(context, message):
    excep_name = context.excep.__class__.__name__
    assert excep_name == message


@step('"{message}" message')
def message(context, message):
    assert context.excep.message.strip() == str(message).strip()


@step('the message is like "{message}"')
def alike_message(context, message):
    assert str(message).strip() in context.excep.message.strip()


@step('we find there are daily and monthly scheduled functions')
def no_one_reads_this(context):
    sched = context.trade_sim.api_strategy.get_scheduler()
    assert sched._has_new_day
    assert sched._has_new_month