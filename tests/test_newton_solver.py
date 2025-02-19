from hw1 import newton_solver as ns
import numpy as np
import pytest
import sympy

def test_newtonsolver():
    n = 1  # Number of variables
    x = sympy.symbols(f'x:{n}')

    F = sympy.Matrix([ x[0]**3- 4 *x[0] ])
    J = F.jacobian(x)
    x0 = np.array([ 6 ])
    
    found = ns.solver( F, J, x, x0, verbose = True)
    known = 2
    assert np.all( np.isclose( known , found ) )

    n = 1 
    x = sympy.symbols(f'x:{n}')

    F = sympy.Matrix([ x[0]**2 - 2 * x[0] + 1 ])
    J = F.jacobian(x)
    x0 = np.array([ 1 ])

    found = ns.solver( F, J, x, x0, verbose = True)
    known = 1
    assert np.all( np.isclose( known , found ) )

    n = 2  
    x = sympy.symbols(f'x:{n}')  
    
    F = sympy.Matrix([x[0]**3- 4 *x[0], x[1]**2- 4 *x[1]])  
    J = F.jacobian(x)
    x0 = np.array([1.5, 2.2])
    
    found = ns.solver( F, J, x, x0, verbose = True)
    known = np.array([2, 4])
    assert np.all( np.isclose( known , found ) )

    n = 1
    x = sympy.symbols(f'x:{n}')

    F = sympy.Matrix([x[0]**2 + 1])
    J = F.jacobian(x)
    x0 = np.array([9]) 

    with pytest.raises(ns.MaxIterationReached):
        ns.solver( F, J, x, x0, max_iter=5)
