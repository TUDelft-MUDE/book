# Introduction to PDEs

A partial differential equation (PDE) permits one to describe solutions that depend
on more than one independent variable. Often these independent variables are time and
one or more spatial dimensions or, in **steady state** problems, two or more spatial
dimensions only.

This section is not intended to be a complete treatment of partial differential equations.
Instead, its aim is to serve as an introduction to a minimal amount of terminology from the field of PDEs.

## Examples of PDEs

Partial differential equations arise in many areas of physics and engineering.
On physical grounds, the form of these equations will involve the time rate-of-change of the solution
and/or the spatial rate-of-change (or gradient) of the solution.
Some examples are:

**Diffusion equation**: $\qquad \frac{\partial T}{\partial t} = \kappa \frac{\partial^2 T}{\partial x^2}$

where $t$ is time, $x$ is the coordinate in space, $T(x,t)$ is the temperature, and $\kappa$ is a thermal diffusivity coefficient.

**Advection equation**: $\qquad \frac{\partial c}{\partial t} + u \frac{\partial c}{\partial x} = 0$

where $c(x,t)$ is the concentration, and $u$ is a constant propagation velocity.

**Wave equation**: $\qquad \frac{\partial^2 c}{\partial t^2} - u^2 \frac{\partial^2 c}{\partial x^2} = 0$

**Laplace equation**: $\qquad \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} = 0$

where $\phi(x,y)$ is a potential or harmonic function.

**Poisson equation**: $\qquad \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} = f$

with $f(x,y,t)$ a source term.

**Burgers equation**: $\qquad \frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} = \nu \frac{\partial^2 u}{\partial x^2}$

with $u(x,t)$ the flow velocity and $\nu$ the (molecular) viscosity.

**Shallow water equations**: $\qquad \frac{\partial \zeta}{\partial t} + \frac{\partial hu}{\partial x} = 0, \quad \frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + g\frac{\partial \zeta}{\partial x} + c_f \frac{u|u|}{h} = 0$

with $\zeta(x,t)$ the water level above the still water level, $h(x,t)=\zeta(x,t)+d(x)$
the water depth, $d(x)$ the bottom level measured from the still water level positively downwards, $u(x,t)$ the flow velocity,
$c_f$ the dimensionless bottom friction coefficient, and $g$ the acceleration of gravity.

In addition to the partial differential equations, some boundary conditions and initial data must be provided to
uniquely specify a solution. Solving the equations means finding the **dependent** variable or variables,
e.g. $T$, $u$, $\zeta$, $\phi$, $c$, as function of the **independent** variables, e.g. $t$, $x$, $y$, such that they fulfill the PDEs
and the boundary conditions are satisfied. This is called the **boundary value problem**.

## Relevant notions on PDEs

Let $u$ be the dependent variable.
A shorthand notation to represent a general PDE is

$$
  \mathcal{L}(u) = g
$$

and $\mathcal{L}$ is called the **differential operator**. The right-hand side $g$ is not a function of $u$.
If $g \equiv 0$ then the PDE is called **homogeneous**, otherwise it is **nonhomogeneous**.
Example: the Laplace equation is homogeneous and the Poisson equation is nonhomogeneous.


The **order** of a PDE is the order of highest derivative that appears in the equation. Example: the order of the advection equation is one, whereas that of the wave equation is two.
The **dimension** of a PDE is the dimension of the spatial domain. Example: the diffusion equation is one dimensional (1D), while the Poisson equation is two dimensional (2D).


A differential operator $\mathcal{L}$ is called **linear** if and only if the following hold

1. $\mathcal{L}(u+v) = \mathcal{L}(u) + \mathcal{L}(v)$

2. $\mathcal{L}(\alpha u) = \alpha \mathcal{L}(u)$

with $\alpha$ a constant. An operator that is not linear is called **nonlinear**. Example of a nonlinear PDE is the Burgers equation.
Do not confuse non-constant or variable-coefficient PDEs with nonlinear PDEs. For example

$$
  \frac{\partial u}{\partial t} = \frac{\partial ^2u}{\partial x^2} + \sin^2(x) \text{ } u
$$

is linear, but with non-constant coefficient, while

$$
  \frac{\partial u}{\partial t} = \frac{\partial ^2u}{\partial x^2} + u\frac{\partial u}{\partial x}
$$

is nonlinear.


The distinguishing of PDEs into linear and nonlinear is an important issue. Solutions of linear
equations **superimpose**. Assume $u$ and $v$ are both solutions of a given linear
PDE. Then all linear combinations of these two solutions, $\alpha u + \beta v$, are also
solutions of the PDE, where $\alpha$ and $\beta$ are constant coefficients. This is a very important
advantage for solving linear PDEs. If we are able to find a set of particular solutions of
the PDE, we can construct all other solutions as linear combinations of these.
Nonlinear PDEs do not share this property of superposition and are usually much
harder to solve and the solutions more difficult to analyze. It is common in mathematical
modelling to attempt to approximate a nonlinear phenomenon in nature with a linear
model. (An example can be found in *to be filled in*.)
While this linear model provides insight into the nature of the phenomenon, often
it is insufficient to describe some of the important aspects and one must introduce
nonlinear terms to the model. Usually nonlinear PDEs cannot be solved by hand, so
numerical methods must be devised. In this chapter, however, we shall largely ignore nonlinear equations.

:::{card} Exercise

Consider the above 1D shallow water equations. Verify that these equations are first order, nonlinear and homogeneous.

```{admonition} Solution
:class: tip, dropdown

The shallow water equations are given by

$$\frac{\partial \zeta}{\partial t} + \frac{\partial hu}{\partial x} = 0$$

and

$$\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} + g\frac{\partial \zeta}{\partial x} + c_f \frac{u|u|}{h} = 0$$

The first equation is derived from the mass conservation and is known as the **continuity equation**. This equation contains first order derivatives only while the second term contains a product of $h$ and $u$,
implying a nonlinear term. Also this equation does not contain a term independent of $\zeta$ and $u$, hence this equation is considered homogeneous.

The second equation is derived from the conservation of momentum and is referred to as the **momentum** equation. Like the continuity equation, this momentum equation is first order, nonlinear and homogeneous as well.
```
:::

## Well posed problems

In the previous sections we saw some examples of PDEs.
We now consider some important issues regarding the **solvability** of PDE problems.
In general, a PDE alone, without any boundary or initial conditions, will either have an infinity of solutions, or have no solution.
Thus, in formulating a boundary value problem there are at least three ingredients:

1. The equation itself.
2. The enclosed spatial domain $\Omega$ on which the PDE is required to be satisfied.
3. The boundary conditions that the solution must to be met at the boundaries of $\Omega$.
4. In case of a time-dependent problem, initial condition(s) must be included as well.

For a PDE based mathematical model of a physical system to give *useful* results, it is generally necessary to formulate that model as a **well posed** problem.
A PDE problem is said to be well posed if

* a solution to the problem **exists**,
* the solution is **unique**, and
* the solution depends **continuously** on the problem data[^wp3]. This is closely related to the notion of **stability** of the PDE.

[^wp3]: The problem data consists of the coefficients in the PDE, the boundary and initial conditions and the domain on which the PDE is required to hold.


If one of these conditions is not satisfied, the PDE problem is said to be **ill posed**.
In practice, the question of whether a PDE problem is well posed can be difficult to settle. Roughly speaking the following guidelines apply.

* The boundary conditions imposed must not be too many or a solution will not exist.
* The boundary conditions imposed must not be too few or the solution will not be unique.
* The kind of boundary conditions must be correctly matched to the type of the PDE or the solution will not be stable.

In this chapter, only well posed problems will be considered.

## Types of boundary conditions

Since the domain $\Omega$ is *finite*, boundary conditions are thus required and represent the influence of the outside world.
Different types of boundary conditions can be applied on the boundary of $\Omega$. The most common occurring
in practice are **Dirichlet**, **Neumann** and **Robin** conditions.

Physically speaking, a Dirichlet condition usually corresponds to setting the value,
a Neumann condition usually specifies a flux condition on the boundary, and a Robin condition typically represents a radiation condition.

Mathematically speaking, they are given as follows.
Dirichlet condition provides a function of time, $g(t)$, as
the constraint on the solution at a specific boundary point $\vec{x}_b$,

$$ u(\vec{x}_b,t) = g(t)$$

In the case of Neumann condition the flux of $u$ normal to the boundary is specified
by a given function $g(t)$ at a boundary point $\vec{x}_b$,

$$ \frac{\partial u}{\partial \vec{n}} (\vec{x}_b,t) = g(t)$$

with $\vec{n}$ the normal to the boundary. If $g(t)$ = 0 then we say that the boundary is **insulated**: $u$ cannot flow across the
boundary.

The Robin condition is a combination of Dirichlet and Neumann conditions,

$$ \alpha u(\vec{x}_b,t) + \beta \frac{\partial u}{\partial \vec{n}}(\vec{x}_b,t) = g(t)$$

where $\alpha$ and $\beta$ may in general depend on position along the boundary.


As with PDEs, boundary conditions can be classified into linear or nonlinear and homogeneous or
nonhomogeneous. The above are linear. They are homogeneous if $g(t) \equiv 0$ and nonhomogeneous otherwise.

## Classification of PDEs

We classify ODEs in terms of their order and whether they are linear or nonlinear. PDEs
are more difficult to classify, because of the greater variety of basic forms
the PDE may take. Not only are the order and linearity important, but also
the PDE formulation. It is the PDE formulation that dictates what types of boundary
conditions can be imposed and ultimately what types of physical processes the
PDE describes.


A classification is possible for
second order, linear PDEs in two independent variables. Any such 2D equation can be written as

$$a\frac{\partial^2 u}{\partial x^2} + 2b \frac{\partial^2u}{\partial x \partial y} + c\frac{\partial^2 u}{\partial y^2} + d\frac{\partial u}{\partial x} +e\frac{\partial u}{\partial y} + fu + g = 0$$ (pde2)

where the coefficients $a$, $b$, $c$ etc. may depend on $(x,y)$.
One of the independent variables may represent time~$t$, which we then have a 1D equation.
The classification of Eq. {eq}`pde2` is based upon the first three terms. It
can be classified into three types according to the sign of the discriminant $b^2 - 4ac$,

* $b^2 - 4ac < 0$: elliptic
* $b^2 - 4ac = 0$: parabolic
* $b^2 - 4ac > 0$: hyperbolic

Generally, different numerical methods are required for the different classes of PDEs. The need for
this specialization in numerical approach is rooted in the physics from which the different classes of PDEs arise.
The physical problem has certain properties that we would like to preserve with our numerical approximation, and it is
important to understand the underlying problem and be aware of its mathematical properties before blindly applying a numerical method.


Elliptic equations generally arise from a physical problem that involves a diffusion process that has reached equilibrium,
a steady state temperature distribution, for example.
Hyperbolic equations are able to support solutions with discontinuities, for example a shock wave.
Hyperbolic PDEs usually arise in wave propagation and advection driven transport problems.
Mathematically, parabolic PDEs serve as a transition from the hyperbolic PDEs to the elliptic PDEs. Physically, parabolic PDEs tend to arise in
time dependent diffusion problems, such as the transient flow of heat in accordance with Fick's law of heat conduction.


It turns out that all elliptic equations are steady state, all parabolic equations are diffusion-like, and all hyperbolic equations are
wave-like. Therefore, we outline the following **prototypes**.


**Elliptic**


Prototype is the Laplace equation

$$
  \frac{\partial ^2u}{\partial x^2} + \frac{\partial ^2u}{\partial y^2} = 0
$$

Elliptic equations do not depend upon time, but rather only spatial variables.
The boundary conditions are usually of the type Dirichlet or Neumann.


**Parabolic**


Prototype is the diffusion equation

$$
  \frac{\partial u}{\partial t} = \frac{\partial ^2u}{\partial x^2}
$$

Here, the independent variable $y$ of the general PDE, Eq. {eq}`pde2`, is time.
An initial condition is thus necessary.
The problem is only well posed in the forward time direction (otherwise the solution becomes unstable in the backward time direction).
$\Omega$ is bounded at two sides in the $x-$direction.
Any boundary conditions, Dirichlet, Neumann and Robin, though in certain combinations, are appropriate at both sides of $\Omega$. (See also Exercise \ref{opg:illpos}.)


**Hyperbolic**


Prototype is the wave equation

$$
  \frac{\partial ^2u}{\partial t^2} - \frac{\partial ^2u}{\partial x^2} = 0
$$

or the advection equation

$$
  \frac{\partial u}{\partial t} + \frac{\partial u}{\partial x} = 0
$$

Here, $y$ variable is again time. An initial condition is necessary.
The problem is well posed in both direction of time.
Boundary conditions of the Dirichlet type
are imposed at boundaries with ingoing characteristics.
Note that the advection
equation is a first order PDE and hence cannot be classified in the above sense.

:::{card} Exercise

Show that the wave equation and the advection equation are mathematically equivalent.

```{admonition} Solution
:class: tip, dropdown

Consider the advection equation

$$
  \frac{\partial u{\partial t} + \frac{\partial u{\partial x} = 0
$$

First, we take the time derivative of this equation, which yields

$$
  \frac{\partial^2 u{\partial t^2} + \frac{\partial^2 u{\partial t \partial x} = 0
$$

Next, we also take the derivative to $x$ of the advection equation giving

$$
  \frac{\partial^2 u{\partial x \partial t} + \frac{\partial^2 u{\partial x^2} = 0
$$

Finally, we substract the last equation from the second to last one in order to get the wave equation

$$
  \frac{\partial ^2u{\partial t^2} - \frac{\partial ^2u{\partial x^2} = 0
$$

```
:::


Important differences between the three prototypes are:

* The Laplace equation is not time dependent. The advection equation is valid in both directions in time. The diffusion equation is well posed only in forward time direction.
* Information is propagated at *finite speed* without changing its shape in the advection equation.
  For the diffusion equation information is transmitted at *infinite speed* but it is also *dissipated* and thus the shape of the solution becomes more smooth as time proceeds.
* The Laplace equation is fundamentally different from the diffusion and advection equation in that
  the solution at each point depends on all other points. Solutions, e.g. potential fields, cannot be found by marching in from the boundary.
  Instead, solutions must be found at all points *simultaneously*.

Since both diffusion and advection equations are typically time dependent, the associated numerical approach is therefore time marching: the numerical solution is determined
at any time through a sequence of time steps.
On the other hand, the solution method for the Laplace equation is typically **iterative** of nature: the solution in each point in the domain is **updated** a number of times by taking
into account the surrounding points until an acceptable error tolerance is reached.


It is not possible to give a meaningful classification for PDEs in more than two independent variables.
However, there are natural extensions for the three prototype equations such as


3D Laplace equation: $\qquad \frac{\partial ^2u}{\partial x^2} + \frac{\partial ^2u}{\partial y^2} + \frac{\partial ^2u}{\partial z^2} = 0$

2D diffusion equation: $\qquad \frac{\partial u}{\partial t} = \frac{\partial ^2u}{\partial x^2} + \frac{\partial ^2u}{\partial y^2}$

2D advection equation: $\qquad \frac{\partial u}{\partial t} + \frac{\partial u}{\partial x} + \frac{\partial u}{\partial y} = 0$


Diffusion and advection equations exist also in three space dimensions.


Later in this lecture notes, we shall deal with free surface flows, such as occurring in seas, estuaries, lakes, rivers and canals. The underlying equations to describe such flows are
the shallow water equations. These equations are a set of *hyperbolic* partial differential equations that describe the flow below a free surface.
Not only flow but also *advective* transport of dissolve substances and their *diffusive* processes in open water bodies will be discussed.
For these reasons, we shall focus on the numerical solution of the diffusion equation (Section~\ref{sec:diffusion}), the advection equation (Section~\ref{sec:advection}) and
the advection-diffusion equation (Section~\ref{sec:cveq}).
Though elliptic equations are very important in the field of computational fluid dynamics (CFD), they will not dealt with here. Detailed discussion on the numerical solution of elliptic equations
may be found in Abbott and Basco (1989), Ferziger and Peri\'{c} (1996), Fletcher (1988) and Wesseling (2001).
