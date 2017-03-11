from enum import Enum
from fxEngine.order.limit_order import LimitOrder
from fxEngine.order.stop_order import StopOrder
from fxEngine.order.market_order import MarkerOrder


class Order(Enum):
    limit = LimitOrder
    stop = StopOrder
    market = MarkerOrder
