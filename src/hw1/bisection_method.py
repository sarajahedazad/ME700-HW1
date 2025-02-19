import numpy as np
import math
import matplotlib.pyplot as plt

# types of error to think about
class OutofRangeError(Exception):
    pass

class MaximumIterationError(Exception):
  pass

class BisectionSolver:
  def __init__(self, abs_tol = 10**(-10), rel_tol = 10**(-10), max_iter = 50 , verbose = False):
    self.abs_tol = abs_tol #absolute tolearnce
    self.rel_tol = rel_tol # relative tolerance
    self.max_iter = max_iter # maximum number of iterations
    self.verbose = verbose # whether to print out the debug information at each iteration or not

  def solve( self, function, a: float, b: float )-> float:
    lower_bound, upper_bound = sorted([a, b])

    f_lb = function( lower_bound ) # value of the function at the lower bound
    f_ub = function( upper_bound ) # value of the fucntion at the upper bound

    if f_lb * f_ub > 0 :
      raise OutofRangeError("No root in the provided range or unable to find any. \n Changing the domain boundaries may help.")
    if f_lb == 0 :
      return lower_bound
    if f_ub == 0 :
      return upper_bound

    iter = 1
    if f_lb * f_ub < 0 :
      mid_point = ( lower_bound + upper_bound ) / 2
      f_mid = function( mid_point )
      while np.abs( ( upper_bound - lower_bound ) )> self.rel_tol and np.abs( f_mid ) > self.abs_tol :
        if f_mid * f_ub > 0 :
          upper_bound = mid_point
          f_ub = f_mid
        else:
          lower_bound = mid_point
          f_lb = f_mid

        mid_point = ( lower_bound + upper_bound ) / 2
        f_mid = function( mid_point )

        if self.verbose:
          print(f"Iteration number { iter } completed \n Upper bound: { upper_bound } , lower bound: {lower_bound }, midpoint {mid_point} \n Function (f) value at the upper bound: { f_ub }, f at the lower point {f_lb}, f at the mid point {f_mid} \n")

        iter += 1
        if iter > self.max_iter:
          raise MaximumIterationError("Maximum nummber of iterations reached. \n Changing the values of the default maximum nunmber of iterations or tolerances may help.")
      return (upper_bound + lower_bound) / 2
