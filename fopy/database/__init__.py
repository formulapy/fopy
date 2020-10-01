"""A Database Maneger Module

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
        # Test data (optional)
        # Graph data
        # Compile data to fast code
        pass

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
        # 
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
