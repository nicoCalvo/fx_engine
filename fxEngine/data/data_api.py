from collections import namedtuple
from .exceptions import InvalidPairValueError


class DataAPI(object):
    '''
    This class provides a selfcontained set of method to be published in dev's console
    Through this class and using DataPortal dependencie, the simulation data is opened
    to devs using any of the public methods

    Eg: its the "data" parameter in handle_data(context, data)


    '''

    def __init__(self, data_portal):
        '''
        Attributes:
        ==========
        data_portal: Instance of DataPortal containing the required data for the simulation
        data_pairs: The DataFrame/Panel returned from DataPortal

        '''
        self.data_portal = data_portal
        self.data_pairs = ''
        self.allowed_values = ['OpenBid', 'OpenAsk', 'HighBid', 'HighAsk']

    def current(self, pairs, values, ticks):
        """
        Returns the current value of the given pairs for the given fields
        at the current simulation time.  Current values are the as-traded price
        and are usually not adjusted for events like splits or dividends (see
        notes for more information).

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
        if not self.__are_valid_pairs(pairs):
            raise InvalidPairError(str(pairs))
        self.data_portal.get_current_slice(pairs, ticks)
        if values:
            self.__get_pair_value(values)

        return self.data_pairs

    def __get_pair_value(self, values):
        if values not in self.allowed_values:
            raise InvalidPairValueError(str(values))
        # TODO see how to get only the requested columns of data
        self.data_pairs = self.data_pairs[value]

    def history(self, pairs, ticks):
        if self.__are_valid_pairs(pairs):
            pair_names = self.__get_pairs_names()
            self.data_pairs = self.data_portal.get_slice(pair_names, ticks)

    def __get_pairs_names(self):
        return [x for x.name in pairs]

    def __are_valid_pairs(self, pairs):
        return self.__get_pairs_names() in self.data_portal.get_pairs_names_list()
