# Strong form of the 1D Poisson equation

The *strong from* of the problem is a Partial Differential Equation (PDE), or a set of PDEs, describing the physics of the phenomena at hand, supplemented with appropriate boundary and initial conditions. Solving the strong form of the problem leads to the exact solution of the continuous system. However, for many engineering problems, it is not possible to obtain the exact solution, and numerical methods need to be employed to find an approximate solution. The finite element method is one approach to find approximate solutions that is applicable to a wide range of different problems. In this chapter we will focus on problems for which the strong form is the Poisson equation. 

The story told below and up to the [discrete form](./discrete.ipynb) section is also presented in this video: 

```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/VNfRdJdcSKM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

##  1D Poisson equation
At this point, let's take as an example the one dimensional Poisson equation to illustrate at first the so-called strong form of the problem:

$$
-\frac{\partial}{\partial x} \left(\nu(x) \frac{\partial u(x)}{{\partial x}}\right) = f(x)
$$ (1Dpoissonequation)

where $\nu(x)$ is a material property, $u(x)$ the solution and $f(x)$ a source, all of which can depend on the coordinate $x$. To simplify notation we will omit the $x$-dependence and write $\nu$, $u$ and $f$ in what follows.

Equation {eq}`1Dpoissonequation` can be used to express various physical phenomena such as steady-state heat conduction, elastic deformation of a rod or flow in a permeable media (such as Darcy’s law).

Alternatively, the Poisson equation can be written as: 

$$ 
−\frac{\partial}{\partial x} \Lambda + f = 0 
$$ (generalpoisson)

where $\Lambda$ is a flux term, of which the interpretation depends on the problem at hand. In the case of heat conductivity, $\Lambda$ is the heat flux, while in Darcy’s law, $\Lambda$ is the flow rate, and in extension of a rod, $\Lambda$ is the stress. The typical constitutive relationship between the flux $\Lambda$ and the unknown solution $u$ is given by:

$$ 
\Lambda=-\nu \frac{\partial u}{\partial x}
$$ (constitutive)

In the case of heat conduction, for instance, $u$ in the above equation is the temperature. In the case of a structural problem, $u$ would be the displacement. For Darcy’s law, $u$ is the hydraulic head. 

Keep in mind that the constitutive relationship always depends on the problem being solved and $ \nu $ can take different meanings. For the heat equation, $\nu$ is the thermal conductivity while for Darcy’s law $ \nu $ is the hydraulic conductivity and for extension of a rod $\nu$ is a measure for the stiffness. 

## The strong form of a linear elastic rod
```{figure} https://files.mude.citg.tudelft.nl/barDefinition-1.png
---
height: 150px
name: rodDefinition
---
One dimensional rod with distributed load
```

An application of the Poisson equation is the extension of one-dimensional structural elements. Let us consider a horizontal steel rod with length $L$, stiffness $EA$ and distributed load $f(x)$. This equilibrium problem can be described with the following differential equation:


$$
-\frac{\partial}{\partial x}\left(EA \frac{\partial u}{\partial x}\right) = f
$$ (1drod)

where $u$ is the displacement of the rod as function of location $x$. For constant $EA$, this can be simplified to

$$
-EA \frac{\partial^2 u}{\partial x^2} = f
$$ (1drodsimplified)


We also consider as **boundary conditions** that the rod is fixed at the left end and loaded with a force $F$ at the right end:

$$
u = 0, \quad \text{at} \quad x = 0 \\
EA\frac{\partial u}{{\partial x}} = F, \quad \text{at} \quad x = L
$$ (1drodBCs)

As can be seen, the form of equation {eq}`1drod` is exactly the same as the 1D Poisson equation shown above. The only difference is in the physical interpretation of $u$ and $f$ and that instead of the constant $\nu$ we use the constant $EA$ (Young's modulus $E$ times cross section area $A$) to describe the stiffness. The exact same mathematical problem could be interpreted as a heat conduction problem. 

:::{card} Quiz question
<iframe src="https://tudelft.h5p.com/content/1292102761306552137/embed" aria-label="Boundary conditions for heat equation" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>
:::

