import six
import abc



class PairFactory(object):

    @six.add_metaclass(abc.ABCMeta)
    def get_pair(cls, pair):
        '''
        1- Obtain available pairs
        2- initialize it (assign values)
        3- return
        4- raise NotImplementedPair
        '''
