#from .dto import ValidPairs
import cython
''' TICK EXAMPLE

{u'RefreshRate': 100, u'ContextId': u'asd', u'State': u'Active', u'InactivityTimeout': 60, 
u'ReferenceId': u'asqd', u'Snapshot': {u'AssetType': u'FxSpot', u'Uic': 16, u'LastUpdated': 
u'2017-02-12T09:32:09.967000Z', u'Quote': {u'Bid': 7.43505, u'Mid': 7.435365, u'ErrorCode': 
u'None', u'Amount': 100000, u'DelayedByMinutes': 0, u'Ask': 7.43568, u'RFQState': u'None', 
u'PriceTypeAsk': u'Indicative', u'PriceTypeBid': u'Indicative'}}}
'''


# class Pair(object):
cdef class Pair:
    '''
    Pair is DTO class containing data related to a Pair such as Pip, name, etc

    '''
    cdef readonly object name
    cdef readonly object start_date
    cdef readonly object end_date
    cdef readonly object pip

    def __init__(self, name):
        '''

        '''
        self.name = name
        self.start_date = ''
        self.end_date = ''
        self.pip = ''

