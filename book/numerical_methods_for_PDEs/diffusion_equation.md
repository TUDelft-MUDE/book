(diffusion)=
# Diffusion Equation

In this section we discuss the numerical solution of the 1D diffusion equation. The specific (initial) boundary value problem (IBVP) we wish to solve is the following

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
$$

and is known as the **heat equation**. This equation describes the flow of heat in a rod with a finite length, made out of some heat-conducting
material, subject to some boundary conditions at each end.
Specifically, this heat *spreads* out spatially as time increases. This phenomenon is called **diffusion**.
The solution to the heat equation is the temperature distribution at any time $t$ and vary with $x$ along the rod.

We assume that $T(x,t)$ is smooth enough, so that we can differentiate this function many times as we want and each derivative is a well-defined *bounded* function (that has thus a fixed upperbound).
Here $L$ is the given finite length of the domain and $T^0(x)$ is a given function defining the initial condition.
The coefficient $\kappa > 0$ is the thermal diffusivity.

```{tip}

Always check the dimension of parameters that appear in the PDE. For instance, in the given heat equation, the unit of $\kappa$ is m$^2$/s. (Check yourself!)

```

In the above case, we have imposed a Dirichlet condition at $x = 0$ and a Neumann condition at $x = L$.
Since both these boundary conditions are time independent, we expect the solution to eventually reach a **steady state**
solution $T(x,t) \to {\tilde T}(x)$ which then remains essentially unchanged at later times.
Hence, we shall marching forward in time until a steady state solution is found. During this marching a **transient** solution will be obtained that must fulfill the initial condition.

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

The above mathematical model is well posed since we found a unique solution that is stable. An example of an ill posed problem would be the one
in which the Dirichlet boundary condition at $x = 0$ is replaced by the following homogeneous Neumann condition

$$
 \frac{\partial T}{\partial x} (0,t) = 0\, ,\quad t > 0
$$

In that case, the steady state solution would be

$$
  {\tilde T}(x) = b
$$

where $b$ remains undetermined. Hence, this solution is not unique!

```

The first step is to **discretize** the domain $[0,L]$ into a finite number of **grid points** $M+1$ where we
intend to compute the solution of the PDE. We shall use a uniform or **equidistant** grid, with a **grid spacing** $\Delta x = L/M$.
We shall refer to one of the points in the grid as $x_m = m\Delta x\,, m=0,\ldots,M$.
The first and last grid points of the domain, $x_0$ and $x_M$, are called the **boundary points**, while the other grid points are
the **internal** ones. See also {numref}`grid`.

Likewise we discretize the time interval into a number of time steps, separated
by a time increment $\Delta t$, and only compute the solution for times $t_n = n\Delta t\,, n=1,2,3,\ldots$ until a steady state is found.
Our aim is to compute the solution of the PDE for all values $T^n_m \approx T(m\Delta x,n\Delta t)$.
