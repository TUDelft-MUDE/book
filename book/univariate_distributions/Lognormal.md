
# Lognormal distribution

The **lognormal distribution** is the continuous distribution of a random variable whose natural logarithm is normally distributed. This is, if the random variable $X \sim Lognormal$, then the random variable $Y=ln(X) \sim Normal$.

```{figure} https://files.mude.citg.tudelft.nl/Lognormal_Distribution.svg
Relationship between Lognormal and Normal distribution[^ref].
```

This distribution is widely used in engineering, since it models variables that can only take positive real values. The PDF of the Lognormal distribution is given by 

$$
f(x) = \cfrac{1}{x \sigma \sqrt{2 \pi}}e^{\left( \normalsize-\cfrac{(ln(x)-\mu)^2}{2\sigma^2}\right)}
$$

where $\mu$ and $\sigma$ are the mean and standard deviation of the variable's natural logarithm. Note that they are not the mean and standard deviation of the variable $X$ itself.

Integrating the PDF, the following expression of the CDF is derived

$$
F(x) = \Phi\left( \cfrac{ln(x)-\mu}{\sigma} \right) = \cfrac{1}{2}\left[ 1+erf\left( \cfrac{ln(x)-\mu}{\sigma \sqrt{2}}\right)\right]
$$

where $\Phi$ is the cumulative distribution function of of the standard Normal distribution function ($N(0,1)$). The CDF of the Lognormal distribution is displayed in the figure below.

## Interactive element

Let's see how these parameters influence the shape of the distribution. The lower the value of $\mu$, the more peaked  and the the PDF becomes and the mode of the distribution shifts towards 0. Note that the relationship between the mean and the peak of the distribution is nonlinear: the larger $\mu$, the further the peak shifts to the right for any given increment of $\mu$. The lower the mean $\mu$, the steeper the CDF becomes, reaching higher non-exceedance probabilities for increasing values of the random variable.

The effect of the standard deviation $\sigma$ may appear unintuitive at first. In most other distributions, as we increase $\sigma$, the peak value of the PDF decreases. However, when $\sigma$ grows ($\sigma>1$) in a lognormal PDF, the peak of the PDF moves towards 0 and increases in height. This is because the distibutions becomes flatter in log-space $y$, but the log-transformation concentrates the densities for $y < 1$ and stretches the densities for $y > 1$. The more probability mass is shifted into the region $y < 1$, the more the probability density concentrates in the region $0 < x < 1$. Similarly, when $\sigma$ is reduced below 1, the distribution becomes more peaked; however, it also moves towards positive values. Therefore, the influence of this parameter is different if $\sigma$ is above or below 1. Adjust the values in the interactive element below and observe this effect yourself.

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_lognormal_pdf.html
:name: lognormal_pdf
:aspectratio: 1.5 / 1

Interactively visualize the relationship between the PDF and the CDF of a lognormal distribution.
````

## Interesting properties

The mean of the Lognormal distribution can be computed as

$$
E[X]=e^{\normalsize \mu + \cfrac{\sigma^2}{2}}
$$

The variance is given by

$$
Var[X] = \left( e^{\normalsize\sigma^2}-1 \right)e^{\normalsize2\mu + \sigma^2}
$$

Finally, note that Lognormal distribution is not symmetric and presents positive skewness. This is, it presents a tail towards positive values.

Also, the **Lognormal distiribution is bounded in 0**. This is, the random variable modelled with the Lognormal distribution cannot take negative values or a value of zero.

# Let's practice

````{card} Exercises
During the design phase of a coastal structure, it is needed to assess if its height is enough to protect the sheltered area from overtopping events (sea water overpassing the structure and reaching the lee side). The distribution of overtopping volumes is known to follow a Lognormal distribution. The engineer has already calculated the parameters of the Lognormal distribution ($\mu$=5.5 and $\sigma$=1.15) and has plotted the CDF for you.

```{figure} https://files.mude.citg.tudelft.nl/logn_ex.png
PDF and CDF of Lognormal distribution to describe overtopping volumes $V (l/m)$.
```

<iframe src="https://tudelft.h5p.com/content/1292083830902957237/embed" aria-label="Lognormal" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>

```````

[^ref]: "Lognormal Distribution" by StijnDeVuyst is licensed under CC BY-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/?ref=openverse.

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre, Robert Lanzafame, and Maximilian Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT

