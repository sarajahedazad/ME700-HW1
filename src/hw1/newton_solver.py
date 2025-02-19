import numpy as np
import sympy

class MaxIterationReached(Exception):  # Ensure it inherits from Exception  
    def __init__(self, message="Maximum allowed iteration reached. No roots were found."):
        super(MaxIterationReached, self).__init__(message) 

def evaluate( expr, symb, x0 ):
    func = sympy.lambdify(symb, expr, 'numpy')
    func_val = func( *x0 )
    return np.squeeze( func_val )

def inverse( mat ): # mat stands for matrix
    if mat.size > 1:
        return np.linalg.inv( mat )
    else:
        return 1 / mat

def step( F, J, x, x0):
    F_val = evaluate( F, x, x0 )
    J_val = evaluate( J, x, x0 )
    J_inv = inverse( J_val )
    x1 = x0 - np.dot( J_inv , F_val )
    return x1

def compute_abs_error( F, x, root):
    return np.abs( evaluate( F, x, root ) )

def compute_rel_error( x1, x0):
    return np.abs( x1 - x0 )

def is_error_small( error, tol ):
    return np.all( error < tol )

def is_initial_guess_root( F, x, x0, abs_tol ):
    abs_error = compute_abs_error( F, x, x0)
    return is_error_small( abs_error, abs_tol )

def iterate(F, J, x, x0, verbose, iteration = None ):
    x1 = step( F, J, x, x0)
    abs_error = compute_abs_error( F, x, x1)
    rel_error = compute_rel_error( x1, x0)
    if verbose:
            print( f'Iteration { iteration + 1 }; absolute error is { abs_error } ; relative error is { rel_error }' )
    return x1, abs_error, rel_error

def solver( F: sympy.Matrix,
            J: sympy.Matrix,
            x: tuple[sympy.Symbol, ...],
            x0: np.ndarray, max_iter: int = 50,
            rel_tol: float = 1e-9, abs_tol: float = 1e-9,
            verbose: bool = False) -> np.ndarray:
    if is_initial_guess_root( F, x, x0, abs_tol ):
        return x0
    for iteration in range( max_iter ):
        x1, abs_error, rel_error = iterate(F, J, x, x0, verbose, iteration )
        x0 = x1
        if is_error_small( abs_error, abs_tol ) or is_error_small( rel_error, rel_tol ):
            return x1
    raise MaxIterationReached("Maximum iterations reached without finding a root. Try increasing the tolerance, allowing more iterations, or adjusting the initial guess.")
