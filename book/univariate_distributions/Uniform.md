
# Uniform distribution

The uniform distribution is the simplest type of continuous parametric distribution and, as it is implied in its name, the PDF has a constant value along a given interval $[a,b]$, where $a < b$. The PDF of the uniform is given by

$$
f(x) = \frac{1}{b-a}   \hspace{1cm}   \text{for} \ a\leq x \leq b
$$

$$
f(x) = 0  \hspace{1cm} \text{otherwise}
$$

Note that all values in the distribution are between the lower limit $a$ and the higher limit $b$ and are equally likely to occur. The CDF of a uniform distribution is similarly simple: a piece-wise linear function between $a$ and $b$:

$$
F(x) = 0   \hspace{1cm}   \text{for} \ x<a
$$

$$
F(x) = \frac{x-a}{b-a}   \hspace{1cm}   \text{for} \ a\leq x \leq b
$$

$$
F(x) = 1  \hspace{1cm} \text{for} \ x>b
$$

If we make $a=0$ and $b=1$, we obtain the standard or unity uniform distribution, which is used to generate random values from other distribution functions for simulation purposes.

## Interactive element

Below, you can see the PDF and CDF of a uniform distribution. Adjust the parameters and observe how the PDF's and CDF's shapes change in response.

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_uniform_pdf.html
:name: Gaussian_pdf
:aspectratio: 1.5 / 1

Interactively visualize the relationship between the PDF and the CDF of a uniform distribution.
````

## Interesting properties

The mean of the uniform distribution can be computed based on its simple geometry as

$$
E[X]=\frac{1}{2}(a+b)
$$

The variance is given by

$$
Var[X] = \frac{1}{12}(b-a)^2
$$

Finally, note that uniform distribution is symmetric and presents 0 skewness. Thus, the median and the mean are identical. This is, it does not present any tail.

Uniform distributions are useful choices for variables with natural lower and upper limits, as the distributions *support* (the range of $x$ values for which the PDF returns non-zero densities) is restricted between $[a,b]$. Also, recall from the previous sections that the standard uniform PDF (that is to say $a=0$ and $b=1$) is often used by computers to sample any univariate distribution through their inverse CDF $F^{-1}$.

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre, Robert Lanzafame, and Maximilian Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT