$\newcommand{\beps}{\boldsymbol\varepsilon}$
$\newcommand{\bsig}{\boldsymbol\sigma}$
$\newcommand{\ud}{d}$
$\newcommand{\us}{\mathrm{s}}$
$\newcommand{\ba}{\mathbf{a}}$
$\newcommand{\bb}{\mathbf{b}}$
$\newcommand{\bc}{\mathbf{c}}$
$\newcommand{\bt}{\mathbf{t}}$
$\newcommand{\bu}{\mathbf{u}}$
$\newcommand{\bw}{\mathbf{w}}$
$\newcommand{\bN}{\mathbf{N}}$
$\newcommand{\bB}{\mathbf{B}}$
$\newcommand{\bD}{\mathbf{D}}$
$\newcommand{\bK}{\mathbf{K}}$
$\newcommand{\pder}[2]{\frac{\partial #1}{\partial #2}}$
$\newcommand{\iD}{\boldsymbol{\mathcal{D}}}$


# Poisson equation in 2D

In this section, we will introduce finite element formulations for problems in higher dimensions. Again, we will focus on the Poisson equation, but not in 2D. In this problem, the solution is a field in 2D space. This implies the elements and shape functions need to be different (e.g. triangular, quadrilateral, tetrahedral). 

```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/LO26k4ep8pg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Strong form equation 

The 2D Poisson equation describes the steady state (time-independent solution) of a diffusion problem.

$$-\nu \left(\frac{\partial^{2} u}{{\partial x}^{2}} + \frac{\partial^{2} u}{{\partial y}^{2}}\right) = q$$ (poisson2d)

Where $u$ is the unknown field, $\nu$ is the diffusivity parameter and $q$ is a source term. At least $u$ and possibly also $\nu$ and $q$ are a function of $x$ and $y$. 

There are several applications where this PDE can be used to solve problems in sciences and engineering, such as:
- potential flow
- pressure in saturated soil
- temperature distribution in solids

Equation {eq}`poisson2d` can be written with the Laplacian operator $\Delta = \nabla\cdot\nabla$ as 

$$ -\nu\Delta u = q $$

To formulate a problem the strong form governing equation is combined with boundary conditions

$$
u = \bar{u},\quad \text{on} \quad \Gamma_D \\
\nu\nabla u\cdot\mathbf{n} = h \quad \text{on} \quad \Gamma_N
$$

where $\bar{u}$ stands for prescribed values for the unknown field on the part of the boundary where Dirichlet boundary conditions are applied ($\Gamma_D$) and $h$ for a flux on the part of the boundary where Neumann boundary conditions are applied ($\Gamma_N$) and $\mathbf{n}$ is the normal to that boundary. 




## Weak form

As usual, we start with multiplying the strong form equation with a (for now arbirtary) test function and integrating over the domain

$$
-\int_\Omega w\nu \Delta u\,d\Omega = \int_\Omega wq\,d\Omega
$$(weighted-poisson-2d)

Integration by parts in combination with Divergence theorem gives:

$$
\int_\Omega \nabla w\cdot(\nu\nabla u)\,d\Omega  - \int_{\Gamma} w\nu\nabla u\cdot\mathbf{n}\,d\Gamma = \int_\Omega wq\,d\Omega
$$

```{admonition} Integration by parts / Divergence theorem
:class: dropdown
For the step above, we make use of two fundamental relations. Firstly the product rule of differentation for divergence (with scalar $a$ and vector $\mathbf{b}$) which reads:

$$
\nabla\cdot(a\mathbf{b}) =  a\nabla\cdot\mathbf{b} + \nabla a\cdot\mathbf{b} 
$$(product-rule-div)

And secondly, divergence theorom, which reads (with vector $\mathbf{v}$)

$$
\int_\Omega \nabla\cdot\mathbf{v}\,d\Omega = \int_\Gamma \mathbf{v}\cdot\mathbf{n}\,d\Gamma
$$(divergence-theorem)

With {eq}`product-rule-div`, we rewrite the left hand side of Equation {eq}`weighted-poisson-2d` (with $w$ for $a$ and $\nabla u$ for $\mathbf{v}$). Then with {eq}`divergence-theorem` (with $w\nabla u$ for $\mathbf{v}$), we rewrite the second integral into a surface integral

```

Substitution of the Neumann boundary in combination with the condition that $w=0$ on $\Gamma_D$ eliminates the unknown $u$ from the boundary term, after which it is moved to the right hand side to arrive at the weak form equation:

$$
\int_\Omega \nabla w\cdot(\nu\nabla u)\,d\Omega = \int_\Omega wq\,d\Omega + \int_{\Gamma_N} wh\,d\Gamma 
$$(poisson2d-weak)

## Discrete form

Discretization of the solution is done with 2D shape functions

$$
u \approx u^h = \sum_j N_j(x,y) u_j = \mathbf{Nu}
$$

where $\textbf{u}$ contains the degrees of freedom of the discretized field and $\bN$ is a row vector with all shape functions:

$$  \textbf{N} = \begin{bmatrix}  N_1  & N_2 &... & N_{n} \end{bmatrix}$$

in which $n$ is the number of degrees of freedom, which is for conventional shape functions equal to the number of nodes in the mesh. 

Following the Bubnov-Galerkin method, the same discretization is introduced for $w$:

$$
w \approx w^h = \mathbf{Nw}
$$

The gradients of $u$ and $w$ are defined with the $\bB$-matrix as:

$$
\nabla{u} = \mathbf{Bu} \qquad \text{and} \qquad \nabla{w} = \mathbf{Bw} 
$$

with

$$
\bB = \begin{bmatrix} \frac{\partial N_1}{\partial x}, \frac{\partial N_2}{\partial x}, \ldots, \frac{\partial N_{n}}{\partial x} \\ \frac{\partial N_1}{\partial y}, \frac{\partial N_2}{\partial y}, \ldots, \frac{\partial N_{n}}{\partial y} \end{bmatrix}
$$

Substitution into Equation {eq}`poisson2d-weak` gives

$$
\int_\Omega \mathbf{Bw}\nu \mathbf{Bu}\,d\Omega = \int_\Omega \mathbf{Nw}q\,d\Omega + \int_{\Gamma_N} \mathbf{Nw}h\,d\Gamma
$$

As for the 1D problem, eliminating $\bw$ involves transposing $\bN$ and $\bB$ matrices where they are multiplied with $\bw$. Finally, we arrive at a linear system of equations written as:

$$
\mathbf{Ku} = \mathbf{f}
$$

with

$$
\bK = \int_\Omega \bB^T\nu \bB\,d\Omega \qquad \text{and} \qquad \mathbf{f} = \int_\Omega \bN^Tq\,d\Omega + \int_{\Gamma_N} \bN^Th\,d\Gamma
$$


```{admonition} Poisson equation in 1D vs 2D vs 3D
The finite element derivation for the Poisson equation in 2D follows the same lines as the in 1D. We need Divergence theorem now to arrive at the term where Neumann boundary conditions are applied. This is now an integral over the boundary instead of a term evaluated at the ends of the rod. 

The derivation above also holds for 3D. Expressions and steps are exactly the same, although the interpretation of some of the symbols changes:  in 3D, $\Omega$ is a volume, $\Gamma$ is a surface and the $\bB$ matrix has three rows.
```


