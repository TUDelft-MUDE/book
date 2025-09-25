# Advection equation

In this section we discuss the numerical solution of the 1D advection equation as given by

$$
  \pderiv{c}{t} + u \pderiv{c}{x} = 0
$$ (advection1)

This first order hyperbolic PDE describes
the propagation of any disturbance $c(x,t)$ with a constant speed $u$ in an infinite long 1D domain.
Given any initial condition $c(x,0) = c^0(x)$ the solution at any *later* time is given
by $c(x,t) = c^0(x-ut)$. This can be verified by computing the $t-$ and $x-$derivatives of the solution and substituting
into the equation above. The function $c^0(x-ut)$ is a solution for
**right-travelling waves**, since the graph of $c^0(x-ut)$
is simply the graph of $c^0(x)$ shifted to the right by $ut$ spatial units. As time
increases, the profile $c^0(x)$ moves to the right at speed $u$.
Thus solutions are simply propagated, or **advected**, with constant
speed $u$ without *deforming*, that is, no change in shape. If $u > 0$, propagation is from left to right. If $u < 0$, propagation is from right to left.
This phenomenon is also known as **transport** or **convection**.
