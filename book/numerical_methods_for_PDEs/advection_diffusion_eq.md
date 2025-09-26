(advdif)=
# Advection-diffusion equation

In Sections {ref}`diffusion` and {ref}`advection` we have treated the numerical solution of the diffusion equation and the advection equation, respectively.
By combining these processses we obtain the following 1D **advection-diffusion** equation

$$
  \frac{\partial c}{\partial t} + u\frac{\partial c}{\partial x} - \kappa\frac{\partial^2 c}{\partial x^2} = 0
$$ (advdifi)

This **instationary** advection-diffusion equation describes the time evolution of a **constituent** $c(x,t)$ that is transported with
flow velocity $u$ and at the same time diffuses with a diffusion coefficient $\kappa$. This PDE is classified as a *parabolic* one.

In some cases, however, we may be interested in the steady state only. In this respect, the following **stationary** equation will be considered

$$
  u\frac{dc}{dx} - \kappa\frac{d^2 c}{dx^2} = 0
$$ (advdifs)

```{note}

Eq. {eq}`advdifi` is a 1D PDE while Eq. {eq}`advdifs` is a 1D ODE. However, a 2D stationary advection-diffusion equation as given by

$$
  u\frac{\partial c}{\partial x} + v\frac{\partial c}{\partial y} - \kappa \left ( \frac{\partial^2 c}{\partial x^2} + \frac{\partial^2 c}{\partial y^2} \right ) = 0
$$

is an elliptic PDE. Here, $v$ is the flow velocity in $y-$direction.

```

We first deals with the numerical solution of stationary advection-diffusion equation {eq}`advdifs` and then that of instationary advection-diffusion equation {eq}`advdifi` in a separate section.

## Stationary advection-diffusion equation

The following
