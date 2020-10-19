"""Solving a fourmula for a variable
"""
import sympy as sp


def solve_for(expr: str, var: str) -> list: #local API
    """solve for `var` in `expr`.
    This function wrap over sympy.solve

    Parameters
    ----------
    expr : str
        A formula in a string format.
    var : str
        The variable that is being solved for.

    Returns
    -------
    list
        list of exprestions of sympy.symbols.

    Examples
    --------
    >>> import FormulaLab as fl
    >>> fl.FormulaSearch.solve_for(expr="f = m  * a", var='a')
    [ f / m ]

    """
    if '=' in expr:
        L = sp.sympify(expr.split('=')[0])
        R = sp.sympify(expr.split('=')[1])
    else:
        L = sp.sympify(expr)
        R = 0
    return sp.solve(L-R, sp.Symbol(var))