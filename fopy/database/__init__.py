p"""A Database Maneger Module

Puplic API
==========

Search
------

add_data
--------

rm_data
-------

Private API
===========
 _load_data

"""

class FDb: #Puplic API

    def __init__ec(self, data, *args, **Kwargs):
        pass

    def _load_data(self,):
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
        pass

    def search(self, *args, **kwargs):  # should return Formulas obj
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
        # creat a subset of data that is a Formulas obj
        pass

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