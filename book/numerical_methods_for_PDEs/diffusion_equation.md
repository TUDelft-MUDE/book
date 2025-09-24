(diffusion)=
# Diffusion Equation

This section builds on Chapter {ref}`numerical_modelling` and discusses the numerical solution of the 1D diffusion equation.

```{note} 

**The learning objectives of this section are:**
- describe the role of diffusion and identify the diffusion equation
- formulate and discretize the diffusion equation using the finite difference method
- assess various time integration schemes for the diffusion equation

```

## Mathematical model

The (initial) boundary value problem (IBVP) we wish to solve is the following

$$
  \begin{align}
    &\frac{\partial T}{\partial t} = \kappa \frac{\partial^2 T}{\partial x^2}\, , \quad x \in (0,L)\, ,\quad t > 0 \\
    \\
    &T(x,0) = T^0(x)\, ,\quad x \in [0,L] \\
    \\
    &T(0,t) = 1\, ,\quad t > 0 \\
    \\
    &\frac{\partial T}{\partial x} (L,t) = 0\, ,\quad t > 0
  \end{align}
$$ (diffusion1)

and is known as the **heat equation**. This equation describes the flow of heat in a rod with a finite length, made out of some heat-conducting
material, subject to some boundary conditions at each end.
Specifically, this heat *spreads* out spatially as time increases. This phenomenon is called **diffusion**.
The solution to the heat equation is the temperature distribution $T(x,t)$ at any time $t$ and vary with $x$ along the rod.

We assume that $T(x,t)$ is smooth enough, so that we can differentiate this function many times as we want and each derivative is a well-defined *bounded* function (that has thus a fixed upper bound).
Here $L$ is the given finite length of the domain and $T^0(x)$ is a given function defining the initial condition on the temperature.
The coefficient $\kappa > 0$ is the thermal diffusivity. In general, the parameter $\kappa$ is called the **diffusion coefficient** or sometimes the **dispersion** coefficient.

```{tip}

Always check the dimension of parameters that appear in the PDE. For instance, in the given heat equation, the unit of $\kappa$ is m$^2$/s. (Check yourself!)

```

In the above case, we have imposed a Dirichlet boundary condition at $x = 0$ and a Neumann boundary condition at $x = L$.
Since both these boundary conditions are time independent, we expect the solution to eventually reach a **steady state**
solution $T(x,t) \to {\tilde T}(x)$ which then remains essentially unchanged at later times.
Hence, we will marching forward in time until a steady state solution is found. During this marching a **transient** solution will be obtained that must fulfill the initial condition.

:::{card} Exercise

Show that the steady state solution is $\underset{t \to \infty}{\lim} T(x,t) = {\tilde T}(x) = 1, \quad x \in [0,1]$.

```{admonition} Solution
:class: tip, dropdown

To find the stationary solution, the time derivative is set to zero. Hence, we consider the following equation

$$
  \kappa \frac{\partial^2 {\tilde T}}{\partial x^2} = 0
$$

Integrating twice, we obtain the following solution

$$
  {\tilde T}(x) = a\,x + b
$$

where $a$ and $b$ are the constants of integration. Their values can be found by means of the boundary conditions.

First, ${\tilde T}(0) = 1$, so that $b = 1$. Second, $\partial {\tilde T}/\partial x = 0$ at $x = 1$, so that $a = 0$. Hence, the final solution is given by

$$
  {\tilde T}(x) = 1, \quad x \in [0,1]
$$

```
:::

```{note}

The above mathematical model {eq}`diffusion1` is well posed since we found a unique solution that is stable. An example of an <u>ill posed</u> problem would be the one
in which the Dirichlet boundary condition at $x = 0$ is replaced by the following homogeneous Neumann condition:

$$
 \frac{\partial T}{\partial x} (0,t) = 0\, ,\quad t > 0
$$

In that case, the steady state solution would be

$$
  {\tilde T}(x) = b
$$

where $b$ remains undetermined. Hence, this solution is not unique!

```

## Domain discretization

The first step is to **discretize** the domain $[0,L]$ into a finite number of **grid points** $M+1$ where we
intend to compute the solution of the PDE {eq}`diffusion1`. $M$ represents the number of spatial intervals or **grid cells**.
We will use a uniform or **equidistant** grid, with a **grid spacing** $\Delta x = L/M$,
which is the size of each grid cell.

We will refer to one of the points in the grid as $x_m = m\Delta x\,, m=0,\ldots,M$.
The first and last grid points of the domain, $x_0$ and $x_M$, are called the **boundary points** (or in 1D the **end points**),
while the other grid points are the **internal** (or **inner**) points. {numref}`grid` illustrates an example of 1D uniform grid in $x-$space with 5 inner grid points
$x_1, \cdots, x_5$ and 2 boundary points $x_0$ and $x_6$. Also, there are 6 grid cells.

Likewise we discretize the time interval into a number of time steps, separated
by a time increment $\Delta t$, and compute the solution for times $t_n = n\Delta t\,, n=1,2,3,\ldots$ until a steady state is found.
Our aim is to compute the solution of the PDE for all values $T^n_m \approx T(m\Delta x,n\Delta t)$. The function $T^n_m$ is called the **grid function** and consists only of discrete values
defined at grid points $x_m$ and time steps $t_n$. (Keep in mind that $T(x,t)$ is continuous and smooth.)

## Method of lines

We now have a **spatial grid** or **computational domain** that approximates the physical domain $x \in [0,L]$ and a discrete time frame. The next step it to
define approximations to the partial derivatives appearing in the heat equation.

The approach to follow is to carry out the approximation of time derivatives and the approximation of spatial
derivatives separately. Hence, the whole approximation process is done in two steps:

1. Approximate the spatial derivative first. This step is called the **semi discretization** step and leads to a system of first order ODEs.
2. The resulting system of ODEs is approximated by means of time integration. This step has been dealt with in Chapter {ref}`numerical_modelling`.

This two-step process is called the **method of lines** (MOL)[^mol].

[^mol]: The origin of the name <u>method of lines</u> is best illustrated at the following [Wikipedia page](https://en.wikipedia.org/wiki/Method_of_lines#mediaviewer/File:Method\_of\_lines.gif).


A number of methods have been proposed in the field of numerical mathematics to approximate spatial derivatives. Popular methods are the finite difference, finite volume and finite element methods. In this chapter,
we restrict ourselves to the traditional numerical method in hydraulic engineering, namely, the finite difference method.
Another popular method is the finite element method which will be discussed in Chapter {ref}`finite_element_method`.

## Finite difference method

The basic methodology of the **finite difference method** (FDM) is to approximate the spatial derivatives
with **differences** of the unknowns on the grid. A variety of different approximations are possible and the
choice depends on the desired accuracy (consult Chapter {ref}`numerical_modelling` for further clarification).


Recall the definition of the partial derivative:

$$
  \frac{\partial T}{\partial x} (x,t) = \lim_{\Delta x \to 0} \frac{T(x+\Delta x,t) - T(x,t)}{\Delta x}
$$

We do not have the luxury of computing the limit numerically so we must select
a small but finite value for the **mesh width** $\Delta x$ and approximate the derivative as

$$\frac{\partial T}{\partial x} (m\Delta x,t) \approx \frac{T_{m+1}(t) - T_m(t)}{\Delta x}$$ (fdfs)

with $T_m(t) \approx T(m\Delta x,t)$.
Note that the quantity $T_m(t)$ is *continuous* in time as there is no approximation in time yet!
Approximation {eq}`fdfs` is known as the **forward finite difference** scheme. This scheme is also called the **one-sided**
approximation since $T$ is evaluated only at $x_{m+1} > x_m$.

We now quantify the accuracy of the forward difference scheme.
By means of the Taylor series expansion we can derive the truncation error of this approximation. We expand
$T(x+\Delta x,t)$, as follows

$$
\begin{align}
  T(x+\Delta x,t) = & \quad T(x,t) + \Delta x\, T_x(x,t) + \frac 12 \Delta x^2\, T_{xx}(x,t) + \\
                    \\
                    &\quad \frac 16 \Delta x^3\, T_{xxx}(x,t) + \frac{1}{24} \Delta x^4\, T_{xxxx}(x,t) + \ldots
\end{align}
$$

with $T_x = \partial T/\partial x$, $T_{xx} = \partial^2T/\partial x^2$, etc. Here we assume that $T(x,t)$ is sufficiently smooth. Hence, all its derivatives exist.
Substitution gives

$$
\begin{align}
  \frac{T(x+\Delta x,t) - T(x,t)}{\Delta x} &= \frac{1}{\Delta x} \left ( \Delta x \frac{\partial T}{\partial x}(x,t) + \frac 12 \Delta x^2 \frac{\partial^2 T}{\partial x^2} (x,t) + \ldots \right ) \\
                                            \\
                                            &= \frac{\partial T}{\partial x}(x,t) + \frac 12 \Delta x \frac{\partial^2 T}{\partial x^2} (x,t) + \ldots \\
                                            \\
                                            &= \frac{\partial T}{\partial x}(x,t) + \mathcal{O}(\Delta x)
\end{align}
$$

Hence, the forward difference formula is accurate only to order $\Delta x$ and is called the **first order** scheme.

There are, however, two other common possibilities.
The first is the **backward finite difference** scheme

$$\frac{\partial T}{\partial x} (m\Delta x,t) \approx \frac{T_m(t) - T_{m-1}(t)}{\Delta x}$$ (bdfs)

and the second is the **centred finite difference** scheme or **central differences**

$$\frac{\partial T}{\partial x} (m\Delta x,t) \approx \frac{T_{m+1}(t) - T_{m-1}(t)}{2\Delta x}$$ (cdf1)

since this approximation is centred around the point of consideration $x_m$.
Central differences is an example of a **two-sided** approximation and we will see that, for a sufficiently small value of $\Delta x$, this
approximation leads to a more accurate numerical solution of the diffusion equation than a one-sided approximation. This does
not necessarily imply that one-sided approximations are not appropriate. For instance, for *advective* transport,
it may be appropriate to use either the forward or backward scheme. This will be discussed later on.

:::{card} Exercise

Show that the backward and centred finite difference schemes are accurate to $\Delta x$ and $\Delta x^2$, respectively.

```{admonition} Solution
:class: tip, dropdown

See Chapter {ref}`numerical_modelling`.

```
:::

The above central differences is measured using *double* grid size, that is, $2\Delta x$. Alternatively, the partial derivative may
also be approximated as follows

$$\frac{\partial T}{\partial x} (m\Delta x,t) \approx \frac{T_{m+1/2}(t) - T_{m-1/2}(t)}{\Delta x}$$ (cdf2)

which is central differences using *single* grid size. However, the quantities $T_{m\pm1/2}$ are not defined on the grid.
In fact, there locations are in between the grid points and are called **midpoints**.
Hence, they must be computed by means of **linear interpolation**, as follows

$$
  T_{m-1/2} \approx \frac 12 \left ( T_{m-1} + T_m \right )\, , \quad T_{m+1/2} \approx \frac 12 \left ( T_m + T_{m+1} \right )
$$

:::{card} Exercise

By means of the above interpolations, show that Eq. {eq}`cdf2` is equivalent to Eq. {eq}`cdf1`.

```{admonition} Solution
:class: tip, dropdown

By way of substitution of the above linear interpolations into Eq. {eq}`cdf2`, we obtain Eq. {eq}`cdf1`.

```
:::

Chapter {ref}`numerical_modelling` outlined a method to find an approximation for the second derivative. Here, we will follow another approach.
The approximation of the second derivative can be obtained by recalling that

$$
  \frac{\partial^2 T}{\partial x^2} = \frac{\partial}{\partial x} \left ( \frac{\partial T}{\partial x} \right )
$$

Hence,

$$
  \frac{\partial^2 T}{\partial x^2} (m\Delta x,t) \approx \frac{{(\frac{\partial T}{\partial x})}_{m+1/2} - {(\frac{\partial T}{\partial x})}_{m-1/2}}{\Delta x} \approx \frac{\frac{T_{m+1} - T_m}{\Delta x} - \frac{T_m - T_{m-1}}{\Delta x}}{\Delta x} = \frac{T_{m+1}-2T_m+T_{m-1}}{\Delta x^2}
$$

Note again the use of midpoints. Since this approximation is symmetric and centred around point $x_m$ it is referred to as the **central difference scheme** for the second derivative. 

:::{card} Exercise

Show that this central differences is second order accurate.

```{admonition} Solution
:class: tip, dropdown

Note that the grid function $T_m$ represents discrete values at grid points $x_m$, but is still continuous in time, that is, $T_m(t)$.
Furthermore, $T_{m\pm1}(t) \approx T(x\pm\Delta x,t)$ while $T(x,t)$ is sufficiently smooth in $x$. Hence,
we apply the Taylor series expansion to find the expansion of both $T(x+\Delta x,t)$ and $T(x-\Delta x,t)$.
Since we are dealing with the second derivative and we also expect second order accuracy, we will expand them till the fourth order (2+2=4). Hence, we have

$$
\begin{align}
  T(x\pm\Delta x,t) = & \quad T(x,t) \pm \Delta x\, T_x(x,t) + \frac 12 \Delta x^2\, T_{xx}(x,t) \pm \\
                        \\
                      &\quad \frac 16 \Delta x^3\, T_{xxx}(x,t) + \frac{1}{24} \Delta x^4\, T_{xxxx}(x,t)
\end{align}
$$

Plugging these expansions into the approximation yields

$$
\begin{align}
  \frac{T(x+\Delta x,t) - 2T(x,t) + T(x-\Delta x,t)}{\Delta x^2} &= \frac{1}{\Delta x^2} \left ( \Delta x^2 \frac{\partial^2 T}{\partial x^2}(x,t) + \frac{1}{12}\Delta x^4 \frac{\partial^4 T}{\partial x^4} (x,t) \right ) \\
                                            \\
                                            &= \frac{\partial^2 T}{\partial x^2}(x,t) + \frac{1}{12} \Delta x^2 \frac{\partial^2 T}{\partial x^4} (x,t) \\
                                            \\
                                            &= \frac{\partial^2 T}{\partial x^2}(x,t) + \mathcal{O}(\Delta x^2)
\end{align}
$$

which proves second order accuracy.

```
:::

Substituting this second order scheme into our original PDE, Eq. {eq}`diffusion1`, we obtain


$$\frac{dT_m}{dt} = \kappa \, \frac{T_{m+1} - 2T_m + T_{m-1}}{\Delta x^2}\, , \quad m=1,\ldots,M-1$$ (semid)

which is a semi discretization of Eq. {eq}`diffusion1` of the **interior** of the domain. Note that Eq. {eq}`semid` is an <u>ordinary differential equation</u>.

Finally, we need to discretize the boundary conditions. The Dirichlet condition at first boundary point $x_0$ is simply given by

$$
  T_0(t) = 1\, , \quad t > 0
$$

The implementation of the Neumann condition at last boundary point $x_M$ is less trivial. When using the central differences for spatial
derivatives, we often need to consider values of the numerical solution that *lie* outside the computational domain in order to compute spatial derivatives on the boundaries.
The usual approach is to introduce **virtual points** that lie outside the domain and to use both
the Neumann boundary condition and the numerical scheme for the interior domain, to eliminate the values at virtual points.
For example, the centred approximation for the first derivative $\partial T/\partial x$ at boundary $x=L$ is (substitute $m=M$ in Eq. {eq}`cdf1`)

$$
  \frac{\partial T}{\partial x} (L,t) \approx \frac{T_{M+1}(t) - T_{M-1}(t)}{2\Delta x} = 0 \quad \Rightarrow \quad T_{M+1}(t) = T_{M-1}(t)
$$

involving the virtual point $x_{M+1} = L + \Delta x$. We also apply the semi discretization of the heat equation at the boundary point $x_M$ (see Eq. {eq}`semid`),

$$
  \frac{dT_M}{dt} = \kappa \, \frac{T_{M+1}-2T_M+T_{M-1}}{\Delta x^2}
$$

and eliminate $T_{M+1} = T_{M-1}$ from this equation. We are left with the numerical treatment for the
Neumann condition, involving only values of the numerical solution located *within* the domain, namely,

$$
  \frac{dT_M}{dt} = 2\kappa \, \frac{T_{M-1}-T_M}{\Delta x^2}
$$


Summarising, we have the following **semi-discrete** linear system of first order ODEs with the unknowns $T_m(t)\,, m=0,\ldots,M$,

$$
  \begin{align}
    &T_0 = 1\, , \quad t > 0 \\
    \\
    &\frac{dT_m}{dt} = \kappa \, \frac{T_{m+1}-2T_m+T_{m-1}}{\Delta x^2}\, , \quad m=1,\ldots,M-1\, , \quad t > 0 \\
    \\
    &\frac{dT_M}{dt} = 2\kappa \, \frac{T_{M-1}-T_M}{\Delta x^2}\, , \quad t > 0 \\
    \\
    &T_m(0) = T^0(x_m)\, , \quad m=0,\ldots,M
  \end{align}
$$ (modedif1)

It is standard practice to write this linear system in the matrix-vector notation

$$
  \frac{d\vec{T}}{dt} = A\vec{T} + \vec{g}\,,\quad \vec{T}(0) = \vec{T}^0
$$

with

$$
  \vec{T} = \begin{pmatrix} T_1 \\ T_2 \\ T_3 \\ \vdots \\ T_{M-2} \\ T_{M-1} \\ T_M \end{pmatrix}
$$

a vector containing $M$ unknowns,

$$
   A=   \frac{\kappa}{\Delta x^2} \left (
   \begin{array}{rrrrrrrrr} -2       &  1 &  0  &          &        & \cdots &        &        & 0        \\
                             1       & -2 &  1  &          &        &        &        &        &          \\
                             0       &  1 & -2  &  1       &        &        &        &        &          \\
                                     &    &  1  & -2       & 1      &        &        &        &          \\
                             \vdots  &    &     & \ddots   & \ddots & \ddots &        &        & \vdots   \\
                                     &    &     &          &  1     & -2     &  1     &        &          \\
                                     &    &     &          &        &  1     & -2     &  1     &  0       \\
                                     &    &     &          &        &        &  1     & -2     &  1       \\
                             0       &    &     & \cdots   &        &        &  0     &  2     & -2
   \end{array} \right )
$$

an $M \times M$ discretization matrix, and

$$
  \vec{g} = \frac{\kappa}{\Delta x^2} \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}
$$

a vector with $M$ elements. Note that vector $\vec{g}$ is due to the Dirichlet boundary condition.

:::{card} Exercise

Recall the first exercise above. Now, we want to find the steady-state solution by means of the semi-discrete system of ODEs {eq}`modedif1`.
The rod is 1 m long and is divided into five equally spaced cells, so that $\Delta x = 0.2$ m. The grid consists of six points, denoted
$x_0 = 0,\cdots,x_5 = 1$. The Dirichlet boundary condition is still ${\tilde T}(x_0) = 1$ and at $x_5=1$ the homogeneous Neumann boundary condition holds.

Now, write down the system of ODEs as given above for $M=5$ and try to solve this system using the Numpy library, in particular the function `numpy.linalg.solve`.
(See also section on *Boundary-value problems* of Chapter {ref}`numerical_modelling`.)

Repeat the exercise with various values of $\Delta x$ and also $\kappa$. What are your conclusions?

```{admonition} Solution
:class: tip, dropdown

Note that $d\vec{T}/dt = 0$. Now, for the case $M=5$ the system of equations is given by

$$
\begin{pmatrix} -2 & 1 & 0 & 0 & 0 \\ 1 & -2 & 1 & 0 & 0 \\ 0 & 1 & -2 & 1 & 0 \\ 0 & 0 & 1 & -2 & 1 \\ 0 & 0 & 0 & 2 & -2 \end{pmatrix} \, \begin{pmatrix} T_1 \\ T_2 \\ T_3 \\ T_4 \\ T_5 \end{pmatrix} =
\begin{pmatrix} -1 \\ 0 \\ 0 \\ 0 \\ 0 \end{pmatrix}
$$

which can be solved using the Numpy function. The steady-state solution is given by

$$
\begin{pmatrix} T_1 \\ T_2 \\ T_3 \\ T_4 \\ T_5 \end{pmatrix} = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}
$$

Notice that the given system of ODEs is independent of both parameters $\Delta x$ and $\kappa$, because of the fact that $d\vec{T}/dt = 0$.
Hence, the second order accurate scheme represented by the above system {eq}`modedif1` for an arbitrary $M$ provides an exact (constant) solution ${\tilde T} = b$ for the following equation

$$
  \frac{d^2 {\tilde T}}{dx^2} = 0
$$

augmented with the Dirichlet boundary condition at $x=0$ and the homogeneous Neumann condition at $x=L$.

```
:::

## Time integration

The semi discretization of the heat equation leads to a linear system of first order ODEs, {eq}`modedif1`. The next step is to integrate this system over time.
Our choice for time integration would be the explicit Euler scheme, since this is the most simple one.
Application of explicit Euler to Eq. {eq}`modedif1` yields

$$
  \frac{T^{n+1}_m-T^n_m}{\Delta t} = \kappa \, \frac{T^n_{m+1}-2T^n_m+T^n_{m-1}}{\Delta x^2}\, , \quad m=1,\ldots,M-1\, , \quad n =0,1,2,\ldots
$$

with $\Delta t$ the time step and $T^n_m \approx T(m\Delta x,n\Delta t)$ a discrete grid function, which
represents the wanted numerical solution to the heat equation, Eq. {eq}`diffusion1`, at time step $n$ and grid point $m$.
We can re-arrange this equation as follows

$$
  T^{n+1}_m = T^n_m + \frac{\kappa \Delta t}{\Delta x^2} \, \left (T^n_{m+1}-2T^n_m+T^n_{m-1} \right )
$$ (ftcs)

At each *new* time step, the dependent variable $T$ at each interior grid point $x_m$ is computed from values of $T$ at
three grid points, $x_{m-1}$, $x_m$ and $x_{m+1}$, at the *preceding* time step.
This expression defines an **explicit** scheme for solving the heat equation.
Hence, the solution can be found at any time through a sequence of time steps.
This scheme is known as the **FTCS** scheme, which stands for **F**orward in **T**ime, **C**entral in **S**pace, since we have used
the forward approximation in time with explicit Euler and the central differences in space.
