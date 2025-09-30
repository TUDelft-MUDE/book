(advdif)=
# Advection-diffusion equation

In Sections {ref}`diffusion` and {ref}`advection` we have treated the numerical solution of the diffusion equation and the advection equation, respectively.
By combining these processses we obtain the following 1D **advection-diffusion** equation

$$
  \frac{\partial c}{\partial t} + u\frac{\partial c}{\partial x} - \kappa\frac{\partial^2 c}{\partial x^2} = 0
$$ (advdifi)

This **instationary** advection-diffusion equation describes the time evolution of a **constituent** $c(x,t)$ that is transported with
flow velocity $u$ and at the same time diffuses (or spread) with a diffusion coefficient $\kappa$. This PDE is classified as a *parabolic* one.

In some cases, however, we may be interested in the steady state only. In this respect, the following **stationary** equation will be considered

$$
  u\frac{dc}{dx} - \kappa\frac{d^2 c}{dx^2} = 0
$$ (advdifs)

which renders the balance between advection and diffusion.

```{note}

Eq. {eq}`advdifi` is a 1D PDE while Eq. {eq}`advdifs` is a 1D ODE. However, a 2D stationary advection-diffusion equation as given by

$$
  u\frac{\partial c}{\partial x} + v\frac{\partial c}{\partial y} - \kappa \left ( \frac{\partial^2 c}{\partial x^2} + \frac{\partial^2 c}{\partial y^2} \right ) = 0
$$

is an elliptic PDE. Here, $v$ is the flow velocity in $y-$direction.

```

We first deals with the numerical solution of stationary advection-diffusion equation {eq}`advdifs` and then that of instationary advection-diffusion equation {eq}`advdifi` in separate sections.
In particular we dive into the role and the meaning of central differences and the first order upwind scheme with respect to the numerical solution of the particular PDE.
In this context, we will explore the common phenomena like **wiggles** and **numerical diffusion**.

Wiggles are a numerical artifact caused by central differences and numerical diffusion is typically created by the first order upwind scheme.
In this section, we will explore how to reduce wiggles through diffusion, either physical and/or numerical.

```{note} 

**The learning objectives of this section are:**
- formulate and discretize the advection-diffusion equation using central differences and the first order upwind scheme
- explain the notions of wiggles and numerical diffusion
- describe the role of the mesh P&eacute;clet number
- discuss the possibilities to reduce wiggles

```

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
proportional to the square root of $\kappa$. To accurately solve this boundary layer, a local mesh refinement is often necessary.

Based on accuracy reasons, we choose central differences for both advective and diffusive processes, as follows

$$
  u\frac{c_{m+1}-c_{m-1}}{2\Delta x} - \kappa \frac{c_{m+1}-2c_m+c_{m-1}}{\Delta x^2} = 0\, , \quad m = 1,\ldots,M-1
$$ (statcveq)

:::{card} Exercise

Verify this approximation and show that $\tau_{\Delta x} = \mathcal{O}(\Delta x^2)$.

:::

The boundary conditions are simply discretized as follows

$$
  c_0 = 0 \, , \quad c_M = 1
$$

A peculiar feature of central differences applied to the first derivative $\partial c/\partial x$ (or generally, the advection term) is that they are
prone to generate **spurious oscillations** or **wiggles**, especially near steep gradients.
This renders the numerical solution physically meaningless. The way to counteract these wiggles is to add some diffusion.
The effect of this diffusion process is to smear out these irregularities.
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
In this case, $P_{\Delta} > 2$ which implies that the current amount of physical diffusion is not sufficient to prevent wiggles.

```{figure} https://files.mude.citg.tudelft.nl/cvcentral.png
---
scale: 75%
name: cvcentral
align: center
---
Solution obtained with central differences and $\Delta x = 0.1$ m.
```

A simple remedy would be to decrease the mesh size $\Delta x$ such that restriction {eq}`restpc` is fulfilled. This is
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

In practice, this increase of mesh resolution can be a severe one.
Another remedy would be to apply the first order upwind scheme. This is explained in the following way.

In general, **numerical diffusion** arises from a first order finite difference scheme to the spatial derivative $\partial c/\partial x$.
To see this why this is so, recall the Taylor series expansion of $c(x_{m+1})$:

$$
  c(x_{m+1}) = c(x_m) + \Delta x\, \frac{\partial c}{\partial x}(x_m) + \frac 12 \Delta x^2\, \frac{\partial^2 c}{\partial x^2}(x_m) + \text{ HOT}
$$

where HOT stands for higher order terms. Now the first derivative at point $x_m$ can be written as

$$
  \frac{\partial c}{\partial x} = \frac{c(x_{m+1}) - c(x_m)}{\Delta x} - \frac 12 \Delta x\, \frac{\partial^2 c}{\partial x^2} + \text{ HOT}
$$

Here, we have expressed the exact first derivative by the first order forward difference formula plus higher order terms.

Now, let us consider the following advection equation at point $x_m$:

$$
  \frac{\partial c}{\partial t}(x_m) + u\frac{\partial c}{\partial x}(x_m) = 0
$$

and then replace the first derivative by the first order differences above while moving the higher order terms to the right hand side, as follows

$$
  \frac{\partial c}{\partial t}(x_m) + u\frac{c(x_{m+1}) - c(x_m)}{\Delta x}  - \kappa_a \, \frac{\partial^2 c}{\partial x^2}(x_m) = \text{HOT}
$$

where

$$
  \kappa_a = \frac{u\,\Delta x}{2}
$$

is the diffusion coefficient associated with the first order differences. This amount of diffusion has no physical meaning and is therefore called
**numerical diffusion**.

We conclude that the original diffusion-free PDE has been converted into an advection-diffusion PDE due to truncation error.
Since the amount of numerical diffusion $\kappa_a$ is proportional to $\Delta x$, this amount cannot be neglected, that is,
the term $\kappa_a c_{xx}$ cannot be considered as a negligible truncation error.

Below we will demonstrate that the first order upwind scheme generates sufficient amount of numerical diffusion so that wiggles are prevented.
Let us assume $u>0$. Hence, we have the following discretized equation for internal points $m = 1,\cdots,M-1$,

$$
  u\frac{c_m-c_{m-1}}{\Delta x} - \kappa \frac{c_{m+1}-2c_m+c_{m-1}}{\Delta x^2} = 0
$$ (statcveq2)

:::{card} Exercise

Verify this approximation and show that $\tau_{\Delta x} = \mathcal{O}(\Delta x)$.

:::


The corresponding characteristic equation is given by

$$
  r^2 - (P_{\Delta} +2) \, r + P_{\Delta}+1 = 0
$$

and its roots are

$$
  r_1 = 1\, , \quad r_2 = 1+P_{\Delta}
$$

Hence, both roots are always non-negative ($P_{\Delta}>0$ since $u>0$) and the numerical solution will not display any oscillations, irrespective of the value of $P_{\Delta}$.

Precautions should be taken so that the numerical diffusion will not dominate the physical one, that is, $\kappa_a < \kappa$.
Otherwise, the first order upwind scheme is then considered to be too dissipative. In practice, this means mesh refinement if desired.

Let us recall the above example with $u = 1$ m/s, $\kappa = 0.025$ m$^2$/s and $\Delta x = 0.1$ m, implying $P_{\Delta} = 4$. Hence, the amount of numerical diffusion equals
$\kappa_a = 0.5 \times 1 \times 0.1 = 0.05$ m$^2$/s which is twice larger than the physical one. The numerical solution is depicted below which shows that it is rather inaccurate.
Note that the boundary layer thickness of the numerical solution is larger than that of the exact one due to numerical diffusion.

```{figure} https://files.mude.citg.tudelft.nl/cvupwind.png
---
scale: 75%
name: cvupwind
align: center
---
Solution obtained with the first order upwind scheme and $\Delta x = 0.1$ m so that $\kappa_a = 0.05$ m$^2$/s.
```

Now, let us see what happen if we refine the grid four times, so that $\Delta x = 0.025$ m. Hence, $\kappa_a = 0.0125 < \kappa = 0.025$ m$^2$/s. The numerical solution is plotted below.

```{figure} https://files.mude.citg.tudelft.nl/cvupwind2.png
---
scale: 75%
name: cvupwind2
align: center
---
Solution obtained with the first order upwind scheme and $\Delta x = 0.025$ m.
```

Although the solution is much more accurate (cf. {numref}`cvupwind`), it is still less accurate compared to central differences (cf. {numref}`cvcentral2`).
This is explained by the fact that scheme {eq}`statcveq2` is only first order accurate, so that the numerical solution converges slower to the exact solution.

We may perhaps conclude that it is wiser to prefer central differences over the first order upwind scheme provided the grid is sufficiently fine, at least for linear
advection-diffusion equations. In practice, however, we see that upwind schemes are a much more robust alternative for nonlinear problems (such as the
Navier-Stokes or shallow water equations) despite being generally less accurate.

## Instationary advection-diffusion equation

We consider the following 1D initial boundary value problem

$$
  \begin{align}
    &\frac{\partial c}{\partial t} + u\frac{\partial c}{\partial x} - \kappa\frac{\partial^2 c}{\partial x^2} = 0\, , \quad 0 < x < 1 \, , \quad t > 0 \\
    &\\
    &c(x,0) = 0\, , \quad 0 \leq x \leq 1 \\
    &\\
    &c(0,t) = 0\, , \quad t > 0 \\
    &\\
    &c(1,t) = 1\, , \quad t > 0
  \end{align}
$$ (instatcv1)

Again, we assume that the constituent $c(x,t)$ is sufficiently smooth. The solution to this problem is called **transient** and in the limit, $t \to \infty$,
a steady state solution may be obtained. This is the case when the boundary conditions are time independent.
This is also the solution to the stationary problem  {eq}`statcv1`.

For the discretization of {eq}`instatcv1`, we employ the MOL approach. Again, we may choose central differences. The semi-discretized equation reads

$$
  \frac{dc_m}{dt} + u\frac{c_{m+1}-c_{m-1}}{2\Delta x} - \kappa \frac{c_{m+1}-2c_m+c_{m-1}}{\Delta x^2} = 0\, , \quad m = 1,\ldots,M-1\, , \quad t > 0
$$

A commonly time integration method would be the explicit Euler method. Thus, we obtain the following discretized equation
for the instationary convection-diffusion equation {eq}`instatcv1`,

$$
  \frac{c^{n+1}_m-c^n_m}{\Delta t} + u\frac{c^n_{m+1}-c^n_{m-1}}{2\Delta x} - \kappa \frac{c^n_{m+1}-2c^n_m+c^n_{m-1}}{\Delta x^2} = 0\, , \quad m = 1,\ldots,M-1\, , \quad n=0,1,2,\ldots
$$ (ftcsadvdif)

This scheme is first order accurate in time but second order in space. Furthermore, it is explicit and thus conditionally stable.
By requiring non-negative solutions we may find some stability conditions. We rewrite the discretized equation as

$$
  c^{n+1}_m = (q - \frac 12 \sigma) c^n_{m+1} + (1-2q) c^n_m + (q + \frac 12 \sigma) c^n_{m-1}
$$

with $q = \kappa \,\Delta t/\Delta x^2$ and $\sigma = u\,\Delta t/\Delta x$.

and by induction, we assume that $c^n_m \geq 0$ for $m=0,\ldots,M$. To have $c^{n+1}_m \geq 0$, the following conditions must be met

$$
   \boxed{
          q \leq \frac 12 \, , \quad |P_{\Delta}| \leq 2
         }
$$

:::{card} Exercise
Verify these conditions.

```{admonition} Solution
:class: tip, dropdown

First, we rewrite {eq}`ftcsadvdif` to express the unknown at the new time step $n+1$ into the unknowns at the present time step $n$, using the numerical parameters $q$ and $\sigma$, as follows

$$
  c^{n+1}_m = c^n_m - \frac 12 \sigma \left (c^n_{m+1}-c^n_{m-1} \right) + q \left( c^n_{m+1}-2c^n_m+c^n_{m-1} \right )
$$

Further rewriting by grouping the terms with the same unknown,

$$
  c^{n+1}_m = \left ( 1 -2q \right ) c^n_m + \left ( q - \frac 12 \sigma \right ) c^n_{m+1} + \left ( q + \frac 12 \sigma \right ) c^n_{m-1}
$$

Now, assume that $c^n_m \geq 0$, $c^n_{m+1} \geq 0$ and $c^n_{m-1} \geq 0$, then the coefficients $1 -2q$, $q - \frac 12 \sigma$ and $q + \frac 12 \sigma$ must be non-negative in order to get $c^{n+1}_m \geq 0$.
Hence,

$$
  1-2q \geq 0 \quad \Rightarrow \quad q \leq \frac 12
$$

Note that

$$
  \frac{\sigma}{q} = P_{\Delta}
$$

so that

$$
  q - \frac 12 \sigma \geq 0 \quad \Rightarrow \quad P_{\Delta} \leq 2
$$

and

$$
  q + \frac 12 \sigma \geq 0 \quad \Rightarrow \quad -2 \leq P_{\Delta}
$$

```
:::

The first condition is recognized as the stability condition for the heat equation while the second one is the condition that we have found for the stationary advection-diffusion equation.

Instead of explicit Euler we may choose the implicit Euler scheme and regarding the advection term, we may choose a first order upwind scheme instead of central differences.
