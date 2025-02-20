
[![codecov](https://codecov.io/gh/sarajahedazad/ME700-HW1/graph/badge.svg?token=hH3HwU10J5)](https://codecov.io/gh/sarajahedazad/ME700-HW1)
[![Run Tests](https://github.com/sarajahedazad/ME700-HW1/actions/workflows/test.yml/badge.svg)](https://github.com/sarajahedazad/ME700-HW1/actions/workflows/test.yml)
# Computational Mechanics: Nonlinear Analysis and Software Development - HW1

This repository contains the implementations for Assignment #1 of ME700: Advanced Topics in Mechanical Engineering. The assignment covers two numerical methods/solvers and a material model:
- **Bisection Method Solver**
- **Newton’s Method Solver**
- **1D Elasto‑Plastic Material Models** (with isotropic and kinematic hardening)

The repository’s primary codes are located in **src/hw1**.

---

## Table of Contents

- [Course Information](#course-information)
- [Assignment Overview](#assignment-overview)
- [Theory](#theory)
  - [Bisection Method](#bisection-method)
  - [Newton’s Method](#newtons-method)
  - [Elasto‑Plastic Material Models](#elasto-plastic-material-models)
- [Installation and Environment Setup](#installation-and-environment-setup)
- [Tutorials and Testing](#tutorials-and-testing)
- [References](#references)

---

## Course Information

**ME700 – Advanced Topics in Mechanical Engineering**  
This course is offered at Boston University and, for Spring 2025, will be taught by Dr. Lejeune under the specific topic:  
**Computational Mechanics: Nonlinear Analysis and Software Development**.  
Each semester, the course may cover different topics, and the assignments are designed to blend theoretical insights with practical coding and testing practices.

---

## Assignment Overview

**Assignment #1: Introduction to Nonlinear Equations**  
This assignment requires the development of:
- A **bisection method solver** (with clear documentation, TDD, and error handling).
- A **Newton’s method solver** (again emphasizing good coding practices and comprehensive tutorials).
- **Elasto‑plastic material models** implementing both isotropic and kinematic hardening rules, along with associated tutorials.


---

## Theory

### Bisection Method

#### Introduction
The bisection method is a fundamental numerical algorithm for locating the root of a continuous function by repeatedly dividing an interval in half. This method leverages the Intermediate Value Theorem by ensuring that $$f(a)$$ and $$f(b)$$ have opposite signs.

#### Algorithm Description
1. **Initialization**: Choose two points (a and b) such that $$f(a)$$ and $$f(b)$$ have opposite signs.
2. **Midpoint Calculation**: Compute $$c = \frac{a + b}{2}$$.
3. **Subinterval Selection**: Evaluate $$f(c)$$ and determine whether to retain the interval [a, c] or [c, b] based on the sign.
4. **Iteration**: Continue until the function value is within a pre-defined tolerance or a maximum number of iterations is reached.

#### Requirements & Codes
- **Requirements**: Uses the `numpy` library.
- **Code**: The implementation is provided in `bisection_method.py` along with a Jupyter notebook tutorial (`tutorial_bisectionmethod.ipynb`) that demonstrates usage with various examples.

---

### Newton’s Method

#### What is Newton’s Method?
Newton’s method (or the Newton–Raphson method) is an iterative technique for finding roots of a function $$F(x)=0$$.  
By leveraging the first-order Taylor series expansion, the method updates guesses according to:

$$
x_{k+1} = x_k - \frac{F(x_k)}{F'(x_k)}
$$

For multivariable systems, the method uses the Jacobian matrix:

$$
x_{k+1} = x_k - J(x_k)^{-1} F(x_k)
$$

#### Key Features
- **Rapid convergence** (quadratic near the root) given a good initial guess.
- **Stopping criteria**: based on maximum iterations, absolute tolerance, or relative tolerance.
- **Usage**: The primary function is `solve` in `newton_solver.py`, and detailed examples are provided in the accompanying tutorial.

#### Requirements & Codes
- **Requirements**: Requires the `numpy` and `sympy` libraries.
- **Code**: The main functions reside in `newton_solver.py` (in the src/hw1 directory) with detailed usage examples provided in `tutorial_newton_solver.ipynb`.

---

### Elasto‑Plastic Material Models

#### Introduction
Elasto‑plasticity models describe material behavior that exhibits both elastic and permanent (plastic) deformations. In this assignment, two common hardening rules are implemented:
- **Isotropic Hardening**: Where the yield surface expands uniformly.
- **Kinematic Hardening**: Where the yield surface translates in stress space.

#### Hardening Models

##### Isotropic Hardening
- **Concept**: Uniform expansion of the yield surface as plastic deformation accumulates.
- **Evolution**:  
  - $\phi_{\text{trial}} = |\sigma_{\text{trial}}| - Y$
  - $\Delta \epsilon_p = \frac{\phi_{\text{trial}}}{E + H}$
  - $\epsilon_{p_{n+1}} = \epsilon_{p_n} + \Delta \epsilon_p$
  - $Y_{n+1} = Y + H \Delta \epsilon_p$


##### Kinematic Hardening
- **Concept**: In kinematic hardening, the yield surface shifts in stress space via the backstress ($\alpha$).   
- **Evolution**:  
  - $\phi_{\text{trial}} = |\sigma_{\text{trial}} - \alpha| - Y$
  - $\Delta \epsilon_p = \frac{\phi_{\text{trial}}}{E + H}$
  - $\epsilon_{p_{n+1}} = \epsilon_{p_n} + \Delta \epsilon_p$
  - $\alpha_{n+1} = \alpha_n + H \Delta \epsilon_p$


#### Requirements & Codes
- **Requirements**: Uses `numpy` and `matplotlib`.
- **Code**: The implementation is modules `elasto_plasticity.py` within the src/hw1 directory along with a Jupyter notebook tutorial (`tutorial_elastoplasticity.ipynb`).

---

### Conda environment, install, and testing <a name="install"></a>
_This section is copied and pasted from [Lejeune's Lab Graduate Course Materials: Bisection Method](https://github.com/Lejeune-Lab-Graduate-Course-Materials/bisection-method.git)_

To install this package, please begin by setting up a conda environment (mamba also works):
```bash
conda create --name hw1-env python=3.12
```
Once the environment has been created, activate it:

```bash
conda activate hw1-env
```
Double check that python is version 3.12 in the environment:
```bash
python --version
```
Ensure that pip is using the most up to date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```
Create an editable install of the bisection method code (note: you must be in the correct directory):
```bash
pip install -e .
```
Test that the code is working with pytest:
```bash
pytest -v --cov=hw1 --cov-report term-missing
```
Code coverage should be 100%. Now you are prepared to write your own code based on this method and/or run the tutorial. 


If you are using VSCode to run this code, don't forget to set VSCode virtual environment to hw1-env.

If you would like the open one of the tutorials located in the `tutorials` folder ( for example, `tutorial_elastoplasticity.ipynb`) as a Jupyter notebook in the browser, you might need to install Jupyter notebook in your conda environment as well:
```bash
pip install jupyter
```
```bash
cd tutorials/
```
```bash
jupyter notebook tutorial_elastoplasticity.ipynb
```
### An alternative way to test the codes without installing the package <a name="alter"></a>  
elow is an example that demonstrates how to use `elasto_plasticity.py` without installation. Similarly, you can employ `bisection_method.py` and `newton_solver.py`.
- Step 1: Download the `elasto_plasity.py` file from the folder `src/hw1`([here](https://github.com/sarajahedazad/ME700-HW1/tree/main/src/hw1)). Place it in the same folder as your working directory.
- Step 2: Create a python file in that folder and write your example in that file. You can import the `elastoplasticity` with the following line:
`import elasto_plasticity as ep`
- Step 3: Run your code an enjoy!
Here is an example that demonstrates how you can test `elasto_plasticity.py` file (it should be in the same folder as the python file that you intend to run):

```
import numpy as np
import elasto_plasticity as ep

E, H, Y= 1000, 111, 10
Y0 = Y
ep_iso = ep.ElastoPlasticIsoHard( E, H, Y0)
ep_k = ep.ElastoPlasticKinematicHard( E, H, Y)
sigma0 = 0
epsilon_arr = np.concatenate( (np.linspace(0, 0.02, 100), np.linspace(0.02, 0, 100), np.linspace(0, -0.02, 100), np.linspace(-0.02, 0, 100), np.linspace(0, 0.04, 200), np.linspace(0.04, 0, 200)))

ep.plot_total_applied_strain( epsilon_arr )
ep_iso.plot_stress_strain_curve(epsilon_arr, sigma0)
ep_k.plot_stress_strain_curve(epsilon_arr, sigma0)
```

### References
* [Lejeune Lab Graduate Course Materials: Bisection-Method](https://github.com/Lejeune-Lab-Graduate-Course-Materials/bisection-method/tree/main) 
* ChatGPT: was used for completing the documentation. More details about the AI use is provided in the `assignment_1_genAIuse.txt`.

   
References used by ChatGPT:
- J. Lubliner, *Plasticity Theory*, 2006.
- T. Belytschko, *Nonlinear Finite Elements for Continua and Structures*, 2014.
- Simo & Hughes, *Computational Inelasticity*, 1998.
