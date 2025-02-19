# Introduction to finite elements

In this chapter we will introduce all the steps that are usually followed to solve a PDE using the finite element method, from the definition of the PDE to the solution of a linear system of equations. To make the learning curve ease, we focus on the simplest PDE for finite elements: the Poisson equation, first in 1D and then in 2D. Note that the laplacian operator with second derivatives in space that appears in th Poisson equation is an ingredient in many different engineering problems, so this is not only a convenient place to start but also a fundamental one.  

The general goal of the finite element method is to convert PDEs into a form which we, or rather a computer, can solve. The reason for doing this is because it allows a PDE with no analytical solution for the full domain, to be approximated by solving it on smaller 'elements'. This *discretization* into several elements enables us to solve the problems in irregular geometries, different materials, dynamic effects, jumps or complex changes in geometry, while the resulting formulation is well generalizable to nonlinear problems of different kinds.

We will first show the main steps of the derivation of the finite element formulation:
1. Starting point is a PDE with boundary conditions, the [strong form](./strong.md) of the problem 
2. From the strong form, derive the [weak form](./weak.md)
3. Substitute an assumed discretization into the weak form to arrive at the [discrete form](./discrete.ipynb) 

Then we will show a simple single-purpose implementation of the finite element method for the 1D Poisson equation

4. A [finite element implementation](./matrix.ipynb) translates the equations to code

In subsequent sections, key concepts of general finite element implementations are discussed: 

5. The definition of [shape functions](./shape.md)  which played a key role in the discretization step
6. [Numerical integration](./numerical_integration.md) for evaluating the integrals that are present in the discrete form
7. The derivation is repeated for the [Poisson equation in 2D](./poisson2d.md)
8. The concept of [isoparametric mapping](./isoparametric_mapping.md) for generalization to unstructured meshes


