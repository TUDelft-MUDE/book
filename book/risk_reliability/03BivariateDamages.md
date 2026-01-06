# Bivariate damage 

Consider now that we have two damages $(X,Y)$ instead of one. For example, imagine a flood event that affect two cities and generates economic losses in both. $(X,Y)$ would represent the losses in the cities. In this case, the (smoothed) risk curve becomes a risk surface, as shown in the left panel in Figure below.

```{figure} https://files.mude.citg.tudelft.nl/bivar_both_consequences.png

---

---
Risk surface for the economic consequences in city #1 and city #2: (left) 3D surface, and (right) projection.
```

A common representation of a bivariate risk surface is presented in the Table below. The information in this table, which in turn is a summary of the previous figure, can be represented by triples $〈x_i,y_j,P_{i,j} 〉$ where $P_{i,j}=P(X≥x_i  ∩ Y≥y_j  )$. In the previous example, $x_i$ and $y_j$ would be a given value for the economic consequences in the city #1 and #2, respectively.

<div align="center">

|       | $y_1$ | $y_2$ | $...$ | $y_{N-1}$| $y_{N}$ |
|-------|-------|-------|-------|-------|-------|
| $x_1$ |$P_{1,1}$ |$P_{1,2}$|$...$| $P_{1,N-1}$|$P_{1,N}$|
| $x_2$ |$P_{2,1}$ |$ P_{2,2}$| $...$ |       |       |
|    ⋮  |  ⋮     | ⋮      |  ⋮     |  ⋮     | ⋮      |
|$x_{N-1}$|$P_{N-1,1}$|$P_{N-1,2}$| $...$ |       |       |
| $x_{N}$ |  $P_{N,1}$|$P_{N,2}$| $...$ |$P_{N,N-1}$|$P_{N,N}$|

</div> 

## Multivariate damage 

When more than two damages are considered, the risk curve becomes a risk surface over a multidimensional space. Imagine that a flood affects a larger region with consequences not only to two cities but also to different infrastructures. In that case, an intuitive graphical representation as in the figure above is not possible anymore and a tabular representation becomes also inconvenient. However, the $(m+1)$-tuple representation is still a good way to summarize multivariate damages as $\langle x_{1,i_1}, x_{2,i_2}, \ldots, x_{m,i_m}, P_{i_1,i_2,\ldots,i_m} \rangle$. Notice that in this case $P_{i_1,i_2,\ldots,i_m} = P(X_1 \geq x_{1,i_1}, X_2 \geq x_{2,i_2}, \ldots, X_m \geq x_{m,i_m})$.

```{note}
In the construction that we have followed so far, **we are interested in the joint exceedance probability**, in the bivariate case $P(X_1>x_1 \cap X_2>x_2)$. However, remember that **OR probabilities might also be of interest** if we would be interested in at least one element of the system $X_i$ exceeding a certain damage level.
```
