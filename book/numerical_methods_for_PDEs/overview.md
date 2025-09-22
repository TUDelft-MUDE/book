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
Such systems are described by mathematical equations called the partial differential equations. Examples are
the Navier-Stokes equations that describe the motion of fluids, such as water and air, and the Maxwell's equations
describing the behaviour of electric and magnetic fields.

It is virtually impossible to solve the PDEs analytically, and one must therefore rely on numerical methods to find an
approximate solution. These methods result in a discrete (algebraic) equations which can be solved in a finite sequence
of algebraic operations on a computer.

Various numerical approaches are used to discretize differential equations: finite difference methods,
finite volume methods, finite element methods, spectral methods, etc. The key notions related to these discretization methods are
**consistency** and **stability**. They play an important role for the construction of a suitable (accurate and stable) numerical scheme.

In this chapter, first, a brief review of **partial differential equations** (PDEs) is provided. Next, discretizations of the **diffusion
equation** by employing the **finite difference method** are considered. This is followed by the approximatons of the **advection
equation** and the **advection-diffusion equation**.
