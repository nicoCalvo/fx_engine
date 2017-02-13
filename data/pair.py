#TODO: Move this class to CPython

class Pair(object):
	'''
	Pair is DTO class containing data related to a Pair such as Pip, name, etc

	'''
    __slots__ = ('name','start_date', 'end_date' )

    def __init__(self, name):
        self.name = name
        self.start_date = ''
        self.end_date = ''
        self.pip = ''

    



