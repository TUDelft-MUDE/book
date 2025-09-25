(advection)=
# Advection Equation

In this section we discuss the numerical solution of the 1D advection equation as given by

$$
  \frac{\partial c}{\partial t} + u \frac{\partial c}{\partial x} = 0
$$ (advection1)

This first order hyperbolic PDE describes
the propagation of a disturbance (e.g., waves, pollutants, particles) $c(x,t)$ with a constant flow speed $u$ in an infinite long 1D domain.
Given any initial condition $c(x,0) = c^0(x)$ the solution at any *later* time is given
by $c(x,t) = c^0(x-ut)$. This can be verified by computing the $t-$ and $x-$derivatives of the solution and substituting
into the equation above. The function $c^0(x-ut)$ is a solution for
**right-travelling waves**, since the graph of $c^0(x-ut)$
is simply the graph of $c^0(x)$ shifted to the right by $ut$ spatial units. As time
increases, the profile $c^0(x)$ moves to the right at speed $u$.
Thus solutions are simply propagated, or **advected**, with constant
speed $u$ without *deforming*, that is, no change in shape. If $u > 0$, propagation is from left to right. If $u < 0$, propagation is from right to left, that is, **left-travelling waves**.

Advection is thus an example of transport by fluid motion. Another example is **convection** which is the transport of a fluid (water or air) in response to heat, for instance, boiling water.
Although, these two terms are interchangeably in mathematical sense, <u>advection</u> is the usual term (especially in hydraulic engineering).

The above described problem is an initial value problem (IVP). Now, let us consider a 1D domain with a finite length $L$, that is, $0 \leq x \leq L$.
In this case we need to impose some boundary conditions. A boundary condition is needed at a certain boundary location where the information *enters* the domain.
This depends on the propagation velocity. If $u > 0$, the ingoing transport is at the left boundary, $x=0$, while if $u < 0$, the ingoing transport is at the right boundary, $x=L$.

As an example, we consider Eq. {eq}`advection1` with $u = 1$ m/s. A well posed problem is then formulated as follows:

$$
  \begin{align}
    &\frac{\partial c}{\partial t} + u \frac{\partial c}{\partial x} = 0\, , \quad x \in (0,L)\, ,\quad t > 0 \\
    \\
    &c(x,0) = c^0(x)\, ,\quad x \in [0,L] \\
    \\
    &c(0,t) = f(t)\, ,\quad t > 0 \\
  \end{align}
$$ (advection2)

where $f(t)$ described the incoming wave-like disturbance; this function is usually expressed as a Fourier timeseries.
This IBVP is called the **wave equation** and is commonly applied in wave modelling but also in sediment transport.

```{note}

Note that the above IBVP {eq}`advection2` would become ill posed if $u<0$.

```

In contrast to the diffusion equation {eq}`diffusion1`, the solution to the advection equation is not necessarily smooth. In other words, $c(x,t)$ is allowed to be discontinuities or
non-smooth. Examples are shock waves, hydraulic jumps and tidal bores. Although the wave equation {eq}`advection1` appears seemingly simple, the numerical solution to this equation is quite a challenge, as we
will discover below.

## Discretization

We reconsider the computional grid as discussed in Section {ref}`diffusion`.
Thus, we have our uniform mesh consisting of nodes $x_0,\cdots,x_{M}$ and $\Delta x = x_m - x_{m-1}$.
We apply the MOL approach, so that we first discretize in space and then integrate over time.

A possible candidate for the spatial approximation would be central differences
(cf. Eq. {eq}`cdf1`), as follows

$$
  \frac{dc_m(t)}{dt} + u \frac{c_{m+1}(t) - c_{m-1}(t)}{2\Delta x} = 0\, , \quad m=1,\ldots,M-1\, , \quad t > 0
$$

This is a semi discretization of Eq. {eq}`advection1` for the *inner* grid points of the computational domain.

:::{card} Exercise

Verify yourself that this spatial discretization is second order accurate.

:::

The resulted system of first order ODEs with the unknowns $c_m(t)$ can be written as

$$
  \frac{d\vec{c}}{dt} = A \vec{c}
$$ (vecadv)

with $\vec{c} = (c_1,\cdots,c_{M-1})^{\text{T}}$ being the vector representing the unknowns and
matrix $A$ is the $(M-1) \times (M-1)$ discretization matrix as given by

$$
   A=   \frac{u}{2\Delta x} \left (
   \begin{array}{rrrrrrr}    0       & -1 &  0      &          & \cdots &        &   0       \\
                             1       &  0 & -1      &          &        &        &           \\
                             0       &  1 &  0      & -1       &        &        &           \\
                             \vdots  &    & \ddots  & \ddots   & \ddots &        &  \vdots   \\
                                     &    &         &  1       &  0     & -1     &   0       \\
                                     &    &         &          &  1     &  0     &  -1       \\
                             0       &    &         & \cdots   &        &  1     &   0
   \end{array} \right )
$$

The next step is to integrate the above system of ODEs with respect to time. Although the MOL approach is very flexible in the sense that
the choice of time integration is independent of the choice of space discretization, we must be careful since the resulted scheme
may not be stable. For example, let us choose the forward Euler scheme, we get

$$
  \frac{c^{n+1}_m - c^{n}_m}{\Delta t} + u \frac{c^n_{m+1} - c^n_{m-1}}{2\Delta x} = 0\, , \quad m=1,\ldots,M-1\, , \quad n = 0, 1, 2, \ldots
$$ (ftcs3)
 
This explicit scheme is again the FTCS scheme but applied to the wave equation. In contrast to the diffusion equation (cf. Eq. {eq}`ftcs`),
this FTCS scheme {eq}`ftcs3` is **unconditionally unstable**, that is, it is unstable for any time step. Therefore, the FTCS scheme is useless
for any advection-type equation.

This instability is related to the fact that the influence of the disturbance only comes from upstream and not from downstream.
This is a specific feature for hyperbolic problems. More specifically, assuming that the propagation velocity
is positive, $u>0$, the solution $c_m$ at $x_m$ should only be affected by $c_{m-1}$ at $x_{m-1}$ (upstream) and not by the solution downstream, that is, $c_{m+1}$.
However, since this does occur with scheme {eq}`ftcs3`, it inevitably leads to unlimited growth.

```{note}

A possible solution to this instability problem is to apply the backward Euler scheme. This **implicit** scheme is always stable (see Chapter {ref}`numerical_modelling`). We then obtain
the so-called BTCS (**B**ackward in **T**ime, **C**entral in **S**pace) scheme, as follows

$$
  \frac{c^{n+1}_m - c^{n}_m}{\Delta t} + u \frac{c^{n+1}_{m+1} - c^{n+1}_{m-1}}{2\Delta x} = 0
$$

However, this is very unusual since the numerical solution is less straightforward to obtain. This can be seen as follows.

Let us consider the system of ODEs {eq}`vecadv` and subsequently apply backward Euler. This yields

$$
  \frac{\vec{c}^{n+1}-\vec{c}^n}{\Delta t} = A \, \vec{c}^{n+1} \quad \Rightarrow \quad \left ( I - \Delta t A \right ) \, \vec{c}^{n+1} = \vec{c}^n
$$

with $\vec{c}^n = (c^n_1,\cdots,c^n_{M-1})^{\text{T}}$ being the vector representing the numerical solution at time step $n$ and
$A$ is the discretization matrix as given above. Matrix $I$ is the identity matrix.
We see that the solution $\vec{c}^{n+1}$ cannot be computed immediately. Instead, we need to solve a linear system of $M-1$ equations for the $M-1$ unknowns at the new time step.
In addition, the rank of the matrix $A$ is expressed in terms of $M = L/\Delta x$ which can be quite large, especially if the mesh size $\Delta x$ is chosen very small.

This observation generally holds for any implicit scheme.

```

## The upwind method

Since we are dealing with information being propagated along a certain direction, it would be better to propose a scheme that gathers information to be propagated
in the same direction. For instance, the backward finite difference approximation, Eq. {eq}`bdfs`, applied to $\partial c/\partial x$ will gather information from the
left to propagate, while the forward finite difference operator, Eq. {eq}`fdfs`, gathers from the right. Hence,
our knowledge of which direction the wave should propagate indicates the **upwind** direction.
If $u > 0$, then propagation of the disturbance is from left to right. So, the upwind direction is *to the left*, that is, the information is obtained from the **backward**
direction. For $u < 0$, the upwind direction is *to the right* and so, the information is from the **forward** direction.

The **upwind difference scheme** is given by

$$
  \frac{\partial c}{\partial x} =
  \begin{cases} \frac{c_{m}-c_{m-1}}{\Delta x}\, , \quad \text{if} \, \, u > 0 \\
                 \\
                 \frac{c_{m+1}-c_{m}}{\Delta x}\, , \quad \text{if} \, \, u < 0
  \end{cases}
$$

and it correctly passes information in the direction of the characteristic of the advection equation.
This approximation is called **first order upwinding**.

:::{card} Exercise

Verify the first order accuracy of this scheme to $\partial c/\partial x$.

:::

Application of explicit Euler yields

$$
  c^{n+1}_m = c^n_m - \sigma
  \begin{cases} c^n_m - c^n_{m-1} \, , \quad \mbox{if} \, \, u > 0 \\
                 \\
                 c^n_{m+1} - c^n_m \, , \quad \mbox{if} \, \, u < 0
  \end{cases}
$$ (ftbs)

This scheme is called the **FTBS** scheme, which stands for **F**orward in **T**ime, **B**ackward in **S**pace,
and is first order accurate in both time and space.

:::{card} Exercise

For the FTBS scheme with $u>0$, show that $\tau_{\Delta t,\Delta x} = \mathcal{O} (\Delta t,\Delta x)$.

```{admonition} Solution
:class: tip, dropdown

With $u>0$, the FTBS scheme is given by

$$
  \frac{c^{n+1}_m - c^n_m}{\Delta t} + u \frac{c^n_m - c^n_{m-1}}{\Delta x} = 0
$$

To check consistency we must require the solution $c(x,t)$ to be smooth, so that we can apply the following Taylor series expansions

$$
  c(x,t+\Delta t) = c(x,t) + \Delta t\, c_t(x,t) + \frac 12 \Delta t^2\, c_tt(x,t)
$$

and

$$
  c(x-\Delta x,t) = c(x,t) - \Delta x\, c_x(x,t) + \frac 12 \Delta x^2\, c_xx(x,t)
$$

Note that both series have been expanded till second order ("*first derivative + first order accuracy*").

Next, substituting both expansions into the FTBS scheme yields

$$
\begin{align*}
\tau_{\Delta t,\Delta x} &= \frac{c(x,t+\Delta t)-c(x,t)}{\Delta t} + u \, \frac{c(x,t)-c(x-\Delta x,t)}{\Delta x} \\
                         &\\
                         &=\frac{\partial c}{\partial t}(x,t)+\frac 12 \Delta t \frac{\partial^2 c}{\partial t^2}(x,t) + \u \frac{\partial c}{\partial x}(x,t) -
                           \frac{u\Delta x}{2}\frac{\partial^2 c}{\partial x^2}(x,t) + \ldots\\
                         &\\
                         &=\frac 12 \Delta t \frac{\partial^2 c}{\partial t^2}(x,t) - \frac{u\Delta x}{2}\frac{\partial^2 c}{\partial x^2}(x,t) + \ldots
\end{align*}
$$

and, thus

$$
  \tau_{\Delta t,\Delta x} = \mathcal{O} \left(\Delta t, \Delta x \right)
$$

Hence, the FTBS scheme is first order in $\Delta t$ and first order in $\Delta x$.

```
:::

The above exercise demonstrates that the FTBS scheme is consistent with the wave equation {eq}`advection1`.
Next, we check the stability of the FTBS scheme. Since it is explicit, we expect that this scheme can either be
*conditionally stable* or *unconditionally unstable* (like the FTCS scheme).

Suppose that $u>0$. Then the FTBS scheme is given by

$$
  \frac{c^{n+1}_m - c^n_m}{\Delta t} + u \frac{c^n_m - c^n_{m-1}}{\Delta x} = 0
$$

To check stability, we rewrite the scheme as follows

$$
  c^{n+1}_m = c^n_m - \frac{u\,\Delta t}{\Delta x} \, \left ( c^n_m - c^n_{m-1} \right )
$$

or 

$$
  c^{n+1}_m = c^n_m - \sigma \, \left ( c^n_m - c^n_{m-1} \right )
$$

with $\sigma = u\,\Delta t/\Delta x$ defined as the **Courant number**. This equation is rewritten as

$$
  c^{n+1}_m = (1-\sigma)c^n_m + \sigma c^n_{m-1}
$$

We assume by induction that $c^n_m \geq 0$ and $c^n_{m-1} \geq 0$. Then $c^{n+1}_m \geq 0$ if $1-\sigma \geq 0$.
Hence, the stability condition of the FTBS scheme reads

$$
  \sigma = \frac{u\,\Delta t}{\Delta x} \leq 1
$$

This condition is known as the *Courant-Friedrichs-Lewy* (**CFL**) condition. The CFL condition plays an important role
in the numerical solution to wave-like (or advection-like) PDEs.

:::{card} Exercise

Suppose that $u<0$. Verify that in that case the FTBS scheme is stable if

$$
 -1 \leq \frac{u\,\Delta t}{\Delta x} \leq 0
$$

:::
