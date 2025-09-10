# Gaussian distribution

Most of you should have already encountered the **Gaussian distribution** (also sometimes known as the **Normal distribution**) during your studies. This distribution is one of the most widely-used PDFs since it occurs commonly in nature and engineering and has many elegant mathematical properties. The PDF of the Normal distribution is given by

$$
f(x) = \cfrac{1}{\sigma \sqrt{2 \pi}} e^{\normalsize{-}\cfrac{1}{2}\left(\cfrac{x-\mu}{\sigma}\right)^2}
$$

where $x$ is the value of the random variable and $\mu \in \mathbb{R}$ and $\sigma \in \mathbb{R}^{+}$ are the two parameters of the distribution, the mean and standard deviation. If we integrate the PDF, we obtain the CDF. In the case of the Normal distribution, there is no closed form of the CDF, but it can be expressed as

$$
F(x) = \cfrac{1}{2}\left(1+\text{erf}\left(\cfrac{x-\mu}{\sigma\sqrt{2}}\right)\right)
$$

where $\text{erf}$ denotes the **error function** given by

$$
\text{erf}(x) = \cfrac{2}{\sqrt{\pi}}\int_0^x{e^{\normalsize-t^2}dt}
$$

## Interactive element

Observe the influence of the parameters on the function value: within the exponent, the numerator computes the $L^1$-distance between the argument $x$ and the mean $\mu$, then scales by the standard deviation $\sigma$. This distance is then squared, rendering its sign positive, and multiplied by $-1/2$, which makes it zero (for $x = \mu$) or negative (for $x \neq \mu$). Taking the exponent of this number yields a function which is largest around the mean, then decays to zero the farther $x$ and $\mu$ deviate, scaled by $\sigma$. The factor before the exponent is a constant that depends only on $\sigma$ and ensures that the resulting function integrates to one. 

Let's see how the resulting distribution looks. The element below shows a univariate Gaussian PDF and CDF for adjustable $\mu$ and $\sigma$.

````{iframe-figure} ../_static/elements/element_Gaussian_pdf.html
:name: Gaussian_pdf
:aspectratio: 1.5 / 1

Interactively visualize the relationship between the PDF and the CDF of a Gaussian distribution.
````

Observe that as we increase or decrease the mean $\mu$, the function moves to the right or left, respectively, since the reference point for the distance calculation shifts. Likewise, increasing the standard deviation $\sigma$ flattens the distribution, since a larger denominator within the exponent reduces the magnitude of the fraction within the exponent.

## Interesting Properties

The mean, median and mode of the Normal distribution are each equal to $\mu$. The variance is $\sigma^2$. Note that Normal distribution is a symmetric distribution and presents 0 skewness. It is also sometimes known as the *maximum entropy* distribution, that is to say, the distribution which imposes the least structure on the pdf for a given finite standard deviation $\sigma$. Gaussian distributions have a number of highly attractive properties in higher dimensions that will play a significant role in the week on **multivariate probability distributions**.

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre, Robert Lanzafame, and Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT