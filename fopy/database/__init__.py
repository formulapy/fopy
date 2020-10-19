"""A Database Maneger Module

"""
from ._handle_input_formulas_dtype import _Handle_input_dtype
from collections.abc import Iterable
from ._search import  _Match

class Fdb(_Handle_input_dtype, _Match): #Puplic API

    def _search(self, pat:str or tuple=None, *args, **kwargs):
        if 'operator' not in kwargs:
            operator = ['and'] * len(pat)  #default
        else:
            operator = kwargs['operator']
            if isinstance(operator, str):
                operator = [operator] * len(pat)
        col = self._formula_col if 'col' not in kwargs else kwargs['col']
        match = 0 if operator[0] == 'or' else 1
        if pat:
            if isinstance(pat, str):
                pat = (pat, )
            pat = (*pat, *args)
            kwargs[col] = pat
        columns = self.data.columns.to_list()
        #all keys in kwargs must be in data column
        search = {kw: kwargs[kw] for kw in kwargs if kw in columns}
        return self.data[self._match(search=search, operator=operator, match=match)]
     
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