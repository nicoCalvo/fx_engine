from data.calendar import DefaultCalendar


class DataPortal(object):

    def __init__(self, ingester=None, pairs_names_list=None,
                 calendar=DefaultCalendar()):
        self.pairs_names = pairs_names_list or DEMO_PAIRS
        self.ingester = ingester 
        self.data_bundle = ''
        self.calendar = calendar

    def ingest(self):
        self.data_bundle = self.ingester.ingest()

    def get_pairs_names_list(self):
       self.data_bundle.cols.names

    def get_slice(self, pair, ticks):
        return self.data_bundle.cols[pair][-ticks:]

    def add_new_tick(self, tick):
        '''
        put the tick into data_bundle and check size, apply LIFO to the queue

        '''
        pass

    def get_current_slice(self, pairs, ticks):
        #TODO: Get all elements in pairs and return only those
        pass
