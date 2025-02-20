import numpy as np
import pytest
from hw1 import bisection_method as bm
import math

def test_bisection_method():
  def func_example(x):
    return x**3 - 4 * x
  abs_tol = 10**(-10)
  rel_tol = 10**(-10)
  max_iter = 50
  verbose = True
  
  a = 1
  b = 4
  known_answer = 2
  
  solver = bm.BisectionSolver(abs_tol = abs_tol, rel_tol = rel_tol, max_iter = max_iter, verbose = verbose)
  calculated_answer = solver.solve( func_example, a, b )

  assert np.isclose( known_answer , calculated_answer )

  def func_example(x):
    return math.log(x+8)
  abs_tol = 10**(-10)
  rel_tol = 10**(-10)
  max_iter = 50
  verbose = True
  
  a = -7
  b = 2
  known_answer = -7
  
  solver = bm.BisectionSolver(abs_tol = abs_tol, rel_tol = rel_tol, max_iter = max_iter, verbose = verbose)
  calculated_answer = solver.solve( func_example, a, b )

  assert np.isclose( known_answer , calculated_answer )

  def func_example(x):
    return x**3 - x**2 + x - 1
  abs_tol = 10**(-10)
  rel_tol = 10**(-10)
  max_iter = 50
  verbose = True
  
  a = -5
  b = 1
  known_answer = 1
  
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

def test_max_iter_error():
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

