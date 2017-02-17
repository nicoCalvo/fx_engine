from .exceptions import InvalidPairError
from .ticker_filter import TickerFilter


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
        data_portal: Instance of DataPortal containing the required data for the simulation
        data_pairs: The DataFrame/Panel returned from DataPortal

        '''
        # TODO: Rethink current method with decorator instead. Fucking crap

        self.__data_portal = data_portal
        self.__traded_pairs = traded_pairs

    def current(self, pairs=[], values=[]):
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
        pairs = pairs if isinstance(pairs, list) else [pairs]
        values = values if isinstance(values, list) else [values]
        tick = self._DataAPI__data_portal.get_current_tick()
        ticker_filter = TickerFilter(
            tick, pairs, values, self._DataAPI__traded_pairs)

        import pdb
        pdb.set_trace()
        ticker = ticker_filter.filter()
        '''
        TODO: Format this into panda or array or single value
        '''

        return tick

    def __get_pair_value(self, values):
        if values not in self.allowed_values:
            raise InvalidPairError(str(values))
        # TODO see how to get only the requested columns of data
        self.data_pairs = self._DataAPI__traded_pairs[value]

    def history(self, pairs, ticks):
        if self.__are_valid_pairs(pairs):
            pair_names = self.__get_pairs_names()
            self.data_pairs = self.data_portal.get_slice(pair_names, ticks)
