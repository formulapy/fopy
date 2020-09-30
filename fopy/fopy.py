"""Main module API.


## Formulas Public API:
    # FormulasDb
        # search -> subset of Formulas obj
        # add_data
        # rm_data
    # Solve
        # find
        # derive
    # function
        # function
        # vector
        # loop
    # sympy API  - Nativly under Formulas obj
        # - for all subset formulas, including single formula:
            # solve_for
            # diff
            # ...
        # to_sympy - convert to sympy obj
    # Scipy API  - Nativly under Formulas obj
        #- for all formulas subset / including single formula:
            # root
            # quad
            # diff
            # ...

## Formulas Private API:
    # FormulasDb
        # Store DB
        # Test DB (optional)
        # Export subset of Db with graph (under search)
    # Graph
        # Compile_to_graphs
        #   To new graph
        #   To existing graph
        # Export subset of graph
    # Compile to fast code
        # Numba
        # cython ?
        # Julia ?
        # C/C++ ?
        # ?
    # Solve
        # Trace
    # Function
        # bind - bring the right compiled formula from compiled formulas
        #        with proper wraping
        # compile - express comiling for single expr
    # Sympy API
        # Wraper - loops over formulas obj and apply sympy function?
    # Scipy API
        # Wraper - loops over formulas obj and apply scipy function ??


"""


class Formulas:
    def __init__(self, Data, compile=True):
        pass

    # DataBase API
    def search(self, *args, **kwargs):  # should return Formulas obj
        """Search in Formulas Database and produce a subset of Formulas obj.

        Examples:
            >>> from fopy import Formulas
            >>> data = {'Formula': ['A = pi * r**2', 'a = v/t', 'd = v*t', 'E = m*c**2],
                        "Field"  : ['Math', 'Mechanics', 'Mechanics', "Relativity"]}
            >>> myfo = Formulas(data=data)
            >>> myfo.search("v")
            ??
            >>> myfo.search(Field="Mechanics")
            ??
        """
        pass

    def add_data(self, data):
        """data to be included to the original db, graph and compiled code.

        Parameters
        ----------
        data : str, list, tuple, dict, or pd.DataFrame
            If str is provided, it must be a path to a .csv database.
        """
        pass

    def rm_data(self, data):
        """data to be removed from the original database, graph and compiled code.

        Parameters
        ----------
        data : str, list, tuple, dict, or pd.DataFrame
            If str is provided, it must be a path to a .csv database.
        """
        pass

    # Solve API;
    def find(
        self,
    ):  # should return subset of Formulas obj
        pass

    def derive(
        self,
    ):  # should return a subset of Formulas obj
        pass

    # Function API
    def function(
        self,
        find_and_derive_args,
    ):  # Uses all find/derive args + ??
        pass

    def vector(
        self,
    ):
        pass

    def loop(
        self,
    ):
        pass

    # Sympy API

    # scipy API


def __add__(self, other):  # should join 'other' db to original
    pass


def __subs__(self, other):  # should remove 'other' db from original
    pass


def __repr__(
    self,
):
    """return pd.DataFrame of the database"""
    pass
