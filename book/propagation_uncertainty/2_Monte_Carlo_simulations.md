(01_errorprop)=
# Monte Carlo simulations for uncertainty propagation

In the previous parts we learned how a transformation of random variables lead to random outputs with a different distribution. Moreover, we also saw how to propagate **means** and **(co)variances** via linearization, including the exact linear case. Alternatively, Monte Carlo (MC) simulations are very effective tools when models are highly non-linear, or when inputs are non-Gaussian, or when we need the **full distribution** rather than just principal moments. 

```{Historic curiosity}
The **Monte Carlo** method traces its roots to early probability puzzles (e.g., Buffon’s needle), but it consolidated during the **1940s** at **Los Alamos** for **neutron transport** in the Manhattan Project. **Stanislaw Ulam** conceived the idea after card‐game thought experiments; practical algorithms and early random number routines were later developed by **John von Neumann** and **Nicholas Metropolis**. Still, the name “Monte Carlo” (Metropolis) actually nods to the Monaco casino — randomness as a computational tool. In fact, foundationally, the MC approach relies on the **law of large numbers** to estimate expectations by sampling, with examples in the 50s-60s related to **variance-reduction** ideas (e.g., importance sampling). Since then, faster computers and better random-number generators have made Monte Carlo a standard tool in science and engineering.
```

**NOTE:**
In the Group assignment 1.4, you already had a first look into simulations. In fact, you numerically computed the PDF and empirical CDF by drawing random samples from fitted distribution of $x_1$ and $x_2$, while assuming these two input variables to be independent. The workflow is rather simple, but you should always be careful on the assumptions made for the underlying joint distribution.   

---

## Simulating Mean and Variance of transformed variable
**Goal.** Given a model $X = q(Y)$ and an input univariate distribution $p_Y$, estimate mean and variance by random sampling.

From the general analytical expression provided for **Expectation law** and **Variance law**, we observe that we can replace the equalities by a numerical approximation such as

$$
E(X) = E( q(Y) ) \approx \frac{1}{N}\sum_{i=1}^{N} q(Y_i) = \hat{\mu}_X
$$

$$
D(X) = D( g(Y) ) \approx \frac{1}{N-1}\sum_{i=1}^{N} [ q(Y_i) - \hat{\mu}_X ] [ q(Y_i) - \hat{\mu}_X ]^T
$$

which refer to the sample mean and the sample variance, respectively. The standard error on the mean will decrease with $1/\sqrt{N}$, while observe that in the second expression we have $N-1$ at the denominator since we do not know the true mean $E( q(Y) )$ and therefore we first estimate it by the **sample mean** of the data $\{Y_1, ...Y_N\}$. This means that we use one degree of freedom and an unbiased estimator of the variance following by using $N-1$ instead of $N$.

**NOTE** The expression for multivariate functions and distributions follows trivially adopting the same definition in $\mathbb{R}^n$.

---

In Wednesday workshop you will get further experience on how to simulate via Monte Carlo, and you will be able to compare these results with the analytical ones.



% START-CREDIT
% source: uncertainty_propagation
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Lotfi Massarweh. {ref}`Find out more here <uncertainty_propagation_credit>`.
```
% END-CREDIT
