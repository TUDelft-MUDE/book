(diffusion)=
# Diffusion Equation

This section builds on Chapter {ref}`numerical_modelling` and discusses the numerical solution of the 1D diffusion equation.

```{note} 

**The learning objectives of this section are:**
- describe the role of diffusion and identify the diffusion equation
- formulate and discretize the diffusion equation using the finite difference method
- compute the truncation error for a given numerical scheme
- explain the notions of consistency and convergence
- explain the notion of stability
- derive the stability condition for a conditionally stable scheme

```

## Mathematical model

The (initial) boundary value problem (IBVP) we wish to solve is the following

$$
  \begin{align}
    &\frac{\partial T}{\partial t} = \kappa \frac{\partial^2 T}{\partial x^2}\, , \quad x \in (0,L)\, ,\quad t > 0 \\
    \\
    &T(x,0) = T^0(x) > 0\, ,\quad x \in [0,L] \\
    \\
    &T(0,t) = 1\, ,\quad t > 0 \\
    \\
    &\frac{\partial T}{\partial x} (L,t) = 0\, ,\quad t > 0
  \end{align}
$$ (diffusion1)

The diffusion equation is also known as the **heat equation**. This equation describes the flow of heat in a rod with a finite length, made out of some heat-conducting
material, subject to some boundary conditions at each end.
Specifically, this heat *spreads* out spatially as time increases. This phenomenon is called **diffusion**.
The solution to the heat equation is the temperature distribution $T(x,t)$ at any time $t$ and vary with $x$ along the rod.

We assume that $T(x,t)$ is smooth enough, so that we can differentiate this function many times as we want and each derivative is a well-defined *bounded* function (that has thus a fixed upper bound).
Here $L$ is the given finite length of the domain and $T^0(x) > 0$ is a given function defining the initial condition on the temperature.
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

First, ${\tilde T}(0) = 1$, so that $b = 1$. Second, $\partial {\tilde T}/\partial x = 0$ at $x = 1$, so that $a = 0$. Hence, the steady state solution is given by

$$
  {\tilde T}(x) = 1, \quad x \in [0,1]
$$

```
:::

```{admonition} Well posedness
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
The MOL approach has a great flexibility for constructing a numerical scheme in the sense that the choice of spatial discretization and the choice of time integration
are independent from each other.

[^mol]: The origin of the name <u>method of lines</u> is best illustrated at the following [Wikipedia page](https://en.wikipedia.org/wiki/Method_of_lines#mediaviewer/File:Method\_of\_lines.gif).


A number of methods have been proposed in the field of numerical mathematics for spatial discretization. Popular methods are the finite difference, finite volume and finite element methods. In this chapter,
we restrict ourselves to the traditional numerical method in hydraulic engineering, namely, the finite difference method.
Another popular method is the finite element method which will be discussed in Chapter {ref}`Finite Element Method <finite_element_method>`.

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
it may be appropriate to use either the forward or backward scheme. This will be discussed in Section {ref}`advection`.

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
In fact, their locations $x_{m\pm1/2}$ are in between the grid points and are called **midpoints**.
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

Show that this central difference approximation is second order accurate.

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
$$ (discmat1)

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
$$ (matrdiff2)

an $M \times M$ discretization matrix, and

$$
  \vec{g} = \frac{\kappa}{\Delta x^2} \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}
$$

a vector with $M$ elements. Note that vector $\vec{g}$ is due to the Dirichlet boundary condition.

```{admonition} Symmetric matrix
:class: dropdown
You may have noticed that, apart from the last row and the last column, the discretization matrix is **symmetric**, that is, $A = A^T$.
It is possible to make this matrix completely symmetric.
Recall the discretization of the homogeneous Neumann condition

$$
  \frac{dT_M}{dt} = 2\kappa \, \frac{T_{M-1}-T_M}{\Delta x^2}
$$

This is rewritten as follows

$$
  \frac{d{\tilde T}_M}{dt} = \kappa \, \frac{T_{M-1}-2{\tilde T}_M}{\Delta x^2}
$$

with

$$
  {\tilde T}_M = \frac 12 T_M
$$

If we redefine the vector with unknowns as

$$
  \vec{T} = \begin{pmatrix} T_1 \\ T_2 \\ T_3 \\ \vdots \\ T_{M-2} \\ T_{M-1} \\ {\tilde T}_M \end{pmatrix}
$$

then the matrix of the system becomes

$$
   A=   \frac{\kappa}{\Delta x^2} \left (
   \begin{array}{rrrrrrr}   -2       &  1 &  0      &          & \cdots &        &   0       \\
                             1       & -2 &  1      &          &        &        &           \\
                             0       &  1 & -2      &  1       &        &        &           \\
                             \vdots  &    & \ddots  & \ddots   & \ddots &        &  \vdots   \\
                                     &    &         &  1       & -2     &  1     &   0       \\
                                     &    &         &          &  1     & -2     &   1       \\
                             0       &    &         & \cdots   &        &  1     &  -2
   \end{array} \right )
$$

which is symmetric.
This means that all the eigenvalues of $A$ are real. Hence, no harmonic motion shows up in the heat equation (as expected).

Using the theory of Gerschgorin we can estimate the eigenvalues of $A$. For a symmetric matrix $A$ with entries $a_{ij}$ its eigenvalues are lying in the union of intervals

$$
  a_{ii} - \underset{j \neq i}{\sum_{j=1}^M}\,|a_{ij}| \leq \lambda \leq a_{ii} + \underset{j \neq i}{\sum_{j=1}^M}\,|a_{ij}|
$$

Thus, in our case we have

$$
  a_{ii} = \frac{-2\kappa}{\Delta x^2}\, , \quad \forall i \in [1,M]
$$

$$
  \sum_{j=2}^M \,|a_{1j}| = \frac{\kappa}{\Delta x^2}\, , \quad \sum_{j=1}^{M-1} \,|a_{Mj}| = \frac{\kappa}{\Delta x^2}
$$

and

$$
  \underset{j \neq i}{\sum_{j=1}^M}\,|a_{ij}| = \frac{2\kappa}{\Delta x^2}\, , \quad \forall i \in [2,M-1]
$$

and we conclude that all the eigenvalues satisfy the inequality

$$
  -\frac{4\kappa}{\Delta x^2} \, \leq \, \lambda \, \leq \, 0
$$

Moreover, matrix $A$ is nonsingular, meaning that all the eigenvalues are nonzero and thus exclusively negative.
As a consequence, the considered linear system of ODEs {eq}`modedif1` is regarded as being *damped*.
This property is also shared by the diffusion process because diffusion acts as a form of damping $-$ the variation in $c(x,t)$ reduces over time.
```

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

The semi discretization of the heat equation leads to a linear system of first order ODEs, {eq}`modedif1`. In accordance with the MOL approach, the next step is to integrate this system with respect to time.
Our choice for time integration would be the <u>forward Euler scheme</u>, since this is the most simple one.
Application of forward Euler to Eq. {eq}`modedif1` yields

$$
  \frac{T^{n+1}_m-T^n_m}{\Delta t} = \kappa \, \frac{T^n_{m+1}-2T^n_m+T^n_{m-1}}{\Delta x^2}\, , \quad m=1,\ldots,M-1\, , \quad n =0,1,2,\ldots
$$ (ftcs)

with $\Delta t$ the time step and $T^n_m \approx T(m\Delta x,n\Delta t)$ a discrete grid function, which
represents the wanted numerical solution to the heat equation, Eq. {eq}`diffusion1`, at time step $n$ and grid point $m$.
We can re-arrange this equation as follows

$$
  T^{n+1}_m = T^n_m + \frac{\kappa \Delta t}{\Delta x^2} \, \left (T^n_{m+1}-2T^n_m+T^n_{m-1} \right )
$$ (ftcs2)

At each *new* time step, the dependent variable $T$ at each interior grid point $x_m$ is computed from values of $T$ at
three grid points, $x_{m-1}$, $x_m$ and $x_{m+1}$, at the *preceding* time step.
This expression defines an **explicit** scheme for solving the heat equation.
Hence, the solution can be found at any time through a sequence of time steps.
This scheme is known as the **FTCS** scheme, which stands for **F**orward in **T**ime, **C**entral in **S**pace, since we have used
the forward approximation in time with explicit Euler and the central differences in space.

## Truncation error

A common method to check the order of accuracy of a numerical scheme is to compute its (global) truncation error.

```{admonition} Definition (truncation error)
Let be given a PDE with its solution $T(x,t)$ and let a numerical scheme for this PDE be given by

$$
  L_{\Delta t, \Delta x} \left ( T^n_m \right ) = 0
$$

where $L_{\Delta t, \Delta x}$ is a discrete linear operator depending on the numerical parameters $\Delta t$ and $\Delta x$, and $T^n_m$ is its numerical solution
at time step $t_n = n\Delta t$ and grid point $x_m = m\Delta x$.

The truncation error of the scheme is defined as

$$
  \tau_{\Delta t,\Delta x} = L_{\Delta t, \Delta x} \left ( T(x_m,t_n) \right )
$$
```

Let us consider the FTCS scheme {eq}`ftcs`. We can derive its truncation error, as follows

$$
  \tau_{\Delta t,\Delta x} = \frac{T(x_m,t_{n+1})-T(x_m,t_n)}{\Delta t} - \kappa \, \frac{T(x_{m+1},t_n)-2T(x_m,t_n)+T(x_{m-1},t_n)}{\Delta x^2}
$$

with $T(x,t)$ a sufficiently smooth, exact solution to the heat equation {eq}`diffusion1`. Because of this, we can use the Taylor series expansions of
$T(x_m,t_{n+1})$ and $T(x_{m\pm1},t_n)$ to further evaluate the truncation error. So,

$$
\begin{align*}
\tau_{\Delta t,\Delta x} &= \frac{T(x,t+\Delta t)-T(x,t)}{\Delta t} - \kappa \, \frac{T(x+\Delta x,t)-2T(x,t)+T(x-\Delta x,t)}{\Delta x^2} \\
                         &\\
                         &=\frac{\partial T}{\partial t}(x,t)+\frac 12 \Delta t \frac{\partial^2 T}{\partial t^2}(x,t) - \kappa \frac{\partial^2 T}{\partial x^2}(x,t) -
                           \frac{\kappa\Delta x^2}{12}\frac{\partial^4 T}{\partial x^4}(x,t) + \ldots\\
                         &\\
                         &=\frac 12 \Delta t \frac{\partial^2 T}{\partial t^2}(x,t) - \frac{\kappa\Delta x^2}{12}\frac{\partial^4 T}{\partial x^4}(x,t) + \ldots
\end{align*}
$$

and, thus

$$
  \tau_{\Delta t,\Delta x} = \mathcal{O} \left(\Delta t, \Delta x^2 \right)
$$

Hence, the FTCS scheme is first order in $\Delta t$ and second order in $\Delta x$.
In practice, this means we can discretize the spatial domain quite
coarsely but we must discretize the time interval more finely in order to achieve a required
accuracy.

:::{card} Exercise

We consider the ODE related to the Neumann boundary condition at $x=L$, which is given by (see {eq}`modedif1`)

$$
  \frac{dT_M}{dt} = 2\kappa \, \frac{T_{M-1}-T_M}{\Delta x^2}
$$

This ODE can be approximated using the forward Euler scheme which yields

$$
  \frac{T^{n+1}_M - T^n_M}{\Delta t} = \frac{2 \kappa}{\Delta x^2} \left ( T^n_{M-1} - T^n_M \right )
$$ (ftcsn)

Compute the associated truncation error.

```{admonition} Solution
:class: tip, dropdown

First, we replace the numerical solution $T^n_m$ by the exact solution $T(x_m,t_n)$. Hence, we have

$$
  \frac{T(x_M,t_{n+1}) - T(x_M,t_n)}{\Delta t} = \frac{2 \kappa}{\Delta x^2} \left ( T(x_{M-1},t_n) - T(x_M,t_n) \right )
$$

The exact solution is supposed to be smooth so that we can use the Taylor series expansions for the functions $T(L,t+\Delta t)$ and $T(L-\Delta x,t)$.
We expect a first order accuracy in time and hence the Taylor series of $T(L,t+\Delta t)$ is expanded till the second order term ("*first derivative + first order accuracy*").
With respect to the Taylor series of $T(L-\Delta x,t)$, we will expand this till the third order (=1+2) because we expect at most second order accuracy (it can be less!).
Hence,

$$
  T(L,t+\Delta t) = T(L,t) + \Delta t\, T_t(L,t) + \frac 12 \Delta t^2 \, T_{tt} (L,t)
$$

and

$$
  T(L-\Delta x,t) = T(L,t) - \Delta x\, T_x(L,t) + \frac 12 \Delta x^2 \, T_{xx} (L,t) - \frac 16 \Delta x^3 \, T_{xxx} (L,t)
$$

Substitution gives

$$
\begin{align*}
\tau_{\Delta t,\Delta x} &= \frac{T(L,t+\Delta t) - T(L,t)}{\Delta t} - \frac{2 \kappa}{\Delta x^2} \left ( T(L-\Delta x,t) - T(L,t) \right ) \\
                         &\\
                         &= T_t(L,t) + \frac 12 \Delta t \, T_{tt} (L,t) + 2 \kappa \left ( \frac{T_x}{\Delta x}(L,t) - \frac 12 T_{xx} (L,t) + \frac 16 \Delta x \, T_{xxx} (L,t) \right ) \\
                         &\\
                         &= \frac 12 \Delta t \, T_{tt} (L,t) + \frac 13 \kappa\, \Delta x \, T_{xxx} (L,t) \\
                         &\\
                         &= \mathcal{O} \left(\Delta t, \Delta x \right)
\end{align*}
$$

where we have used the homogeneous Neumann condition at $x=L$, namely, $T_x\,(L,t) = 0$.

So, we conclude that the numerical scheme related to the Neumann condition at $x=L$ is first order accurate both in time (as expected!) and in space (not expected!).

Our first thought might be to conclude that our *overall* approximation in the whole(!) domain, including the boundary points, might have lost second order accuracy.
However, this is not the case. Generally, we achieve second order accuracy in the overall numerical method even if the truncation error
is $\mathcal{O}(\Delta x)$ at a *single* boundary point as long as it is $\mathcal{O}(\Delta x^2)$ everywhere else.
So, we can often get away with one order of accuracy lower in the local error for the boundary conditions than what we have elsewhere.

```
:::

## Consistency and convergence

```{admonition} Definition (consistency)
A numerical scheme is called **consistent** if and only if

$$
  \lim_{\Delta x, \Delta t \to 0} \tau_{\Delta t,\Delta x} = 0
$$
```

According to this definition, the FTCS scheme {eq}`ftcs` is consistent with the heat equation {eq}`diffusion1`.

The above error analysis shows how well the FTCS scheme approximates the original
heat equation in the limit of $\Delta x, \Delta t \to 0$. However, it does *not* show how well the
numerical solution approximates the exact solution of the heat equation. This is a matter of convergence.

```{admonition} Definition (convergence)
A numerical scheme as described above is said to be **convergent** if

$$
  \lim_{\Delta x, \Delta t \to 0} T^n_m = T(x_m,t_n)
$$
```

In the study of convergence of a numerical scheme, there are two issues to be considered.

- Firstly, whether the numerical approximation is __*consistent*__ with the PDE we wish to solve.
- Secondly, whether the considered numerical scheme is __*stable*__, that is, its numerical solution remains bounded in case of endless repeating of this scheme, with fixed $\Delta t$ and $\Delta x$. This topic of **stability** will be investigated in some detail in the next section.

With these two considerations, we can apply the following

```{admonition} Basic rule
<center>consistency + stability &#8658; convergence</center>
```

Since a proof of convergence is the hard one, effort in the other two aspects is easily elaborated.
Consistency defines a relation between the numerical scheme and the PDE we wish to solve, whereas stability establishes a relation
between the computed solution and the exact solution of the numerical scheme. It should be emphasised that stability is a requirement
*just* on the numerical scheme and does not involve any condition on the PDE.

## Stability

We may write the FTCS scheme {eq}`ftcs`  and {eq}`ftcsn` in the matrix-vector notation, as follows (see also {eq}`discmat1`)

$$
  \vec{T}^{n+1} = \left ( I + \Delta t A \right ) \vec{T}^{n} + \Delta t \,\vec{g}
$$

with $\vec{T}^n = (T^n_1,\cdots,T^n_M)^{\text{T}}$ being the vector representing the numerical solution at time step $n$ and
$A$ is the discretization matrix as given by Eq. {eq}`matrdiff2`. Matrix $I$ is the identity matrix.
A way to check stability is to consider the eigenvalues $\lambda_m$ of the matrix $I + \Delta t A$ and subsequently require $|\lambda_m| \leq 1\,, \forall m$.
However, the matrices $A$ and $I$ are an $M \times M$ matrix with $M = L/\Delta x$ so that its dimension is growing as $\Delta x \to 0$. Hence, we might
not be able to determine eigenvalues of such a large matrix, because of the cumbersome and laborious algebra.

```{admonition} Derive stability condition using eigenvalues
:class: dropdown
For our discretization matrix $A$ it is still possible to derive a stability condition.
Specifically, using the Gerschgorin's theorem, we found the range of eigenvalues of $A$ which is given by

$$
  -\frac{4\kappa}{\Delta x^2} \, \leq \, \lambda \, < \, 0
$$

The smallest eigenvalue equals $-4\kappa/\Delta x^2$. Hence, the system of equations is stable under the condition

$$
  | 1 - \frac{4\kappa}{\Delta x^2}| \leq 1 \quad \Rightarrow \quad -2 \leq -\frac{4\kappa}{\Delta x^2} \leq 0
$$

The last inequality is always true while the first inequality is true if

$$
  \frac{\kappa \Delta t}{\Delta x^2} \leq \frac 12
$$
```

From a physical point of view, the solution to the heat equation {eq}`diffusion1` cannot be negative, that is, we must have $T(x,t) \geq 0\, , \forall x \in [0,L]\,, \forall t \geq 0$.
This implies that our finite difference scheme should share the same property, so that the numerical solution remains non-negative as time progresses.
As a consequence, **spurious oscillations** (wiggles) will not occur. It is well known that in the case of <u>diffusion processes</u>, wiggles in the solution
will blow up and thus will be unbounded in finite time. To prevent this instability, we have to require that our numerical scheme should not exhibit spurious oscillations.

Recall {eq}`ftcs2`. We can rewrite this equation as follows

$$
  T^{n+1}_m = \left ( 1 - \frac{2\kappa \Delta t}{\Delta x^2} \right ) T^n_m + \frac{\kappa \Delta t}{\Delta x^2} \, \left ( T^n_{m+1}+T^n_{m-1} \right )
$$

Assume that $T^n_m \geq 0$ for all grid points $m = 1,\ldots,M-1$, then the last two terms on the right-hand side are non-negative. Furthermore, if

$$
  1 - \frac{2\kappa \Delta t}{\Delta x^2} \geq 0 \quad \Rightarrow \quad \frac{\kappa \Delta t}{\Delta x^2} \leq \frac 12
$$

then $T^{n+1}_m \geq 0$ for all grid points $m = 1,\ldots,M-1$. Hence, by <u>induction</u> it follows that the numerical solution is non-negative at all times.

This resulted stability condition is

$$
  \boxed{\frac{\kappa \Delta t}{\Delta x^2} \leq \frac 12}
$$

and states that for a given $\Delta x$, the allowed value of $\Delta t$ must be small enough to keep the FTCS scheme {eq}`ftcs` stable.
For this reason, the FTCS scheme is said to be **conditionally stable**.

:::{card} Exercise

Verify the above stability condition for grid point $m=M$.

```{admonition} Solution
:class: tip, dropdown

We rewrite {eq}`ftcsn` as follows

$$
  T^{n+1}_M = T^n_M + \frac{2 \kappa \, \Delta t}{\Delta x^2} \left ( T^n_{M-1} - T^n_M \right )
$$

or

$$
  T^{n+1}_M = \left ( 1 -  \frac{2 \kappa \, \Delta t}{\Delta x^2} \right ) \, T^n_M + \frac{2 \kappa \, \Delta t}{\Delta x^2} T^n_{M-1}
$$

We assume that the values $T^n_M$ and $T^n_{M-1}$ are non-negative.
While the second term on the right-hand side is non-negative, the first term is non-negative as long as the following condition holds

$$
  \frac{\kappa \Delta t}{\Delta x^2} \leq \frac 12
$$

which is the same condition for the inner points $m = 1,\ldots,M-1$.

```
:::
