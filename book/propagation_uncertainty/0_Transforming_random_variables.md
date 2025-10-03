(01_errorprop)=
# Transforming random variables

Let us take the simple example of converting temperature measurements taken in degrees Celsius to degrees Fahrenheit. This transformation is represented by a simple linear function 

$$
T_f = q(T_c) = \frac{9}{5} T_c + 32
$$

In {numref}`frv_C_F`, an example of the distribution of the average July temperature in a city is illustrated, both in degrees Celsius and degrees Fahrenheit. Due to a simple change of units, the PDF is transformed, the mean is shifted and the variance is ultimately also changed.

```{figure} https://files.mude.citg.tudelft.nl/01_Temp.png
---
height: 300px
name: frv_C_F
---
Distribution of temperature in degrees Celsius and degrees Fahrenheit.
```

The previous toy problem shows how even the simplest transformation (i.e., a linear function) can alter the distribution of output variables. However, in some cases we are not interested in evaluating the complete PDF of the output distribution, but we could limit ourselves to some principal _statistical moments_ of the distribution. Before discussing that, we provide a more general theory concerning the transformation of random variables.

```{TIP}
In the previous problem, try to think about the difference between the expected values $E{T_c}$ and $E{T_f}$. This difference is not "32" since the Celsius and Fahrenheit units have a different scale, therefore 1C° is not equivalent to 1F°!  
```

## Generic transformation of univariate functions
Let us temporarily denote random variables/vectors with an underscore symbol. We try to determine the distribution of $\underline{z} = g(\underline{x})$ given the distribution of $\underline{x}$ and the function $g$. The CDF of $\underline{z}$ is defined as 

$$
F_{\underline{z}}(z) = P(\underline{z} \leq z) = P(g(\underline{x}) \leq z) = P( \underline{x} \in I_{z} )
$$

where $I_{z} = \{x\in \mathbb{R} \; | \; g(x) \leq z\}$ is a set of all $x$ that satisfy the inequality $g(x) \leq z$ for a given $z$.

:::{card} Example $z = g(x) = ax + b$

We discriminate between three cases:

* Case $a > 0$ (i.e., $g$ is increasing)
  
  $$ 
  F_{\underline{z}}(z) = P( \underline{z} \leq z ) = P \left( \underline{x} \leq \frac{z-b}{a} \right) = F_{\underline{x}} \left( \frac{z-b}{a} \right)  
  $$

* Case $a < 0$ (i.e., $g$ is decreasing)

  $$
  F_{\underline{z}}(z) = P \left( \underline{x} \geq \frac{z-b}{a} \right) = 1 - F_{\underline{x}} \left( \frac{z-b}{a} \right)
  $$

* Case $a = 0$ (i.e., $g$ is constant)

  $$
  F_{\underline{z}}(z) = P( \underline{z} \leq z ) = 
  \begin{cases}
  1, & z \ge b,\\
  0, & z < b~.
  \end{cases}
  $$

where note that in the last case all $x$ values are mapped to the same value $b$.

:::

Ultimately, if $F_{\underline{z}}(z)$ is differentiable, we can differentiate the aforementioned expression, leading to

$$
f_{\underline{z}}(z) = \frac{d}{dz} \int_{I_z} f_{\underline{x}} (\beta) d\beta
$$

which shows in a general way how the PDF of $\underline{z}$ can be obtained from the PDF of $\underline{x}$. For specific functions monotonically increasing or decreasing in a given interval $A \subset \mathbb{R}$, it is possible to define a transformation rule to express the PDF of $\underline{z} = g(\underline{x})$ in the PDF of $\underline{x}$. 

## Remark on the multivariate case

In the multivariate case this is also possible, but this same analytic procedure becomes more complicated and involves continuous partial derivatives with non-vanishing Jacobian on $A$ and requires $f_{\underline{x}}(x)$ being continuous on $A$. This however goes beyond the scope of this course, therefore in the following sections we will focus on propagation of principal moments of the distribution, thus looking at propagation laws for Mean (first _raw_ moment) and Variance (second _central_ moment).


## Theorem (Expectation law)

For $\underline{x} \in \mathbb{R}^n$ be a $n$-dimensional random vector with continuous PDF $f_{\underline{x}}(x)$, we consider $\underline{z} = g(\underline{x})$, where $g: \mathbb{R}^n \rightarrow \mathbb{R}^m$ has continuous first partial derivatives. Then the expectation of $\underline{z}$ is

$$
E(\underline{z}) = E( g(\underline{x}) ) = \int_{\mathbb{R}^n} g(x) f_{\underline{x}}(x) dx
$$

## Corollary (Variance law)

Under the same assumptions, the variance of $\underline{z}$ is

$$
\mathrm{Var}(\underline{z}) = \mathrm{Var}( g(\underline{x}) ) = \int_{\mathbb{R}^n} [g(x) - \bar{z}][g(x) - \bar{z}]^T f_{\underline{x}}(x) dx
$$

where $\bar{z} = E( g(\underline{x}) )$, which is described in the previous Theorem.


At this point, we proceed in the following part by showing how such expressions can be simplified, e.g., via a linearization of the non-linear transformation.  

% START-CREDIT
% source: uncertainty_propagation
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Lotfi Massarweh. {ref}`Find out more here <uncertainty_propagation_credit>`.
```
% END-CREDIT
