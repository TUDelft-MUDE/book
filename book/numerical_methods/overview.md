(numerical_modelling)=
# Numerical Modelling

% START-CREDIT
% source: numerical_modelling
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Jaime Arriaga Garcia, Anna Störiko, Justin Pittman and Robert Lanzafame. {ref}`Find out more here <numerical_modelling_credit>`.
```
% END-CREDIT

In the earth sciences, civil engineering and environmental engineering, processes and systems are often described by models based on differential equations.
These equations involve derivatives of the states we are interested in, for example with respect to time and space.
Some examples of phenomena in these fields modeled by differential equations are:

- flow of water or heat through the subsurface,
- the distribution of stresses in solid structures,
- pollutant dispersion in the air and water,
- traffic dynamics in an urban region,
- chemical reactions and microbial processes, e.g. in waste water.

While simple differential equations can be solved analytically, real-word situations often lead equations that cannot be solved exactly, for example because of complex geometries, spatially variable parameters or difficult non-linear terms.
In these cases, we need to approximate the solution of the equation numerically.
The animation in {numref}`NumericalMethodsRiver` illustrates how the output from such a complex numerical simulation can look like.

This chapter is about the fundamentals of numerical modelling and basic numerical methods.
For example, we will look into how we can approximate derivatives and integrals numerically.
The main focus is on solution methods for ordinary differential equations (ODE) of varying orders.
Numerical approaches for solving partial differential equations (PDE) will be introduced in another chapter of this book.

% MMMMM the following gif is large (30MB) and is manually added to server at the URL location below to prevent the book from becoming too large.

% START-CREDIT
% source: numerical_modelling
````{margin}
```{attributiongrey} Attribution
:class: attribution
This figure was made by Amgad Omer of Deltares. {ref}`Find out more here <numerical_modelling_credit>`.
```
````
% END-CREDIT

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/NumericalMethodsRiver.gif
:name: NumericalMethodsRiver

Numerical simulation of morphology in the Jamuna river. Included here with permission of Amgad Omer of Deltares. {ref}`Find out more here <numerical_modelling_credit>`

```



