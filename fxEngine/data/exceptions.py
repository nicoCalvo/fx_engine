
class InvalidPairValueError(Exception):

    base_msg = 'Allowed values must be "OpenBid", "OpenAsk", "HighBid" or "HighAsk". Received: '

    def __init__(self, msg):
        super(InvalidPairValueError, self).__init__(self.base_msg + msg)
