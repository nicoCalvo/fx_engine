from .exceptions import InvalidPairError
from .ticker_filter import TickerFilter
from .ticker_adapter import TickerAdapter
import json


class DataAPI(object):
    '''
    This class provides a selfcontained set of method to be published in dev's console
    Through this class and using DataPortal dependencie, the simulation data is opened
    to devs using any of the public methods

    Eg: its the "data" parameter in handle_data(context, data)


    '''

    def __init__(self, data_portal, traded_pairs):
        '''
        Attributes:
        ==========
        data_portal: Instance of DataPortal
        containing the required data for the simulation
        data_pairs: The DataFrame/Panel returned from DataPortal

        '''
        # TODO: Rethink current method with decorator instead. Fucking crap
        self.__data_portal = data_portal
        self._traded_pairs = traded_pairs
        self.__ticker_filter = TickerFilter(traded_pairs)
        self.__ticker_adapter = TickerAdapter()

    def current(self, pairs='', values=''):
        """
            Returns the current value of the given pairs for the given values


            Parameters
            ----------
            pairs : List of Pair instances
            values = List with allowed_values or empty for a full return
            ticks: int stating how many ticks back are requesting data

            Returns
            -------
            current_value : Scalar, pandas Series, or pandas DataFrame.
                            See notes below.

            Notes
            -----
            If a single asset and a single field are passed in, a scalar float
            value is returned.

            If a single asset and a list of fields are passed in, a pandas Series
            is returned whose indices are the fields, and whose values are scalar
            values for this asset for each field.

            If a list of assets and a single field are passed in, a pandas Series
            is returned whose indices are the assets, and whose values are scalar
            values for each asset for the given field.

            If a list of assets and a list of fields are passed in, a pandas
            DataFrame is returned, indexed by asset.  The columns are the requested
            fields, filled with the scalar values for each asset for each field.

            If the current simulation time is not a valid market time, we use the
            last market close instead.

        """
        try:
            pairs = self.__set_pairs(pairs)
            values = self.__set_values(values)
            tick = self.__data_portal.get_current_tick()
            tick = self.__ticker_filter.filter(tick, pairs, values)
            tick = self.__ticker_adapter.get_ticker(tick, pairs, values)
        except:
            pass
        return tick

    def __set_pairs(self, pairs):
        if isinstance(pairs, list):
            return pairs
        if not pairs:
            return self._traded_pairs
        return [pairs]

    def __set_values(self, values):
        if isinstance(values, list):
            return values
        if not values:
            return self.__ticker_filter._allowed_values
        return [values]

    def _validate_values(self, values):
        if values not in self._traded_pairs:
            raise InvalidPairError(str(values))

    def history(self, pairs, ticks):
        if pairs in self._traded_pairs:
            self.data_pairs = self.data_portal.get_slice(
                self._traded_pairs, ticks)
