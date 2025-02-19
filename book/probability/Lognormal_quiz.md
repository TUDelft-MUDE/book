
# Lognormal distribution: let's practice

During the design phase of a coastal structure, it is needed to assess if its height is enough to protect the sheltered area from overtopping events (sea water overpassing the structure and reaching the lee side). The distribution of overtopping volumes is known to follow a Lognormal distribution. The engineer has already calculated the parameters of the Lognormal distribution ($\mu$=5.5 and $\sigma$=1.15) and has plotted the CDF for you.

```{figure} /probability/figures/logn_ex.png

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

```{figure} /probability/figures/logn_ex_c1.png

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

```{figure} /probability/figures/logn_ex_c3.png

---

```