(multivar_design)=
# Practical Applications: Designing with Probability

% MMMMM This material is not in R&R book

This chapter is closed with an illustration of how our probability models can be used in practice, specifically in the **design** of some object or system. As engineers making decisions under uncertain conditions (i.e., the unknown values of our random variables) we face a serious conundrum[^conundrum]: our design must specify a deterministic value, which will eventually be used to build the object or system of interest. In the face of uncertainty, this means there will _always_ be a non-zero probability that the object or system can fail! Thus, the choice is not simply how robust to design somthing, but rather: how safe should it be designed. In other words, _what is an acceptable probability of failure for the design?_

This question can be answered by applying the concepts of risk and risk analysis, which will be covered in a later chapter. For now, we will assume that an _acceptable failure probability_ has been determined and use our probability models to evaluate what the _design value_ should be.

## Discrete Events

Previous sections in this chapter introduced multivariate distributions and, specifically, a few approaches for incorporating _dependence_ in our probabilistic assessment of more than one random variable of interest. Until this point, examples have been illustrated using a simple paradigm: "AND" and "OR" probabilities (analogous to intersection and union in set theory), where each random variable is assumed to have a critical or threshold case with some probability of exceedance, p, for example (if $X_1$ has the lognormal distribution):

$$
X_1\sim \mathrm{LN}(\mu, \sigma) \;\;
\rightarrow \;\;
P[X_1 \leq x_{threshold}] = 1 - F_{X_1}(x_{threshold})
$$

However, for the two random variable case, this limits us to only a few relevant design situations: the various combinations where each variable is either greater than or less than a threshold value. This is very restrictive in practice. Fortunately we already have a tool at hand for evaluating more complex situations: the concept of **functions of random variables**!

## Functions of Random Variables

Given a vector of random variables $X$ and function $q$, the output, $Y$, is a function of random variables:

$$
Y = q(X)
$$

While $Y$ is itself a random variable, its distribution is known only for a few special cases, for example, if $q$ is linear and $X$ is the multivariate Gaussian, then $Y$ is also Gaussian. This is no longer true if the function is non-linear or the marginal distributions of the random variables are non-Gaussian. Luckily we are usually able to empirically find the distribution of $Y$ using _Monte Carlo Sampling._

It is important also to note that although the distribution of $Y$ is univariate, it is related to the underlying multivariate distribution of $X$ via the function $q$. As such, the model chosen for $f_X(x)$ will have an impact on the distribution of $Y$.

```{tip}
In some fields, for example structural reliability and related branches of civil engineering, it is common to formulate the function of random variables as a _limit state function,_ where the _threshold_ value of the function dividing a _safe_ and _failed_ state is found. The function is then reformulated as a new function, $g$ with output $Z$ is defined such that 0 defines the threshold state and negative values the failed state. The probability of being in the failed state, $p_f$, is found as follows:

$$
Z = g(X)
\;\; \rightarrow \;\;
p_f = P[Z\leq0]
$$

```

Regardless of the underlying multivariate distribution of the input random variables, the task at hand is to compute the design value, $y_{design}$, for a given probability of interest, $p_{design}$:

$$
y_{design} = F_Y^{-1}(p_{design})
$$

where $F_Y^{-1}$ is the inverse CDF of the distribution of $Y$. Although we rarely know the exact distribution of $Y$, it is straightforward to compute the design value using Monte Carlo Simulation.

## Next Steps

The following pages work through an example related to flooding on a river to illustrate the role that the random variable inputs of a function of random variables have on . Specifically, the following pages will:

1. Consider a univariate design case for the discharge capacity of a flood protection system on a river.
2. Consider a bivariate design case where two rivers contribute to flooding and make the distinction between AND and OR perspectives explicit.
%3. Illustrate the effect of various marginal distributions and dependence models on the results through examples and exercises.

[^conundrum]: a confusing and difficult problem or question (source: Oxford Languages, via Google).