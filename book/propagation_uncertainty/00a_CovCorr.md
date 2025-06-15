(correl)=
## Random vectors, covariance and correlation

When dealing with multiple [random variables](../fundamentals/prob-rv.md)we need to consider that these may not be independent. Instead of considering the individual random variables, we will then need to work with a random vector $X= [\begin{array}{llll} X_1 & X_2 & \ldots &X_m \end{array}]^T$, which has a *multivariate* (or: [joint](../fundamentals/joint_marginal_conditional.md)) distribution. We will first introduce the covariance and correlation coefficient of two random variables, and then introduce the multivariate normal distribution.

### Covariance and correlation

The covariance $Cov(X_1,X_2)$ is a measure of the joint variability of the two random variables $X_1$ and $X_2$. It gives us information about whether and how the two variables are correlated and it can be either positive or negative (hence, $Cov(X_1,X_2)	\lessgtr 0$). 

By definition 

$$ 
Cov(X_1,X_2)=\mathbb{E}([X_1-\mathbb{E}(X_1)][X_2-\mathop{{}\mathbb{E}}(X_2)]) 
$$ 

where $\mathop{{}\mathbb{E}}(X_1)$ is the expected value of the first random variable, for instance. 

Recall: the [expected value](meanvar) of a random variable $X$ is 

$$ 
\mathbb{E}(X)=\mu_X = \int_{-\infty}^{\infty} x f_X (x)dx
$$ 

where $f_X(x)$ is the probability density function of $X$.

If $Cov(X_1,X_2)>0$ it means that high (low) values of $X_1$ occur together with high (low) values of $X_2$, therefore the covariance is defined as *POSITIVE*.

On the other hand, if $Cov(X_1,X_2)<0$ it means that high (low) values of $X_1$ occur together with low (high) values of $X_2$. In this case the covariance is defined as *NEGATIVE*.

Note that:

$$
Cov(X_i,X_i)=\mathbb{E}([X_i-\mathbb{E}(X_i)]^2) =\sigma^2_i
$$


In order to better understand the relation between the two random variables we can also compute the Pearson correlation coefficient

$$ 
\rho(X_1,X_2)=\frac{Cov(X_1,X_2)}{\sigma_{X_1} \sigma_{X_2}} 
$$ 

which in fact is a measure of the strength of the *linear relationship* among the variables.

The correlation coefficient by definition takes a value between -1 and 1. If $\rho_{ij} =0$ the random variable are uncorrelated, this is the case if the random variables are *independent*. If $\rho_{ij}= \pm 1$ the variables are fully correlated: knowing the value of one variable, means that the value of the other variable is also known, and the two variables have a linear relation. A positive correlation coefficient means that if one variable increases, the other one tends to increase as well; conversely a negative correlation means that an increase of one variable is accompanied by a tendency of the other variable to decrease.

Examples are shown in {numref}`correlation`, for an example with a large number of repeated measurements; for this example $ \sigma_{X_1}=1$ and $\sigma_{X_2}=2$ (the mean values are indicated as $\mu_1$ and $\mu_2$). The larger standard deviation of the second measurement results in a larger spread in the vertical direction. Obviously, the measurements fluctuate around the means.

Generally it is quite difficult to find cases in which $\rho=\pm 1$ or even $\rho=0$. In fact it is more likely to have values of $\rho$ that range between $-1$ and $1$ and, based on this value, we can determine the strength of the linear dependence.

```{figure} https://files.mude.citg.tudelft.nl/01_correlation.png
---
height: 350px
name: correlation
---
Scatterplots of outcomes of ($X_1,X_2$) with different correlation coefficients.
```

The interactive element below allows you to play around with the correlation value yourself. Observe how the distribution's density contours, or the scattered data, changes when you adapt the correlation value.

<iframe src="../_static/elements/element_correlation.html" width="600" height="400" frameborder="0"></iframe>

### Covariance matrix

When considering a random vector $X= [\begin{array}{llll} X_1 & X_2 & \ldots &X_m \end{array}]^T$, we can 'collect' all covariances in the so-called *covariance matrix*:

$$
\Sigma_X=  \left[\begin{array}{cccc} \sigma^2_1 & Cov(X_1,X_2) & \ldots & Cov(X_1,X_m) \\ Cov(X_1,X_2)& \sigma_{2}^2 & \ldots & Cov(X_2,X_m) \\\vdots & \vdots & \ddots & \vdots \\ Cov(X_1,X_m) & Cov(X_2,X_m) & \ldots & \sigma_{m}^2 \end{array}\right]
$$

Note that the covariance matrix is symmetric, since $Cov(X_i,X_j)= Cov(X_j,X_i)$. 

If all measurements are independent, all covariances will be equal to zero, and the covariance matrix becomes a diagonal matrix with the variances on the diagonal. 
