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
            pairs = pairs if isinstance(pairs, list) else [pairs]
            values = values if isinstance(values, list) else [values]
            pairs = pairs if pairs else [pairs]
            values = values if values else [values]
            tick = self.__data_portal.get_current_tick()
            # ticker_filter = TickerFilter(tick=tick, filtered_pairs=pairs,
            #                              filtered_values=values,
            #                              traded_pairs=self.__traded_pairs)
            ticker_filter = TickerFilter()
            ticker_filter._tick = tick
            # ticker_filter = TickerFilter(filtered_pairs=pairs,
            #                              filtered_values=values,
            #                              traded_pairs=self.__traded_pairs,
            #                              tick=json.dumps(tick))
            ticker_filter.filtered_pairs = pairs
            ticker_filter.filtered_values = values
            ticker_filter.traded_pairs = self._traded_pairs
            ticker = ticker_filter.filter()
            # ticker_adapter = TickerAdapter(ticker, pairs, values)
            # ticker = ticker_adapter.get_ticker()
        except Exception, e:
            pass
            # f = open('bosta.log', 'w')
            # f.write(str(e))
            # f.close()
        '''
        TODO: Format this into panda or array or single value
        '''
        return ticker
        # return ticker

    def _validate_values(self, values):
        if values not in self._traded_pairs:
            raise InvalidPairError(str(values))
        # TODO see how to get only the requested columns of data
        #self.data_pairs = self._traded_pairs[value]

    def history(self, pairs, ticks):
        if pairs in self._traded_pairs:
            self.data_pairs = self.data_portal.get_slice(
                self._traded_pairs, ticks)
