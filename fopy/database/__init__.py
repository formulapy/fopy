"""A Database Maneger Module

"""
import pandas as pd
from ._handle_input_formulas_dtype import _Handle_input_dtype
from collections.abc import Iterable
#from fopy import Formulas

class Fdb(_Handle_input_dtype): #Puplic API


    def _load_data(self, data):
        # Save data to .csv (if not exist)
        #   Convert data to pandas DataFrame
        #   Save it to .cvs
        # Graph data
        #   Generate a graph for all formulas
        #   Save it
        # Compile data to fast code
        #   Convert formulas to c/c++ comiled code
        #       Formulas id should be shared and imutable
        #   Save the compile code
        # Test data (optional)
        #   Evalute formulas against a test provided by the user
        self._handle_input_dtype(data)


    def _search(self, *args, **kwargs):  # should return Formulas obj
        """Search in Formulas Database and produce a subset of Formulas obj.

        Examples:
            >>> from fopy import Formulas
            >>> data = {'Formula': ['A = pi * r**2', 'a = v/t', 'd = v*t', 'E = m*c**2],
                        "Field"  : ['Math', 'Mechanics', 'Mechanics', "Relativity"]}
            >>> myfo = Formulas(data=data)
            >>> myfo.search("v")
            <Formulas_obj>
            >>> myfo.search(Field="Mechanics")
            ??
        """
        # Find all Matches
        if kwargs:
            col = list(kwargs)[0]
            args = kwargs[col]
            if isinstance(args, str):
                args = (args, )
        else:
            col = self._formula_col
        match = self.data[col].str.contains('|'.join(args))
        return self.data[match]

        # creat a subset of data that is a Formulas obj
        

    def update(self, *args, **kwargs):
        """Update the database eith by including data to the original database or by
        removing data, or both. That includes updating graph and compiled code.

        Parameters
        ----------
        data : pd.DataFrame, Dict, list, tuple, str
            If str is provided, it must be a path to a .csv database.
        mode : str
            "update", "add" or "remove", default "update"
            
        """
        pass