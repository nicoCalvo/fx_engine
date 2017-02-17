from .dto import ValidPairs

''' TICK EXAMPLE

{u'RefreshRate': 100, u'ContextId': u'asd', u'State': u'Active', u'InactivityTimeout': 60, 
u'ReferenceId': u'asqd', u'Snapshot': {u'AssetType': u'FxSpot', u'Uic': 16, u'LastUpdated': 
u'2017-02-12T09:32:09.967000Z', u'Quote': {u'Bid': 7.43505, u'Mid': 7.435365, u'ErrorCode': 
u'None', u'Amount': 100000, u'DelayedByMinutes': 0, u'Ask': 7.43568, u'RFQState': u'None', 
u'PriceTypeAsk': u'Indicative', u'PriceTypeBid': u'Indicative'}}}
'''

class Pair(object):
    '''
    Pair is DTO class containing data related to a Pair such as Pip, name, etc

    '''
    __slots__ = ('name', 'start_date', 'end_date', 'pip', 'bid','mid', 'ask','amount')

    def __init__(self, name):
        self.name = name
        self.start_date = ''
        self.end_date = ''
        self.pip = ''
        self.bid = ''
        self.mid = ''
        self.ask = ''
        self.amount = ''

    @classmethod
    def is_allowed(self, name):
        try:
            getattr(ValidPairs, name)
        except:
            return False
        else:
            return True
