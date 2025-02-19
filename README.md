
[![codecov](https://codecov.io/gh/sarajahedazad/ME700-HW1/graph/badge.svg?token=hH3HwU10J5)](https://codecov.io/gh/sarajahedazad/ME700-HW1)
[![Run Tests](https://github.com/sarajahedazad/ME700-HW1/actions/workflows/test.yml/badge.svg)](https://github.com/sarajahedazad/ME700-HW1/actions/workflows/test.yml)
# ME700-HW1 : Computational Mechanics: Nonlinear Analysis and Software Development

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

For a complete description of the assignment requirements and guidelines, please refer to the attached [assignment_1.pdf](./assignment_1.pdf).

---

## Theory

### Bisection Method

#### Introduction
The bisection method is a fundamental numerical algorithm for locating the root of a continuous function by repeatedly dividing an interval in half. This method leverages the Intermediate Value Theorem by ensuring that  
$$f(a)$$ and  
$$f(b)$$  
have opposite signs.

#### Algorithm Description
1. **Initialization**: Choose two points (a and b) such that  
   $$f(a)$$ and $$f(b)$$ have opposite signs.
2. **Midpoint Calculation**: Compute  
   $$c = \frac{a + b}{2}$$.
3. **Subinterval Selection**: Evaluate  
   $$f(c)$$ and determine whether to retain the interval [a, c] or [c, b] based on the sign.
4. **Iteration**: Continue until the function value is within a pre-defined tolerance or a maximum number of iterations is reached.

#### Requirements & Codes
- **Requirements**: Uses the `numpy` library.
- **Code**: The implementation is provided in `bisection_method.py` along with a Jupyter notebook tutorial (`tutorial.ipynb`) that demonstrates usage with various examples.

#### References
- Lejeune Lab Graduate Course Materials on the Bisection Method  
- Documentation generated with GenAI assistance

---

### Newton’s Method

#### What is Newton’s Method?
Newton’s method (or the Newton–Raphson method) is an iterative technique for finding roots of a function  
$$F(x)=0$$.  
By leveraging the first-order Taylor series expansion, the method updates guesses according to

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

#### References
- Lejeune Lab Graduate Course Materials on Newton’s Method  
- GenAI-assisted documentation and tutorial examples

---

### Elasto‑Plastic Material Models

#### Introduction
Elasto‑plasticity models describe material behavior that exhibits both elastic and permanent (plastic) deformations. In this assignment, two common hardening rules are implemented:
- **Isotropic Hardening**: Where the yield surface expands uniformly.
- **Kinematic Hardening**: Where the yield surface translates in stress space.

#### Hardening Models

##### Isotropic Hardening
- **Concept**: Uniform expansion of the yield surface as plastic deformation accumulates.
- **Mathematical Representation**:  
  
  $$Y = Y_0 + H \varepsilon_p$$  
  
  where $$Y_0$$ is the initial yield stress, $$H$$ is the hardening modulus, and $$\varepsilon_p$$ is the plastic strain.

##### Kinematic Hardening
- **Concept**: Translation of the yield surface, which is important for modeling cyclic loading and capturing the Bauschinger effect.
- **Mathematical Representation**:  

  $$dX = C \, d\varepsilon_p$$  

  where $$X$$ is the back stress and $$C$$ is a kinematic hardening parameter.

##### Comparison

| Feature                      | Isotropic Hardening         | Kinematic Hardening        |
|------------------------------|-----------------------------|----------------------------|
| Yield Surface Change         | Expands uniformly           | Translates (shifts)        |
| Captures Bauschinger Effect? | ❌ No                       | ✅ Yes                     |
| Suitable for Cyclic Loading? | ❌ No                       | ✅ Yes                     |

#### Requirements & Codes
- **Requirements**: Uses `numpy`, `matplotlib`, and `pytest` for testing.
- **Code**: The implementation is split into modules (e.g., `elasto_plastic_iso.py` and `elasto_plastic_kin.py` within the src/hw1 directory) along with a Jupyter notebook tutorial (`tutorial_elastoplasticity.ipynb`).

#### Installation & Testing
Installation instructions (using conda or mamba) are provided to create an environment, install the package in editable mode, and run tests using pytest. Detailed instructions are available in the original readme sections for elastoplasticity and Newton’s method.

#### References
- Lejeune Lab Graduate Course Materials for setup and testing instructions  
- Additional literature on plasticity theory and computational inelasticity

---

## Installation and Environment Setup

All the code for this assignment is now consolidated in the **src/hw1** directory.

### Environment Setup (Using Conda)
1. **Create the Environment:**
   ```bash
   conda create --name hw1-env python=3.12
