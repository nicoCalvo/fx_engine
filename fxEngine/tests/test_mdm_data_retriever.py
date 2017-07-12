import unittest
from fxEngine.tests.mocks.data_retriever import MockDataRetriever



class MdmRetriever(unittest.TestCase):

    def setUp(self):
        pass

    def test_load_bundle(self):
        data_retriever = MockDataRetriever('test')
        data_bundle = data_retriever.ingest()
        self.assertEquals(data_bundle.EURDKK.ix[0].name, '2012/06/29 00:00:00')
        self.assertEquals(data_bundle.USDEUR.ix[0].name, '2012/06/29 00:00:00')
        self.assertEquals(data_bundle.EURDKK.ix[-1].name, '2012/02/13 00:00:00')
        self.assertEquals(data_bundle.USDEUR.ix[-1].name, '2012/02/13 00:00:00')



