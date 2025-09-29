(advdif)=
# Advection-diffusion equation

In Sections {ref}`diffusion` and {ref}`advection` we have treated the numerical solution of the diffusion equation and the advection equation, respectively.
By combining these processses we obtain the following 1D **advection-diffusion** equation

$$
  \frac{\partial c}{\partial t} + u\frac{\partial c}{\partial x} - \kappa\frac{\partial^2 c}{\partial x^2} = 0
$$ (advdifi)

This **instationary** advection-diffusion equation describes the time evolution of a **constituent** $c(x,t)$ that is transported with
flow velocity $u$ and at the same time diffuses (or spread in space) with a diffusion coefficient $\kappa$. This PDE is classified as a *parabolic* one.

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
In particular we dive into the role and the meaning of central differences and the upwind scheme. In this context, we will explore the typical numerical phenomenon of **wiggles**.
This is an artifact caused by central differences, and we will explore how to reduce it through diffusion.

## Stationary advection-diffusion equation

The following 1D boundary value problem is considered

$$
  \begin{align}
    &u\frac{dc}{dx} - \kappa\frac{d^2c}{dx^2} = 0\, , \quad 0 < x < 1 \\
    & \\
    &c(0) = 0 \\
    & \\
    &c(1) = 1
  \end{align}
$$ (statcv1)

The solution to this BVP is the spatial distribution of the constituent $c(x)$ along the interval $0 \leq x \leq 1$ as depicted below.

```{figure} https://files.mude.citg.tudelft.nl/cvexact.png
---
scale: 75%
name: cvexact
align: center
---
Exact solution to Eq. {eq}`statcv1` with $\kappa = 0.025$ m$^2$/s and $u = 1$ m/s.
```

Generally, this constituent $c(x)$ is assumed to be smooth enough. Clearly,
the solution displays a steep gradient in the **boundary layer**. The thickness of this layer is mainly determined by the amount of diffusion involved
and is due to the fact that the solution has to match to all the given boundary conditions. The boundary layer thickness is
generally proportional to the square root of $\kappa$. To accurately solve this boundary layer, a local mesh refinement is often necessary.

Based on accuracy reasons, we choose central differences for both advective and diffusive processes, as follows

$$
  u\frac{c_{m+1}-c_{m-1}}{2\Delta x} - \kappa \frac{c_{m+1}-2c_m+c_{m-1}}{\Delta x^2} = 0\, , \quad m = 1,\ldots,M-1
$$ (statcveq)

:::{card} Exercise

Verify this and show that $\tau_{\Delta x} = \mathcal{O}(\Delta x^2)$.

:::

The boundary conditions are simply discretized as follows

$$
  c_0 = 0 \, , \quad c_M = 1
$$

A peculiar feature of central differences applied to the first derivative $\partial c/\partial x$ (or generally, the advection term) is that they are
prone to generate **spurious oscillations** or **wiggles**, especially near steep gradients.
This renders the numerical solution physically meaningless. The way to counteract these wiggles is to add some diffusion.
The effect of this diffusion process is to smear out the inregularities.
The question arises whether the amount of physical diffusion, as indicated by $\kappa$, is considered to be enough to prevent oscillations. To answer this question,
we rewrite Eq. {eq}`statcveq` as follows

$$
  \left ( \frac 12 P_{\Delta} - 1 \right ) c_{m+1} + 2c_m - \left ( \frac 12 P_{\Delta} + 1 \right ) c_{m-1} = 0
$$ (recrel1)

with

$$
   P_{\Delta} \equiv \frac{u\Delta x}{\kappa}
$$

the so-called **mesh P&eacute;clet number**.

Note that because of consistency, the sum of the coefficients of Eq. {eq}`recrel1` is zero.
Hence, with $p=$&frac12;$P_{\Delta}-1$ and $q=-$&frac12;$P_{\Delta} - 1$, we have $p+q+2=0$.
Eq. {eq}`recrel1` represents a **recurrent relation** and its general solution is of the form

$$
  c_m = \alpha\, r_1^m + \beta\, r_2^m
$$

where $\alpha$ and $\beta$ are some constants and $r_1$ and $r_2$ are the roots of the following **characteristic equation**

$$
  r^2 - \left ( 1 + \frac{q}{p} \right ) r + \frac{q}{p} = 0
$$

These roots are given by

$$
  r_1 = 1\, , \quad r_2 = \frac{q}{p} = \frac{2+P_{\Delta}}{2-P_{\Delta}}
$$

:::{card} Exercise

Verify the above characteristic equation and its roots.

```{admonition} Solution
:class: tip, dropdown

From Eq. {eq}`recrel1` we have the followng

$$
  p\, c_{m+1} - (p+q)\, c_m + q\, c_{m-1} = 0
$$

or

$$
  c_{m+1} - \left ( 1 + \frac{q}{p} \right ) c_m + \frac{q}{p} c_{m-1} = 0
$$

The associated characteristic equation is then given by

$$
  r^2 - \left ( 1 + \frac{q}{p} \right ) r + \frac{q}{p} = 0
$$

This is a quadratic equation for which the two roots can be found as

$$
r_{1,2} = \frac{p+q \pm \sqrt{p^2+q^2 -2pq}}{2p}
$$

or

$$
  r_1 = 1\, , \quad r_2 = \frac{q}{p}
$$

```
:::

To prevent wiggles, both roots must be non-negative.

```{note}

To see why this is so, we consider the solution

$$
  c_m = r^m
$$

This implies that

$$
  c_{m+1} = r^{m+1} = r \times r^m = r\,c_m \quad \Rightarrow \quad r = \frac{c_{m+1}}{c_m}
$$

Hence, if both solutions $c_m$ and $c_{m+1}$ are positive (or negative) then $r > 0$. However, if $c_m>0$ but the next one $c_{m+1} <0$ (or the other way around), thus the solution oscillates, then $r<0$.
Therefore, wiggles in the solution occur as soon as $r<0$.

```

Here, we must require $r_2 \geq 0$. Hence, the restriction on the mesh P&eacute;clet number reads

$$
  |P_{\Delta}|  = \frac{|u|\Delta x}{\kappa} \leq 2
$$ (restpc)

:::{card} Exercise

Derive this restriction.

```{admonition} Solution
:class: tip, dropdown

The second root $r_2$ must be non-negative which implies

$$
  \frac{2+P_{\Delta}}{2-P_{\Delta}} \geq 0
$$

There are two possibilities:

- both numerator $2+P_{\Delta}$ and denominator $2-P_{\Delta}$ are positive
- both numerator $2+P_{\Delta}$ and denominator $2-P_{\Delta}$ are negative

The first posssibility provides the appropriate restriction, namely,

$$
  -2 \leq P_{\Delta} \leq 2
$$

while the second possibility yields

$$
  P_{\Delta} < -2 \quad \text{and} \quad P_{\Delta} > 2
$$

which is not possible.

```
:::


Let us consider our example with $\kappa=0.025$ m$^2$/s and $u=1$ m/s and we choose $\Delta x = 0.1$ m, so that $P_{\Delta} = 4$.
The following figure depicts the obtained numerical solution that clearly shows wiggles $-$ the solution oscillates around the boundary layer.
In this case, as we can see, $P_{\Delta} > 2$ which implies that the current amount of diffusion is not sufficient to prevent wiggles.

```{figure} https://files.mude.citg.tudelft.nl/cvcentral.png
---
scale: 75%
name: cvcentral
align: center
---
Solution obtained with central differences and $\Delta x = 0.1$ m.
```

A simple remedy would be to decrease the mesh size $\Delta x$ such that the considered restriction is fulfilled. This is
demonstrated with the following example. We now choose $\Delta x = 0.025$ m, so that $P_{\Delta} = 1$. The result is depicted in
the following figure.

```{figure} https://files.mude.citg.tudelft.nl/cvcentral2.png
---
scale: 75%
name: cvcentral2
align: center
---
Solution obtained with central differences and $\Delta x = 0.025$ m.
```

Another remedy would be to apply an upwind scheme.
In this way, sufficient amount of **numerical diffusion** is added so that wiggles are prevented.
However, precautions should be taken so that the numerical diffusion will not dominate the physical one.
This way of applying an upwind scheme is a very common practice.

To demonstrate this, we apply a first order upwind scheme. Let us assume $u>0$. Hence, we have the following discretized equation for internal points $m = 1,\cdots,M-1$

$$
  u\frac{c_m-c_{m-1}}{\Delta x} - \kappa \frac{c_{m+1}-2c_m+c_{m-1}}{\Delta x^2} = 0
$$ (statcveq2)

The corresponding characteristic equation is given by

$$
  r^2 - (P_{\Delta} +2) r + P_{\Delta}+1 = 0
$$

and its roots are

$$
  r_1 = 1\, , \quad r_2 = 1+P_{\Delta}
$$

Hence, both roots are always non-negative and the numerical solution will not display any oscillations, irrespective of the value of $P_{\Delta}$. Apparently, the addition of the numerical
diffusion due to first order upwinding appears to be sufficient.

Another way to see this is by considering the modified equation. This equation is obtained by adding and substracting &frac12;$u(c_{m-1} + c_{m+1} - 2c_m)/\Delta x$
to the left-hand side of Eq. {eq}`statcveq2` and subsequently re-ordering terms

$$
  u\frac{c_{m+1}-c_{m-1}}{2\Delta x} - (\kappa+\kappa_a) \frac{c_{m+1}-2c_m+c_{m-1}}{\Delta x^2} = 0
$$

where $\kappa_a =$&frac12;$u\Delta x > 0$ is the **artificial** or numerical diffusion coefficient due to first order upwinding. This scheme would result from the application of central differences
to Eq. {eq}`statcv1` with a diffusion coefficient $\kappa+\kappa_a$. This scheme will generate non-negative solutions if

$$
  \frac{u\Delta x}{\kappa + \kappa_a} \leq 2 \quad \Rightarrow \quad u\Delta x \leq 2\kappa + u\Delta x
$$

This is true for any $\Delta x$ and thus, the application of first order upwinding will prevent wiggles.

However, this first order upwind scheme is often considered to be too dissipative.
See figure below where the corresponding numerical solution is found to be rather inaccurate, in particular when the physical diffusion is smaller than
the numerical one, $\kappa < \kappa_a$.

```{figure} https://files.mude.citg.tudelft.nl/cvupwind.png
---
scale: 75%
name: cvupwind
align: center
---
Solution obtained with the first order upwind scheme and $\Delta x = 0.1$ m so that $\kappa_a = 0.05$ m$^2$/s.
```

Note that the boundary layer thickness of the numerical solution is larger than that of the exact one due to artificial diffusion.
