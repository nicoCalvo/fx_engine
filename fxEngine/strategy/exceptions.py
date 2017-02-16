
class CompileMethodException(Exception):

    base_msg = 'Unable to compile code: '

    def __init__(self, msg):
        super(CompileMethodException, self).__init__(self.base_msg + msg)
