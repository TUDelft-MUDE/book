# Elements and shape functions

So far you have seen simple linear shape functions and elements that are defined over a 1D subdomain with two nodes. Most applications of the finite element method are not in 1D but in 2D or 3D. In higher dimensional space, the same key concepts can be used. The central idea is that the solution space is reduced with the introduction of shape functions. This can also be done for 2D or 3D fields. 

Another important feature of the finite element method is that it allows for higher order approximations. In finite difference and finite volume schemes it can be shown that their spatial discretization is second order accurate, i.e. there is an error in the solution that is of the order ($\Delta x^2$). With the concept of shape functions it is possible to improve the order of accuracy of the spatial discretization. 

In summary, there are two directions in which we can generalize the finite element method by choosing different shape functions
- Increasing the dimensionality
- Increasing the interpolation order 

In this section, we will start with the second of these. 


```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/pywJkVwAZJA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Recap of linear shape function 

The linear shape functions are visualized once more in {numref}`line2funcs`. They can be interpreted as global functions (left image), but are typically evaluated and implemented element-by-element (right image). In the figure, there are five nodes and four elements. The two shape functions in every element are each equal to 1 at one of the nodes and equal to 0 at the others. 

:::{card}
```{figure} https://files.mude.citg.tudelft.nl/lineFuncs-1.png
---
name: line2funcs
---
Linear shape functions as global functions (left) and element-by-element (right)
```
:::

Inside the element, each of the two shape functions takes the form

$$
N_i = a_i + b_ix
$$

With the coordinates of the nodes it is possible to find the coefficients $a_i$ and $b_i$ for each shape function that makes it go from 0 to 1 over the element domain. However, as you have seen in the implementation, they are often evaluated in a local coordinate frame. 

## Shape function properties

The linear shape functions we have discussed so far have two properties that hold for most finite element shape functions:

:::{card} Partition of unity

$$ 
\sum N_i(x) = 1$$

The sum of the shape functions is equal to one at every position inside the element. This is essential for ability to describe trivial constant solutions exactly. 
:::

:::{card} Kronecker delta property

$$
N_i(x_j) = \begin{cases} 
  1, & i = j \\
  0, & i\neq j
\end{cases}
$$

Every shape function is equal to one at one of the nodes and equal to zero at all other nodes. This is helpful for the interpretation of the degrees of freedom of the solution vector as nodal values. 
:::


## Higher order shape functions

To improve the quality of the approximation, it is possible to introduce more nodes. The solution will converge to the exact solution. However, it is possible to make it converge faster and that is by increasing the polynomial order of the shape functions. Similar to the linear shape functions, quadratic shape functions can be introduced, see {numref}`line3funcs`. The approximate solution is then not piecewise linear as we have seen so far, but piecewise quadratic. 

:::{card}
```{figure} https://files.mude.citg.tudelft.nl/lineFuncs-2.png
---
name: line3funcs
---
Quadratic shape functions as global functions (left) and element-by-element (right)
```
:::

In the 1D discretization of 5 nodes, now 2 elements can be identified with 3 nodes each. Inside the elements three parabolic functions are defined that still have the property that they each are equal to 1 at one of the nodes and equal to 0 at the other nodes. This can be written compactly as

The general form of the quadratic shape functions is

$$
N_i = a_i + b_ix + c_ix^2
$$

You may notice that the Kronecker delta property gives three equations for each shape function (e.g. for $N_1$ we have $N_1(x_1)=1$, $N_1(x_2)=0$ and $N_1(x_3)=0$). For given coordinates $x_1, x_2, x_3$, the coefficients $a_i, b_i, c_i$ are uniquely determined for each of the three shape functions. 

## Finite elements shape functions in two dimensions

For 2D problems we seek the solution of a PDE defined over a two-dimensional domain $u(x,y)$. Shape functions still play a central role: the solution space is restricted by stating that it must be a linear combination of a set of shape functions.  Now, the shape functions are functions defined over the two-dimensional domain. The approximate solution $u^h(x,y)$ is constructed by interpolating the nodal values $u_i$ with their corresponding shape function $N_i(x,y)$:

$$ 
u^h(x,y) = \sum_{i=1}^{n_\text{nodes}} N_i(x,y)u_i
$$

Again, the nodal values $u_i$ are sought that provides a solution $u^h$ that best satisfy the governing equation by substituting the discretized solution into the weak form equation. 

For two-dimensional analysis, finite element meshes of usually consist in quadrilaterals and/or triangles. Triangular elements are superior for constructing unstructured meshes on complex geometries, whereas quadrilaterals are useful for structured meshes. In both cases, linear and quadratic versions exist. 

## Shape functions on a triangular element

The simplest 2D element is a 3-node triangle (see {numref}`triangleFuncs`). The shape function of the 3-node triangle is defined as:

$$ 
N_i = a_i + b_ix + c_iy
$$

where the coefficients $a_i$, $b_i$ and $c_i$ depend on the coordinates of the element. Again, for given coordinates, the Kronecker delta properties defines what the values of the coefficients should be for the shape functions of an element. 

:::{card}
```{figure} https://files.mude.citg.tudelft.nl/triangleFuncs.png
---
name: triangleFuncs
---
Shape functons for 3-node triangular element
```
:::


Triangles with quadratic shape functions have 6 nodes, 3 at each corner and 3 at the middle of each edge. The shape functions are written as:

$$
N_i = a_i + b_ix + c_iy + d_ix^2 + e_ixy + f_iy^2
$$


## Shape functions on a quadrilateral element

Shape functions on quadrilateral elements can be understood as the product of 1D shape functions in the two principal directions of the element. The lowest order quadrilateral element has 4 nodes, one at each corner of the element. The shape function are obtained by multiplying linear shape functions in $x$ direction with linear shape functions in $y$ direction. The resulting shape functions are *bilinear*, the are linear in the coordinates except for a cross term $xy$. In general the shape functions on the 4-node element take the shape:

$$ 
N_i = a_i + b_ix + c_iy + d_ixy
$$

:::{card}
```{figure} https://files.mude.citg.tudelft.nl/quadFuncs-1.png
---
name: quad4Funcs
---
The 4-node quadrilateral element
```
:::

Quadratic shape functions for a 9-node quadrilateral element can be constructed by multiplying the shape functions of the 3-node line element in two different directions. The shape function is expressed as:

$$
N_i=a_i+b_ix+c_iy+d_ix^2+e_ixy+f_iy^2+g_ix^2y+h_ixy^2+j_ix^2y^2
$$

:::{card}
```{figure} https://files.mude.citg.tudelft.nl/quadFuncs-2.png
---
name: quad4Funcs
---
The 9-node quadrilateral element
```
:::

A popular alternative is one where the center node is removed, resulting in an 8-node quadrilateral element with the following shape function:

$$
N_i=a_i+b_ix+c_iy+d_ix^2+e_ixy+f_iy^2+g_ix^2y+h_ixy^2
$$


## Shape functions in 3D

For 3D problems, the solution is defined over a three-dimensional domain. The shape functions are as well. The mesh is then constructed with tetrahedral or hexehedral elements. The 4-node tetrahedral element has shape functions that are a generalization of the triangle with only linear terms: 

$$ 
N_i = a_i + b_ix + c_iy + d_iz
$$

The hexahedral element is like a 3D version of the quadrilateral element. The 8-node hexahedral element has mixed terms and is thus called *trilinear*:

$$
N_i=a_i+b_ix+c_iy+d_iz+e_ixy+f_ixz+g_iyz+h_ixyz
$$


:::{card}
```{figure} https://files.mude.citg.tudelft.nl/3dElements.png
---
name: 3dElements
---
3D elements: hexahedral (left) and tetrahedral (right)
```
:::
