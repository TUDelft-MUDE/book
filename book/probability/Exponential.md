
# Exponential distribution

Another widely used distribution function is the Exponential distribution. For instance, it is applied to model the waiting time between succesive events of a Poisson process. The PDF of the Exponential distribution is given by

$$
f(x) = \lambda e^{-\lambda x} \hspace{1cm} for \ x \geq 0, \lambda>0
$$

$$
f(x) = 0 \hspace{1cm} otherwise
$$

where $\lambda$ is the parameter of the distribution, which is often called *rate*. In the right pannel of the figure below, an example of two Exponential distributions with $\lambda =1$ and $\lambda = 2$ is shown. As you can see, the maximum density in the PDF of en Exponential distribution is located at zero and it is followed by an Exponential decay. The higher the parameter $\lambda$, the higher the value of the density in $x=0$ and the faster the decay. In other words, the higher the parameter $\lambda$, the more concentrated the values of the random variable which are likely to occur and, thus, the lower the standard deviation. This can be seen on the left pannel of the figure, where random samples of the distribution are plotted. There you can see how higher values of the random variable $x$ appear when $\lambda = 1$, presenting then a higher dispersion.

```{figure} /probability/figures/exponential.png

---

---
Exponential distribution function: (left) random samples, and (right) PDF.
```



Integrating the PDF, the following expression of the CDF is obtained

$$
F(x) = 1 - e^{-\lambda x}
$$

which is visually represented in the figure below.

```{figure} /probability/figures/exponential_cdf.png

---

---
Exponential distribution function: CDF.
```

The influence of the parameter $\lambda$ can also be observed in the CDF. The higher the parameter $\lambda$, the faster the CDF reaches values of the non-exceedance probability close to 1. Thus, lower variability of the random variable is obtained.

## Some interesting properties

The mean of the exponential distribution can be obtained integrating by parts as

$$
E[X] = \int_o^{\infty}{x \lambda e^{-\lambda x}dx} = [-xe^{-\lambda x}]_0^{\infty} + \int_0^{\infty}{e^{-\lambda x}dx}= 1/ \lambda
$$

As previously mentioned, the Exponential distribution models the waiting time between events (e.g.: floods or earthquakes) of a Poisson process. For the Poisson process, $\lambda$ is the rate at which the events occur. Therefore, $1/\lambda$ is the average time between those events, since it is the expectation of the associated Exponential distribution. In reliability analysis, it can be called *mean life time* or *time to failure*.

The variance is given as

$$
Var[X] = E[X^2]-(E[X])^2 = 1/\lambda^2
$$

It should be noted that the coefficient of variation $CV = \sqrt{Var[X]}/E[X] = 1$.

If you remember the Poisson process is characterized by independent events. Thus, the time of the next occurrence modelled by the Exponential distribution is independent of the present and past occurrences. This is called the *memoryless property of the exponential distribution*. We can show it calculating the probability of the waiting time until the next ocurrence $X$ being higher than the sum of the two previous ones $X>x_1+x_2$, given that it is already bigger than one of them $X>x_1$ (conditional probability) as follows

$$
P[X>x_1+x_2|X>x_1]=\cfrac{P[X>x_1+x_2]}{P[X>x_1]}=\cfrac{e^{\normalsize{\lambda (x_1+x_2)}}}{e^{\normalsize{\lambda x_1}}}=e^{\normalsize{\lambda x_2}}=P[X>x_2]
$$

If the waiting time $X$ is exponential-distributed, you can see that the probability of the waiting time of one occurence ($x_2$) does not depend on the previous one ($x_1$).

Finally, note that this distribution is not bell-shaped and, thus, not symmetric. It presents a positive tail and its skewness is 2.

```{card} Exercises
An engineer is the manager of the construction of a bridge across a river and is concerned about large floods (floods with discharges higher than $50 m^3/s$) in the river, since they may damage the construction works. Higher floods than that occur in average every 10 years.

Assume that floods are independent and identically distributed. This means that they can be modelled using a Poisson process and, thus, the time between floods can be modelled using an Exponential distribution.

<iframe src="https://tudelft.h5p.com/content/1292083679343540347/embed" aria-label="Exponential" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>

```