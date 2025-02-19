import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import pytest
from hw1 import elasto_plasticity as ep

def test_episotropic():
  E, H, Y0= 1000, 111, 10
  ep_iso = ep.ElastoPlasticIsoHard( E, H, Y0)
  delta_epsilon = 0.001
  epsilon0, sigma0 = 0, 0
  ep_iso.update_step( delta_epsilon, epsilon0, sigma0 )
  known = 1
  found = ep_iso.sigma
  assert np.isclose( known , found ) 

  E, H, Y0= 1000, 111, 10
  ep_iso = ep.ElastoPlasticIsoHard( E, H, Y0)
  delta_epsilon = 0.1
  epsilon0, sigma0 = 0, 0
  ep_iso.update_step( delta_epsilon, epsilon0, sigma0 )
  known = 18.991899189918996
  found = ep_iso.sigma
  assert np.isclose( known , found )

  E, H, Y0= 1000, 111, 10
  ep_iso = ep.ElastoPlasticIsoHard( E, H, Y0)
  epsilon_arr = np.array( [0, 0.001, 0.1] )
  sigma_arr_found = ep_iso.cal_sigma_array( epsilon_arr, 0  )
  sigma_arr_known = np.array( [0, 1, 18.991899189918996] )
  assert np.all( np.isclose( sigma_arr_found , sigma_arr_known ) )

  E, H, Y0= 1000, 111, 10 
  ep_iso = ep.ElastoPlasticIsoHard( E, H, Y0)
  epsilon_arr = np.concatenate( (np.linspace(0, 0.02, 100), np.linspace(0.02, 0, 100), np.linspace(0, -0.02, 100), np.linspace(-0.02, 0, 100), np.linspace(0, 0.04, 200), np.linspace(0.04, 0, 200)))
  sigma0 = 0
  self_path_file = Path(__file__)
  self_path = self_path_file.resolve().parent
  data_path = self_path.joinpath("files").resolve()
  fig_name_with_path = data_path.joinpath("test_plot_funciton_episotropic.png").resolve()
  ep_iso.plot_stress_strain_curve(epsilon_arr, sigma0, fig_name_with_path)
  assert fig_name_with_path.is_file()


def test_kinematic():
  E, H, Y= 1000, 111, 10
  ep_k = ep.ElastoPlasticKinematicHard( E, H, Y)
  delta_epsilon = 0.001
  epsilon0, sigma0 = 0, 0
  ep_k.update_step( delta_epsilon, epsilon0, sigma0 )
  known = 1
  found = ep_k.sigma
  assert np.isclose( known , found ) 

  E, H, Y= 1000, 111, 10
  ep_k = ep.ElastoPlasticKinematicHard( E, H, Y)
  delta_epsilon = 0.1
  epsilon0, sigma0 = 0, 0
  ep_k.update_step( delta_epsilon, epsilon0, sigma0 )
  known = 18.991899189918996
  found = ep_k.sigma
  assert np.isclose( known , found ) 

  E, H, Y= 1000, 111, 10
  ep_k = ep.ElastoPlasticKinematicHard( E, H, Y)
  epsilon_arr = np.array( [0, 0.001, 0.1] )
  sigma_arr_found = ep_k.cal_sigma_array( epsilon_arr, 0  )
  sigma_arr_known = np.array( [0, 1, 18.991899189918996] )
  assert np.all( np.isclose( sigma_arr_found , sigma_arr_known ) )

  E, H, Y= 1000, 111, 10 
  ep_k = ep.ElastoPlasticKinematicHard( E, H, Y)
  epsilon_arr = np.concatenate( (np.linspace(0, 0.02, 100), np.linspace(0.02, 0, 100), np.linspace(0, -0.02, 100), np.linspace(-0.02, 0, 100), np.linspace(0, 0.04, 200), np.linspace(0.04, 0, 200)))
  sigma0 = 0
  self_path_file = Path(__file__)
  self_path = self_path_file.resolve().parent
  data_path = self_path.joinpath("files").resolve()
  fig_name_with_path = data_path.joinpath("test_plot_funciton_kinematic.png").resolve()
  ep_k.plot_stress_strain_curve(epsilon_arr, sigma0, fig_name_with_path)
  assert fig_name_with_path.is_file()

def test_total_strain_plot():
  self_path_file = Path(__file__)
  self_path = self_path_file.resolve().parent
  data_path = self_path.joinpath("files").resolve()
  fig_name_with_path = data_path.joinpath("test_plot_funciton_totalstrain.png").resolve()
  epsilon_arr = np.concatenate( (np.linspace(0, 0.02, 100), np.linspace(0.02, 0, 100), np.linspace(0, -0.02, 100), np.linspace(-0.02, 0, 100), np.linspace(0, 0.04, 200), np.linspace(0.04, 0, 200)))
  ep.plot_total_applied_strain( epsilon_arr, fig_name_with_path )
  assert fig_name_with_path.is_file()
