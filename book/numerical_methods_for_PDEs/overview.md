(NumMethPDE)=
# Numerical Methods for PDEs

% START-CREDIT
% source: numerical_methods_for_PDEs
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Marcel Zijlema. {ref}`Find out more here <numerical_methods_for_pdes_credit>`.
```
% END-CREDIT

In Chapter {ref}`numerical_modelling` ordinary differential equations (ODEs) have been treated.
Their solutions are simply functions of a *single* independent variable representing time.
Frequently, physical systems often evolve not only in time but also in spatial dimensions.
Such systems are described by mathematical equations called the partial differential equations (PDEs). Examples are
the Navier-Stokes equations that describe the motion of fluids, such as water in oceans, rivers and lakes and air around planes and cars,
and the Maxwell's equations describing the propagation of electric and magnetic fields through a medium or vacuum.

It is virtually impossible to solve the PDEs analytically, and one must therefore rely on numerical methods to find an
approximate solution. These methods result in discrete (algebraic) equations which can be solved in a finite sequence
of algebraic operations on a computer.

Various numerical approaches are used to discretize differential equations: finite difference methods,
finite volume methods, finite element methods, spectral methods, etc. The key notions related to these discretization methods are
**consistency** and **stability**. They play an important role in the construction of a suitable (accurate and stable) numerical scheme.

In this chapter, first, a brief review of [**partial differential equations**](./intro_to_pdes.md) is provided.
Next, discretizations of the [**diffusion equation**](./diffusion_equation.ipynb) by employing the **finite difference method** are considered.
This is followed by the approximatons of the [**advection equation**](./advection_equation.md) and finally the
[**advection-diffusion equation**](./advection_diffusion_eq.ipynb).
