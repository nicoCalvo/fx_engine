class NotImplementedOrder(Exception):

    base_msg = 'Order type not available: {}'

    def __init__(self, msg):
        super(NotImplementedOrder, self).__init__(self.base_msg.format(msg))


class InvalidPairOrder(Exception):

    base_msg = 'Pair not available in simulation: {}'

    def __init__(self, msg):
        super(InvalidPairOrder, self).__init__(self.base_msg.format(msg))


class InvalidPriceOrder(Exception):

    base_msg = 'Invalid price: {}'

    def __init__(self, msg):
        super(InvalidPairOrder, self).__init__(self.base_msg.format(msg))


class InvalidDueDate(Exception):

    base_msg = 'Invalid due date: {}'

    def __init__(self, msg):
        super(InvalidPairOrder, self).__init__(self.base_msg.format(msg))
