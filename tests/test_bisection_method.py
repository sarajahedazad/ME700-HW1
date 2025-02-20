import numpy as np
import pytest
from hw1 import bisection_method as bm

def test_bisection_method():
  def func_example(x):
    return x**3 - 4 * x
  abs_tol = 10**(-10)
  rel_tol = 10**(-10)
  max_iter = 50
  verbose = False
  
  a = 1
  b = 4
  known_answer = 2
  
  solver = bm.BisectionSolver(abs_tol = abs_tol, rel_tol = rel_tol, max_iter = max_iter, verbose = verbose)
  calculated_answer = solver.solve( func_example, a, b )

  assert np.isclose( known_answer , calculated_answer )

def test_samesign_error():
  def func_example(x):
      return x**3 - 4 * x
  abs_tol = 10**(-10)
  rel_tol = 10**(-10)
  max_iter = 50
  verbose = False
  a = 4
  b = 5
  solver = bm.BisectionSolver(abs_tol = abs_tol, rel_tol = rel_tol, max_iter = max_iter, verbose = verbose)
  with pytest.raises(bm.OutofRangeError):
      solver.solve( func_example, a, b )

def test_max_iter():
  def func_example(x):
    return x**3 - 4 *x
    abs_tol = 10**(-10)
  rel_tol = 10**(-10)
  max_iter = 10
  verbose = False
  a = -100
  b = 5
  solver = bm.BisectionSolver(abs_tol = abs_tol, rel_tol = rel_tol, max_iter = max_iter, verbose = verbose)
  with pytest.raises(bm.MaximumIterationError):
      solver.solve( func_example, a, b )

