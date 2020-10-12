""" A private module that provide tools for search FDb
"""

class _Search:
    # Provide:
        # General Search -> DataFrame
        # Search for args/var/func. -> List[str]
        # Search for Build-in math function. eg., sin, diff. -> List[str]

    def _search(self, pat:str or tuple, col:str=None) -> pd.DataFrame:
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
        """
        # Find all Matches
        if not col:
            col = self._formula_col
        if isinstance(pat, str):
            pat = (pat, )
        match = self.data[col].str.contains('|'.join(pat))
        return self.data[match]

    
