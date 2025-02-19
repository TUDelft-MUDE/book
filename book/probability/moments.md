(prob_moments)=

# Method of moments

The method of moments consists of equating the moments[^moment] in the observations to those of the distribution we want to fit. This is, there is a relationship between the moments and the parameters of the distribution. Then, if we equate the moments of the distribution to the moments of the observations, we can obtain the values of the parameters of the distribution. Actually, you have already done it in the exercises of the Exponential distribution! 

## Let's see it with an example

An engineer is studying the intensity of earthquakes in Rome (Italy). To this end, the engineer is using *Catalogo dei terremoti italiani dall'anno 1000 al 1980* (the Catalog of Italian earthquakes from year 1000 to 1980) edited by D. Postpischl in 1985. This catalog reports the intensity of earthquakes in terms of the Mercalli-Canconi-Sieber (MCS) index. Due to the uncertainties associated to this natural phenomenom, the engineer considers them as a random one and wants to fit a Gumbel distribution to the observations found in the catalog using the method of moments. The data found in the catalog is shown in the table below [^ref].


```{list-table} MSC intensity of the recorded earthquakes in the city of Rome.
:header-rows: 1
:name: earthquakes

* - MSC intensity
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
* - Number
  - 113
  - 132
  - 56
  - 22
  - 4
  - 2
```

Remember that the CDF of the Gumbel distribution is given by 

$$
F(x) = e^{\normalsize-e^{\normalsize-\cfrac{x-\mu}{\beta}}}
$$

Therefore, the value of $\mu$ and $\beta$ needs to be determined based on the observations to fit the distribution.

The first thing the engineer needs to do is to calculate the moments of the observations in the Table. The empirical mean ($\overline{X}$) and empirical variance ($\sigma^2$) are calculated as:

$$
\overline{X} = \cfrac{2 \cdot 113 + 3 \cdot 132 + 4 \cdot 56 + 5 \cdot 22 + 6 \cdot 4 + 7 \cdot 2}{113+132+56+22+4+2} \approx 3.02
$$

$$
\sigma^2 = \cfrac{\sum{fx^2}}{\sum{f}}-\left( \cfrac{\sum{fx}}{\sum{f}}\right)^2 \approx 0.99
$$

where $x$ is the value of the intensity and $f$ is the frequency of the value $x$.

Based on the properties of the Gumbel distribution, we know 

$$
E[X]=\mu + \gamma \beta
$$

$$
Var[X] = \cfrac{\pi^2}{6}\beta^2
$$

where $\gamma \approx 0.577$ is the Euler-Mascheroni constant.

Therefore, we can equate the expectation and variance of the distribution ($E[X]$ and $Var[X]$) to the calculated moments and obtain the value of the parameters as

$$
3.02 = \mu + 0.577 \beta 
$$

$$
0.99 = \cfrac{\pi^2}{6}\beta^2
$$

Thus, $\mu \approx 2.57$ and $\beta \approx 0.77$. 

```{card} Exercises

As part of the quality control of the construction of a building, lab tests are performed to determine the compressive strengths of concrete. The following values in $N/mm^2$ are obtained: 60.5, 59.8, 53.4, 56.9 and 61.9. 

The engineer responsible for quality assumes that the compressive strength follows a uniform distribution, whose CDF is given by 

$$
F(x) = 0   \hspace{1cm}   for \ x<a
$$

$$
F(x) = \cfrac{x-a}{b-a}   \hspace{1cm}   for \ a\leq x \leq b
$$

$$
F(x) = 1  \hspace{1cm} for \ x>b
$$

<iframe src="https://tudelft.h5p.com/content/1292083850830375117/embed" aria-label="Method moments" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>

```

[^moment]: We denote as moments in statistics to the quantitative properties to characterize a distribution. The four commonly used moments are the mean, the variance, the skewness and the kurtosis.
[^ref]: Data extracted from Kottegoda and Rosso (2008).