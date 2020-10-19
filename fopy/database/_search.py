""" A private module that provide tools for search FDb
"""
import pandas as pd

class _Match:
    # Provide:
        # General Search -> DataFrame
        # Search for args/var/func. -> List[str]
        # Search for Build-in math function. eg., sin, diff. -> List[str]


    def _match(self, search:dict, operator:list, match) -> pd.Series:
        """Search in a database and produce a series of bool

        Parameters
        ----------
        search : dict
            { a column : [pattern to be searched, ] }
        operator : list
            Define the searching mode with either "and" or "or", default "and"
        match : pd.Series[bool]
            Initial Matching to be included, default 1 for operator="and", and 0 for operator="or" 
        """ 
        for i, col in enumerate(search):
            if operator[i] == 'or':
                match |= self._match_pat(pat='|'.join(search[col]), col=col)
            else: #and
                for pat in search[col]:
                    match = match & self._match_pat(pat, col=col)
        return match

    def _match_pat(self, pat:str, col:str):
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

    
