import sympy as sp



def find(self, func: str, vars: list = None, fid: int = None) -> list: # Puplic API
    """Direct search for a function with respect to variable(s).
    If id is specified, then the search is limited to one formula
    with id = "id". If more than one variable are introdueced, then only
    formula(s) with all specified variable(s) are found.

    Parameters
    ----------
    func : str
        Desired function.

    vars : list
        Desired variables

    fid : int, optional
        Restrict the search to one formula with id nunber equals to fid

    function: bool
        To convert the output function to a python function

    Returns
    -------
    list
        All found formulas in symbolic form. Or as a python function,
        at function=True

    See Also
    --------
    derive : For indirect search


    Examples
    --------
    >>> import FormulaLab as fl
    >>> data = ['f = m*a', 'a = v/t', 'd = v*t']
    >>> # Say you want to know what is v(t,a) = ?
    >>> phyfos = fl.FormulaSearch(data)
    >>> phyfos.data
            ID  Formula       Args
        0   1  f = m*a  [m, f, a]
        1   2  a = v/t  [v, a, t]
        2   3  d = v*t  [v, d, t]
    *The Args col. is automaticlly generated
    >>> v_t_a = phyfos.find('v', ['t','a'])
    >>> print(v_t_a)
    [a*t]

    Now, say you are only focused on one formula (eg., ID=3) and you want
    to call it in different places in your code/project, but you do not
    want to rewrite it again many times. Here where `find` becomes handy!
    In any place in your project, you call you formula by its `id` and in
    any form you want: `func (vars)`. For example,

    >>> a = phyfos.find(func='a', fid=1)
    >>> print(a)
    [f/m]

    If you wish the output to be as a pyhon func, then:

    >>> a = phyfos.find(func='a', fid=1, function=True)
    >>> a(f=5,m=2)
    2.5

    """
    if fid:
        return self._get_fo(fid=fid, var=func)
    if vars:
        all_var = tuple(list(vars) + [func])
        # `all_var` must be tuple because get_formula_info uses memory cach
        fo_ids = self._get_formula_info(all_var, target_col=self.id_col)
    else:
        fo_ids = self._get_formula_info(func, target_col=self.id_col)
    return [i for fo_id in fo_ids for i in self._get_fo(fid=fo_id, var=func)]


def _get_fo(self, fid: int, var: str):
    """
    Takes the fid of a formula and solve for var.
    Parameters
    ----------
    fid : int
        Fo id number.
    var : str
        Solve for var.

    Returns
    -------
    list
        list of the solutions that are in sympy symbols.

    """
    fo = self._find_raw_formula(fid)
    return solve.solve_for(expr=fo, var=var)


def _find_raw_formula(self, fid): #Name changed from get_... to find_...
    """Find a formula in the database based on its `fid`, in string format.

    Parameters
    ----------
    fid : int
        Formula fid.

    Returns
    -------
    str
        The formula as it is in the database.

    See Also
    --------
    find : In symbolic format

    """
    fo = str(self.data[self.formula_col][self._get_fo_index(id)]).strip()
    # Git ride off anotation
    if '.' in fo:
        fo = fo.replace('.', '')
    if '_ ' in fo:
        fo = fo.replace('_ ', ' ')
    rex = re.search(r'(_)+[^\w^\s]', fo)
    if rex: #* I need to think about this!
        fo = fo.replace(rex.group(), ' ' + rex.group()[-1])
        # "xx_yy_/" --> replace('_/',' /')  --> xx_yy /
    return fo