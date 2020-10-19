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

from fopy.database import Fdb


class Formulas (Fdb):
    def __init__(self, data, formula_col="Formula", id_col="ID", compile=True):
        # Init Global Constant
        self._formula_col = formula_col
        self._id_col = id_col
        self._compile = compile

        # Load Data
            # Handle dtypes
        self._load_data(data)


    # Database API
    def search(self, pat:str or tuple=None, col:str=None, operator='or', *args, **kwargs):  # should return Formulas obj
        """Search in Formulas Database and produce a subset of Formulas obj.
        """
        return Formulas(data=self._search(pat, col=col, operator=operator, *args, **kwargs))

    # Solve API;
    def find(self,):  # should return subset of Formulas obj
        pass

    def derive(self,):  # should return a subset of Formulas obj
        pass

    # Function API
    def function(self, find_and_derive_args,):  # Uses all find/derive args + ??
        pass

    def vector(self,):
        pass

    def loop(self,):
        pass

    # Sympy API

    # scipy API


    def __add__(self, other):  # should join 'other' db to original
        pass


    def __subs__(self, other):  # should remove 'other' db from original
        pass


    def __repr__(self,):
        return self.data.__repr__()
