
# Lognormal distribution

Lognormal distribution is the continuous distribution of a random variable whose natural logarithm is normally distributed. This is, if the random variable $X \sim Lognormal$, then the random variable $Y=ln(X) \sim Normal$.

```{figure} /sandbox/continuous/figures/Lognormal_Distribution.svg

---

---
Relationship between Lognormal and Normal distribution[^ref].
```

 It is widely used in engineering, since it models variables which only take positive real values.  The PDF of the Lognormal distribution is given by 

$
f(x) = \frac{1}{x \sigma \sqrt{2 \pi}}e^{\left( -\frac{(ln(x)-\mu)^2}{2\sigma^2}\right)}
$

where $\mu$ and $\sigma$ are the mean and standard deviation of the variable's natural logarithm. Note that they are not the mean and standard deviation of the variable $X$ itself.

Let's see how these parameters influence the shape of the distribution. In the figure below, two sets of three PDFs are displayed. In the left pannel, the displayed distributions present the same $\sigma$ and different values of $\mu=$0.5, 1 and 2. The lower the value of $\mu$, the more peaked is the distribution and the mode of the distribution moves towards 0. In the right pannel, all the distributions present the same value of $\mu$ and different values of $\sigma=$0.5, 1 and 2. When $\sigma$ grows towards values $\sigma>0$, the distribution moves towards 0 and becomes much more peakes. Similarly, when $\sigma$ reduces with values below 1, the distribution becomes more peaked. However, it moves towards positive values. Therefore, the influence of this parameter is different if $\sigma$ is above or below 1. 

```{figure} /sandbox/continuous/figures/logn_density.png

---

---
PDF of Lognormal distribution: (left) influence of parameter $\mu$, and (right) influence of parameter $\sigma$.
```

Integrating the PDF, the following expression of the CDF is derived

$
F(x) = \Phi\left( \frac{ln(x)-\mu}{\sigma} \right) = \frac{1}{2}\left[ 1+erf\left( \frac{ln(x)-\mu}{\sigma \sqrt{2}}\right)\right]
$

where $\Phi$ is the cumulative distribution function of of the standard Normal distribution function ($N(0,1)$). The CDF of the Lognormal distribution is displayed in the figure below.

```{figure} /sandbox/continuous/figures/logn_cdf.png

---

CDF of Lognormal distribution: (left) influence of parameter $\mu$, and (right) influence of parameter $\sigma$.
```

In the left pannel, the influence of the parameter $\mu$ is shown. The lower the $\mu$, the steeper becomes the CDF, reaching higher non-exceedance probabilities for increasing values of the random variable. In the right pannel, the influence of the parameter $\sigma$ is presented. Again, it can be seen that the influence of $\sigma$ depends whether it is above or below 1.

## Some properties

The mean of the Lognormal distribution can be computed as

$
E[X]=e^{\mu + \frac{\sigma^2}{2}}
$

The variance is given by

$
Var[X] = \left( e^{\sigma^2}-1 \right)e^{2\mu + \sigma^2}
$

Finally, note that Lognormal distribution is not symmetric and presents positive skewness. This is, it presents a tail towards positive values.

# Let's practice

During the design phase of a coastal structure, it is needed to assess if its height is enough to protect the sheltered area from overtopping events (sea water overpassing the structure and reaching the lee side). The distribution of overtopping volumes is known to follow a Lognormal distribution. The engineer has already calculated the parameters of the Lognormal distribution ($\mu$=5.5 and $\sigma$=1.15) and has plotted the CDF for you.

```{figure} /sandbox/continuous/figures/logn_ex.png

---

---
PDF and CDF of Lognormal distribution to describe overtopping volumes $V (l/m)$.
```

The maximum allowed overtopping volume is 500 l/m. What is the probability of exceeding that value?

```{admonition} Answer
:class: tip, dropdown

The probability of being above 500l/m can be directly derived from the CDF in the previous figure:

$$
   P[X > 500] = 1 - F(500) = 1 - 0.73 = 0.27
$$

The figure below illustrates the previous computation.

```{figure} /sandbox/continuous/figures/logn_ex_c1.png

---

```
This probability is a bit too high! 

And what is the mean expected value of the volumes?

```{admonition} Answer
:class: tip, dropdown

Making use of the definition of expectation of the Lognormal distribution:

$$
E[V]=e^{\mu + \frac{\sigma^2}{2}}=e^{5.5 + \frac{1.15^2}{2}} \approx 474 l/m
$$

```


Note that the mean value is not the same as the median value. How much would be the median $V$ from the mean $V$. Compute it.

```{admonition} Answer
:class: tip, dropdown

The median of the distribution is the observation whose non-exceedance probability is 0.5. Therefore, it can be directly computed from the inverse of the CDF. 

$$
P[X > x] = F^{-1}(x)=0.5 \rightarrow x =  250 l/m
$$

You can see that the mean = 474l/m >> median = 250l/m, indicating that the distribution is not symmetric and presents a positive tail. The process is illustrated in the following figure.

```{figure} /sandbox/continuous/figures/logn_ex_c3.png

---

```

[^ref]: "Lognormal Distribution" by StijnDeVuyst is licensed under CC BY-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/?ref=openverse.