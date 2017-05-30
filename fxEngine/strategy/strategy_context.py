from ..utils.mb_connector import MbConnector
import time
import json


class StrategyContext(object):

    def __init__(self, portfolio):
        '''
            This class provides an execution environment and it can
            be modified dinamically during the execution of the strategy.
            By prodiving a context, all variables can be defined and accessed
            during the execution on each tick
        Parameters:
        ----------

            portolio: DTOPortfolio obj

        '''
        self.portfolio = portfolio
        self._open_orders = ''

