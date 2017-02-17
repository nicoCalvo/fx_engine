
class InvalidPairValueError(Exception):

    base_msg = 'Allowed values must be:'

    def __init__(self, valid_values, requested_values):
        super(InvalidPairValueError, self).__init__(
            self.base_msg + valid_values + ' RECEIVED: ' + requested_values)


class InvalidPairError(Exception):

    base_msg = 'Pair/s not in traded list pairs '

    def __init__(self, valid_pairs, requested_pairs):
        super(InvalidPairValueError, self).__init__(
            self.base_msg + valid_pairs, + ' RECEIVED:' + requested_pairs)
