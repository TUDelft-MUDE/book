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
speed $u$ without *deforming*, that is, no change in shape. If $u > 0$, propagation is from left to right. If $u < 0$, propagation is from right to left.

Advection is thus an example of transport by fluid motion. Another example is **convection** which is the transport of a fluid (water or air) in response to heat, for instance, boiling water.
Although, these two terms are interchangeably in mathematical sense, *advection* is the usual term (especially in hydraulic engineering).

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
This IBVP is called the **wave equation** and is commonly applied in wave modelling.

In contrast to the diffusion equation {eq}`diffusion1`, the solution to the advection equation is not necessarily smooth. In other words, $c(x,t)$ is allowed to be discontinuities or
non-smooth. Examples are shock waves, hydraulic jumps and tidal bores. Although the wave equation appears seemingly simple, the numerical solution to this equation is quite a challenge, as we
will discover below.

## Discretization of advection equation

Here we consider discretization.
