
cdef class LimitOrder:
    
    cdef readonly object buy_limit_percentage
    cdef readonly object buy_limit_pips
    cdef readonly object due_date
    cdef readonly object pair

    def __init__(self, buy_limit_percentage ):
        '''

        '''
        self.buy_limit_percentage = buy_limit_percentage
        self.buy_limit_pips = ''
        self.due_date = ''
        self.pair = ''
