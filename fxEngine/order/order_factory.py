import abc
import six

from fxEngine.order.order_enum import Order
from fxEngine.order.exceptions import NotImplementedOrder


@six.add_metaclass(abc.ABCMeta)
class OrderFactory():

    @abc.abstractmethod
    def get_order(cls, type):
        try:
            order = Order['type']
        except:
            raise NotImplementedOrder(type)
        return order()

print OrderFactory.get_order('limit')
