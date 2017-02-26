

class Scheduler(object):
    STRATEGY = ''

    @classmethod
    def on_new_day(cls, function_name):
        func = cls.STRATEGY[function_name]

    def on_intraday(cls, function_name, time):
        pass

    def on_interday(cls, function_name, date):
        pass


class DailyScheduler(object):
    context = ''
    data = ''

    @classmethod
    def execute(cls, callback):
        import pdb
        pdb.set_trace()
        
        exec_(callback(cls.context, cls.data))
