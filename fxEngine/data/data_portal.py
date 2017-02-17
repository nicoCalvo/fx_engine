

class Observable(object):
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def notify_observers(self):
        [x.update() for x in self.observers]


class DataPortal(Observable):

    def __init__(self, ingester=None, pairs=None):
        super(DataPortal, self).__init__()
        self.pairs_names = [x.name for x in pairs]
        self.ingester = ingester
        self.data_bundle = ''
        self.current_tick = ''

    def ingest(self):
        self.data_bundle = self.ingester.ingest()

    def get_pairs_names_list(self):
        return self.data_bundle.cols.names[1:]

    def get_slice(self, pair, ticks):
        return self.data_bundle.cols[pair][-ticks:]

    def _add_new_tick(self, tick):
        '''
        put the tick into data_bundle and check size, apply LIFO to the queue

        '''
        pass

    def has_new_tick(self):
        self.get_current_tick()
        if self.current_tick:
            self.notify_observers()
            return True
        return False

    def get_current_tick(self):
        self.current_tick = self.ingester.current_tick()
        return self.current_tick[1:] # Jumps timestamp
