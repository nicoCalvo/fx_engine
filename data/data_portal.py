from .demo_data_loader import DEMO_PAIRS, DemoLoader
from data.calendar import DefaultCalendar

class DataPortal(object):

    def __init__(self, ingester=None, pairs_list=None, calendar= DefaultCalendar()):
        self.pairs = pairs_list or DEMO_PAIRS
        self.ingester = ingester or DemoLoader()
        self.data_bundle = ''
        self.calendar = calendar

    def ingest(self):
        self.data_bundle = self.ingester.ingest()

    def get_pairs_list(self):
        # FIXME: Find how to return all loaded pairs available
        self.data_bundle.cols['uru_ars']

    def get_slice(self, pair, ticks):
    	return self.data_bundle.cols[pair][:-ticks]