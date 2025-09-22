(diffusion)=
# Diffusion equation

In this section we discuss the numerical solution of the 1D diffusion equation. The specific (initial) boundary value problem we wish to solve is the following

$$
  \begin{align}
    &\pderiv{T}{t} = \kappa \pderiv{^2T}{x^2}\, , \quad x \in (0,L)\, ,\quad t > 0 \\
    \\
    &T(x,0) = T^0(x)\, ,\quad x \in [0,L] \\
    \\
    &T(0,t) = 1\, ,\quad t > 0 \\
    \\
    &\pderiv{T}{x} (L,t) = 0\, ,\quad t > 0
  \end{align}
$$

and is known as the **heat equation**. This equation describes the flow of heat in a rod with a finite length, made out of some heat-conducting
material, subject to some boundary conditions at each end.
Specifically, this heat *spreads* out spatially as time increases. This phenomenon is called **diffusion**.
The solution to the heat equation is the temperature distribution at any time $t$ and vary with $x$ along the rod.

We assume that $T(x,t)$ is smooth enough, so that we can differentiate this function many times as we want and each derivative is a well-defined *bounded* function.
Here $L$ is the given finite length of the domain and $T^0(x)$ is a given function defining the initial condition.
The coefficient $\kappa > 0$ is the thermal diffusivity.

In this specific case, we have imposed a Dirichlet condition at $x = 0$ and a Neumann condition at $x = L$.
Since the boundary conditions are all time independent, we expect the solution to eventually reach a **steady state**
solution $T(x,t) \to {\tilde T}(x)$ which then remains essentially unchanged at later times.
Hence, we shall marching forward in time until a steady state solution is found. During this marching a **transient** solution will be obtained that must fulfill the initial condition.

:::{card} Exercise

Show that the steady state solution is $\underset{t \to \infty}{\lim} T(x,t) = {\tilde T}(x) = 1, x \in [0,1]$.

:::

The first step is to **discretize** the domain into a finite number of **grid points** $M+1$ where we
intend to compute the solution of the PDE. We shall use a uniform or **equidistant**
grid, with a **grid spacing** $\Delta x = L/M$. We shall refer to one of the points in the grid as $x_m = m\Delta x\,, m=0,\ldots,M$.
The first and last grid points of the domain, $x_0$ and $x_M$, are called the **boundary points**, while the other grid points are
the **internal** ones.

Likewise we discretize the time interval into a number of time steps, separated
by a time increment $\Delta t$, and only compute the solution for times $t_n = n\Delta t\,, n=1,2,3,\ldots$ until a steady state is found.
Our aim is to compute the solution of the PDE for all values $T^n_m \approx T(m\Delta x,n\Delta t)$.
