

class Observable(object):
    def __init__(self, observers):
        self.observers = observers

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

    def __init__(self, ingester=None, pairs_names_list=None, observers=[]):
        super(DataPortal, self).__init__(observers)
        self.pairs_names = pairs_names_list
        self.ingester = ingester
        self.data_bundle = ''
  
    def ingest(self):
        self.data_bundle = self.ingester.ingest()

    def get_pairs_names_list(self):
        return self.data_bundle.cols.names

    def get_slice(self, pair, ticks):
        return self.data_bundle.cols[pair][-ticks:]

    def _add_new_tick(self, tick):
        self.notify_observers()
        '''
        put the tick into data_bundle and check size, apply LIFO to the queue

        '''
        pass

    def has_new_tick(self):
        tick = self.ingester.get_tick()
        if tick:
            self._add_new_tick(tick)
            return True
        return False

    def get_current_tick(self):
        return self.data_bundle[-1]
