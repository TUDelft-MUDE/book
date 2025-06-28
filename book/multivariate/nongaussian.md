
# Non-Gaussian Multivariate Distributions

The multivariate Gaussian distribution $\Phi_X(x)$ is a simple, effective and widely used approach for capturing dependence in multivariate situations. However, for continuous random variables, it has limitations due to its inability to capture:

- non-Gaussian marginal distributions
- non-linear dependence

Fortunately there are many methods available that can take this into account, for example:
- Copulas
- Vine-Copulas
- Parametric and Non-Parametric Bayesian Networks

In this chapter we will focus on the use of a Copula, which provides a simple, yet incredibly flexible way to take into account non-Gaussian marginals _and_ non-linear dependence. However, for simplicity we will stick to the Gaussian Copula, which considers _linear_ dependence, just as the Multivariate Gaussian distribution does.

## Bivariate copulas

Bivariate copulas, or just copulas, are joint distributions with uniform marginal distributions in [0, 1]. According to Sklar theorem (not provided here), any multivariate joint distribution of continuous random variables can be described as a copula, $C$, that models the dependence between the variables, where the variables are defined by univariate marginal distributions. 

```{admonition} Definition of bivariate copula
:class: tip

The definition of copula for the bivariate case is given by

$$
F_{X_1,X_2}(x_1, x_2)=C \big[F_{X_1}(x_1), F_{X_2}(x_2)\big]
$$

where $F_{X_1,X_2}(x_1, x_2)$ for $(x_1, x_2) \in \mathbb{R}^2$ is a joint distribution with marginals $F_{X_1}(x_1)$ and $F_{X_2}(x_2)$ in [0, 1] and $C$ is a copula in the unit square $I^2=([0,1] \times [0,1])$, being this equation satisfied for all $(x_1, x_2) \in \mathbb{R}^2$.

Therefore, the joint density is given as the product of the density of the copula, $c$, and the densities of the marginals as

$$
f_{X_1,X_2}(x_1, x_2) = f_{X_1}(x_1)f_{X_2}(x_2)c(F_{X_1}(x_1), F_{X_2}(x_2))
$$

```

**But what does that mean?**

When using copulas, we are going to model the univariate distributions for each variable and the dependence between them with different models. To do so, we select and fit a univariate distributions for each variable as seen in the previous chapter. That characterizes the univariate distribution of each variable or what call *marginal distributions*. 

To deal with the dependence between the random variables using copulas, we transform the observations to what we call *unity space*, *uniform space* or *pseudo observations* by means of the cumulative distribution function. This is, we will model the dependence between the non-exceedance probabilities of the random variables and not between the values of the random variables. We can perform this transformation using either the empirical cumulative distribution function or the parametric distribution functions we have fitted. 

In the figure below, in panel (a), you have observations of discharges of two rivers, $Q_1$ and $Q_2$. In panel (b) you see how we have transformed the observations to uniform space. Note that the marginal distributions in panel (b) are uniform and defined in [0,1].


```{figure} https://files.mude.citg.tudelft.nl/copula_samples_together.png

---

---
Scatter plot and histograms of the observations of $Q_1$ and $Q_2$: (a) in variable space, and (b) in uniform space.
```

This approach has several advantages when modelling joint multivariate distributions, such as:

- It improves the flexibility of the model, as we can choose different marginal distributions for each random variable, and also different to the model for the dependence.
- It helps in visualizing the dependence between the variable without the influence of the marginal distributions. This is, if you go back to the figure above and compare the shape of the scatter plot between $Q_1$ and $Q_2$, and $F_{Q_1}(q_1)$ and $F_{Q_2}(q_2)$, you can see significant differences. In panel (b), you can see how the high values of $F_{Q_1}(q_1)$ and $F_{Q_2}(q_2)$ are more correlated (the scatter is narrower) than the lower values (larger scatter). That is difficult to observe in panel (a).


When we were studying univariate distributions, we fitted parametric univariate distributions (e.g. Gaussian or Gumbel) to the empirical distribution (the observations). Here, we can do the same with copulas: we can fit a parametric copula to the observations. There are different copula families such as Gaussian, Clayton, or Gumbel, with different shapes. For instance, Gaussian copula is symmetric, while Clayton copula is not. As you can see in the Figure below, the lower values are more correlated than the higher values in Clayton copula. During the course, you will only use Gaussian copula. 


```{figure} https://files.mude.citg.tudelft.nl/examples_copulas.png

---

---
Scatter plot and histograms of the observations of $Q_1$ and $Q_2$: (a) in variable space, and (b) in uniform space.
```


```{admonition} Exam tip
:class: tip

The goal of this course is just to give you a first brief introduction to copulas. Thus, you just need to understand the concept of copula and how to compute the joint density.

You will be provided Python code to evaluate multivariate distributions constructed using Copulas.

If you want to learn more about bivariate copulas and other multivariate joint distributions in higher dimensions, you can study them in the Cross Over "MORE: Probabilistic Modelling of real-world phenomena through ObseRvations and Elicitation".

```