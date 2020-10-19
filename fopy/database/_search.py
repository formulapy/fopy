""" A private module that provide tools for search FDb
"""
import pandas as pd

class _Search:
    # Provide:
        # General Search -> DataFrame
        # Search for args/var/func. -> List[str]
        # Search for Build-in math function. eg., sin, diff. -> List[str]

    def __search(self, *args, **kwargs):
        
        if "operator" not in kwargs:
            kwargs['operator'] = 'or'
        if "_match" not in kwargs:
            _match = 0 if kwargs['operator'] == 'or' else 1
        else:
            _match = kwargs['_match']
        # if user only provide args; _search('a', 'b', 'c')
        if args:
            pat = args
        # when kwargs are provided: _search(formula=('f', 'a'), field='Math', Book='Calculus')
        elif kwargs:            
            columns = self.data.columns.to_list()
            for kw in kwargs:
                if kw in columns:
                    if kwargs['operator'] == 'or':
                        _match = _match | self._search(pat=kwargs[kw], col=kw, operator=operator, match=match)
                    match = match & self._match
            return match
                         
        if "col" not in kwargs:
            col = self._formula_col
        if isinstance(pat, str):
            pat = (pat, )
        if operator == 'or':
            return _match | self._match(pat, col=col, operator=operator, match=_match)
        # operator = and
        return _match & self._match(pat, col=col, operator=operator, match=_match)




    def _search_(self, pat:str or tuple=None, col:str=None, operator='or', match=None, *args, **kwargs) -> pd.Series:
        """General Search in Formulas Database and produce a subset of Formulas obj.

        Examples:
            >>> from fopy import Formulas
            >>> data = {'Formula': ['A = pi * r**2', 'a = v/t', 'd = v*t', 'E = m*c**2],
                        "Field"  : ['Math', 'Mechanics', 'Mechanics', "Relativity"]}
            >>> myfo = Formulas(data=data)
            >>> myfo.search("v")
            <Formulas_obj>
            >>> myfo.search("Mechanics", col="Field")
            ??
            >>> myfo.search(formula=('f', 'a'), field='Math', Book='Calculus')
            
        """
        if not match:
            match = 0 if operator == 'or' else 1
        # if user only provide args; _search('a', 'b', 'c')
        if args:
            pat = args
        # when kwargs are provided: _search(formula=('f', 'a'), field='Math', Book='Calculus')
        elif kwargs:            
            columns = self.data.columns.to_list()
            for kw in kwargs:
                if kw in columns:
                    if operator == 'or':
                        match = match | self._search(pat=kwargs[kw], col=kw, operator=operator, match=match)
                    match = match & self._match
            return match
                         
        if not col:
            col = self._formula_col
        if isinstance(pat, str):
            pat = (pat, )
        if operator == 'or':
            return match | self._match(pat, col=col, operator=operator, match=match)
        # operator = and
        return match & self._match(pat, col=col, operator=operator, match=match)

    def _match(self, pat:list, col:str, operator:str, match):
        if operator == 'or':
            return self._search_pat(pat='|'.join(pat), col=col)
        # operator == 'and'
        if pat:
            match = match & self._search_pat(pat.pop(), col=col) 
            return self._match(pat, col=col, operator=operator, match=match)
        return match

    def _search_pat(self, pat:str, col:str):
        """A single search for pattern in a certain col in the database

        Parameters
        ----------
        pat : str
            Regular expression pattern which could simply be a word
        col : str
            Column Name

        Returns
        -------
        List[bool]
            Pandas contains a list of boolean
        """
        return self.data[col].str.contains(pat)

    
