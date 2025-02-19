
# Revisiting Gaussian distribution

You have already used Gaussian or Normal distribution during your BSc and this course since it is widely used in Observation Theory or to model errors in measurements. The PDF of the Normal distribution is given by

$$
f(x) = \cfrac{1}{\sigma \sqrt{2 \pi}} \ e^{\normalsize{-}\cfrac{1}{2}\left(\cfrac{x-\mu}{\sigma}\right)^2}
$$

where $x$ is the value of the random variable and $\mu$ and $\sigma$ are the two parameters of the distribution. These parameters, $\mu$ and $\sigma$, correspond to the mean and standard deviation of the random variable.

If we integrate it, we obtain the CDF (non-exceedance probabilities). In the case of the Normal distribution, there is no closed form of the CDF (the integral), but it can be expressed as

$$
F(x) = \cfrac{1}{2}\left(1+\text{erf}\left(\cfrac{x-\mu}{\sigma\sqrt{2}}\right)\right)
$$

where $\text{erf}$ denotes the error function given by

$$
\text{erf}(x) = \cfrac{2}{\sqrt{\pi}}\int_0^x{e^{\normalsize-t^2}dt}
$$

Let's see how the distribution looks.

 In the figure below, the PDF and CDF of the Gaussian distribution are shown for different values of its parameters. In the left pannel, the PDF of three Gaussian distributions is shown. The black and blue distributions present the same value of the standard deviation ($\sigma$=1), so in the PDF plot the width of the bell is the same. However, they have different values of the mean ($\mu$), which acts like a location parameter. Thus, increasing the mean moves the distribution towards the right, making more likely higher values of the random variable. You can also see that in the CDF plot. The distribution moves towards the right so for a given value, $x = 2$, $F(x\leq2) \approx 0.98$ for the black line and $F(x\leq2) \approx 0.84$ for the blue line. 

 Regarding the standard deviation ($\sigma$), it can be interpreted as the dispersion around the mean ($\mu$). Thus, you can see in the PDF plot the the red distribution is wider that the black or blue ones, since the standard deviation is the double of the other two. You can also see the effect in the CDF plot, where the slope of the red distribution is more gentle than those of the black and blue distributions.


```{figure} /probability/figures/gaussian.png
---
scale: 75%
name: gaussian distr

---
Gaussian distribution function: PDF and CDF.
```



## Some properties

The mean, median and mode of the Normal distribution is equal to $\mu$. The variance is $\sigma^2$. Note that Normal distribution is symmetric and presents 0 skewness. 