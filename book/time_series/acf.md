(ACF)=
# Autocovariance function

Before we can look into the modelling of a stochastic process for instance using an Autoregressive (AR) model, we first need to introduce the autocovariance function (ACF) for a stationary time series, and describe the relationship between the ACF and the power spectral density (PSD).

As in [Observation theory](../observation_theory/01_Introduction.md), the variance component is often determined based on the precision of an observable (at a given epoch), and the covariance components quantitatively indicate the statistical dependence between observables. In this case, dependence is inherently introduced by the physical process that produces the time series, and in fact our time series methods seek to (mathematically) account for this.

## Autocovariance and autocorrelation

Let us assume an arbitrary stationary (discrete) time series, $S=[S_1,S_2,...,S_m]^T$, with mean $\mathbb{E}(S_{i})=\mu$ and variance $Var(S_{i})=\sigma^2$ for $i=1,\ldots,m$. Remember that stationarity implies that the statistical properties of the time series do not depend on the time at which it is observed, i.e. expectation and variance are constant over time.

The *formal* (or: theoretical) autocovariance is defined as

$$
Cov(S_{t+\tau}, S_t) =\mathbb{E}(S_{t+\tau}S_t)-\mu^2
=c_{\tau}
$$

We have that $Cov(S_{t+\tau}, S_t) =Cov(S_t, S_{t-\tau})$.

The autocovariance depends on $\tau$, which is referred to as lag; it is the difference in time between $t+\tau$ and $t$, and equally the difference between $t$ and $t-\tau$. In the sequel we use $\tau$ both to indicate the time shift in unit of time (e.g. seconds) and the corresponding discrete time index, as at the start of this chapter it was for convenience assumed that $\Delta t = 1$, and hence $t_i = i$.

:::{card} Exercise covariance

Show that the covariance can be written as: 

$$Cov(S_{t+\tau}, S_t) = \mathbb{E}(S_{t+\tau}S_t)-\mu^2
=c_{\tau}$$ 


````{admonition} Solution
:class: tip, dropdown

$$
 Cov(S_{t+\tau}, S_t)= \mathbb{E}[(S_{t+\tau} - \mathbb{E}(S_{t+\tau}))(S_t - \mathbb{E}(S_t))]\\
 = \mathbb{E}((S_{t+\tau}-\mu)(S_t-\mu))\\
 = \mathbb{E}(S_{t+\tau}S_t - \mu S_t - \mu S_{t+\tau} + \mu^2)\\
 = \mathbb{E}(S_{t+\tau}S_t) - \mu \mathbb{E}(S_t) - \mu \mathbb{E}(S_{t+\tau}) + \mu^2\\
= \mathbb{E}(S_{t+\tau}S_t) - 2\mu^2 + \mu^2\\
= \mathbb{E}(S_{t+\tau}S_t) - \mu^2\\
$$
````
:::

:::{card} Exercise covariance

Prove that $Cov(S_t, S_{t-\tau}) =Cov(S_{t+\tau}, S_t)$: 


````{admonition} Solution
:class: tip, dropdown

From the definition of covariance, we know that

$$
Cov(a,b) = Cov(b,a)
$$

Hence, we have that

$$ Cov(S_t, S_{t-\tau}) = Cov(S_{t-\tau}, S_t)$$

Due to the stationarity of the time series (invariant against time shift), we have that

$$ Cov(S_t, S_{t-\tau}) = Cov(S_{t+\tau}, S_t)$$

Therefore, we have that

$$ Cov(S_t, S_{t-\tau}) = Cov(S_{t+\tau}, S_t)$$

and $c_{\tau} = c_{-\tau}$.

````
:::



The *formal* autocorrelation is defined as

$$
r_{\tau} = \mathbb{E}(S_{t+\tau}S_t)
$$

and $r_{\tau} = r_{-\tau}$.

```{note}
When we have a zero-mean time series, $\mu=0$, it follows that $c_{\tau}=r_{\tau}$
```

### Empirical autocovariance

The autocovariance function of a time series is not known beforehand, and hence needs to be estimated based on the actual observed values. The least-squares method or maximum likelihood method can be used to estimate this *empirical* (or sample) autocovariance function of a time series. Let us see how!

**Least-squares estimation**

For a given stationary time series $S = [S_1,S_2,...,S_m]^T$, the least-squares estimator of the **autocovariance function** is given by

$$\
\hat{C}_{\tau} = \frac{1}{m-\tau}\sum_{i=1}^{m-\tau}(S_{i+\tau}-\mu)(S_{i}-\mu), \hspace{25px} \tau=0,1,...,m-1$$

and is an unbiased estimator $E(\hat{C}_{\tau}) = c_\tau$.

The least-squares estimator of **autocorrelation** (also called empirical autocorrelation function) is then

$$
\hat{R}_{\tau}=\frac{1}{m-\tau}\sum_{i=1}^{m-\tau}S_{i+\tau} S_{i}, \hspace{25px} \tau=0,1,...,m-1
$$

**Maximum likelihood estimation**

The maximum likelihood estimator of **autocovariance** is given by

$$
\hat{C}_{\tau} = \frac{1}{m}\sum_{i=1}^{m-\tau}(S_{i+\tau}-\mu)(S_i-\mu), \hspace{25px} \tau=0,1,...,m-1
$$

Note that this is a biased estimator, $\mathbb{E}(\hat{C}_{\tau})\neq c_{\tau}$.

Similarly, the maximum likelihood estimate of the autocorrelation follows as:

$$
\hat{R}_{\tau}=\frac{1}{m}\sum_{i=1}^{m-\tau}S_{i+\tau} S_{i}, \hspace{25px} \tau=0,1,...,m-1
$$

Note practically, for large $m$, and not too large $\tau$, there is little difference in using $\frac{1}{m-\tau}$ and $\frac{1}{m}$.

```{note}
Here we use capitals for $\hat{C}_{\tau}$ and $\hat{R}_{\tau}$ since **estimators** are always a function of the random observables $S_t$.
```

```{note}
If mean $\mu$ is not known, it can be replaced in practice by the empirical mean in the above expressions for the empirical autocovariance function.
```

### Covariance matrix based on autocovariance

The structure of a covariance matrix for a stationary time series is purely symmetric (mirrored in the diagonal) and it looks like

$$
\Sigma_{S} = \begin{bmatrix} 
\sigma^2 & c_1 & c_2 & \dots & c_{m-1}\\ 
c_1 & \sigma^2 & c_1 & \ddots  & \vdots \\ 
c_2 & c_1 & \sigma^2 &  \ddots & c_2  \\ 
\vdots & \ddots & \ddots & \ddots & c_1\\ c_{m-1} &  & c_2 & c_1 & \sigma^2\end{bmatrix}$$

There are $m$ (co)variance components - **one** variance component, $\sigma^2 = c_0$, and $m-1$ covariance components, $c_i$ for $i=1,\ldots,m-1$.


(NACF)=
## Normalized ACF

The *normalized* autocovariance estimator can directly be obtained from the autocovariance estimator as

$$
\hat{\rho}_{\tau} = \frac{\hat{C}_{\tau}}{\hat{C_0}}, \hspace{20px}\tau = 0,...,m-1 \implies \hat{\rho}_0 = 1
$$

and $|\hat{\rho}_{\tau}| \leq 1$ for all $\tau$ (using the biased ACF $\hat{C}_{\tau}$, which is the default implemented in Python)

```{note}
The estimated normalized autocovariance is the same as  the time dependent Pearson correlation coefficient.

In literature $\hat{\rho}_{\tau}$ is sometimes referred to as the *autocorrelation (coefficient) function*.
```

The variance of the normalized ACF can, for large $m$, be approximated as

$$
\sigma_{\hat{\rho}_{\tau}}^2 = \frac{1}{m} (1 + 2 \sum_{i=1}^{\infty} \rho^2_{i})
$$

for processes with decaying autocorrelation function {cite:p}`box2016` (Eq. (2.1.15)).
The variance can be used, only for larger values of $\tau$, as a check whether $\rho_{\tau}$ is effectively zero beyond a certain lag. In practice one can substitute $\hat{\rho}$ for $\rho$.

If $m$ is sufficiently large, $\hat{\rho}_{\tau}$ is approximately normally distributed:

$$
\hat{\rho}_{\tau} \sim N(\rho_{\tau},\sigma^2_{\hat{\rho}_{\tau}})
$$

Though it is possible to compute $\hat{\rho}_{\tau}$ for up to $\tau=m-1$, it is recommended in practice to limit $\tau$ for instance to at most 10 percent of $m$.

### Worked example

Let us consider a time series of $m=100$ observations, such that

$$
\hat{\rho}_1 = 0.4
$$

and $\hat{\rho}_i \approx 0$ for $i>1$.

We know that 

$$
\hat{\rho}_1 \sim N(\rho_1,\sigma^2_{\hat{\rho}_1})
$$

with $\rho_1$ unknown and

$$
\sigma^2_{\hat{\rho}_1}=\frac{1}{m}+\frac{2\hat{\rho}^2_1}{m}=0.0132\implies\sigma_{\hat{\rho}_1}=0.1149
$$

We will now apply a test whether the estimated autocorrelation is significant. The null hypothesis assumes there is **no** correlation:

* $\mathcal{H}_0$: $\rho_1=0$
* $\mathcal{H}_a$: $\rho_1 \neq 0$

Since we know the distribution of $\hat{\rho}_1$, a suitable test statistic would be:

$$
T = \frac{\hat{\rho}_1}{\sigma_{\hat{\rho}_1}} \sim N(0,1)
$$

where we would reject $\mathcal{H}_0$ if $|T|>k_{\alpha}$. With a false alarm rate of $\alpha = 0.01$, we find that the critical value can be obtained from the {ref}`table of the standard normal distribution <table_standardnormal>`. Note that we have a 2-sided critical region, hence we need to look up the value for $0.5\alpha$.

In this example, we obtain:

$$
(T = 3.48 ) > (k_{\alpha}=2.58)
$$

and hence the null hypothesis is rejected, implying that the autocorrelation at lag $\tau = 1$ is significant.

:::{card} Exercise

A zero-mean stationary noise process consists of $m=5$ observations:

$$
s = \begin{bmatrix} 2 & 1 & 0 & -1 & -2 \end{bmatrix}^T
$$

What is the _least-squares estimate_ of the normalized ACF at $\tau=1$; so compute $\hat{\rho}_{1}$?

```{admonition} Solution
:class: tip, dropdown

The normalized autocovariance function (ACF) can be estimated from the auto-covariance function as:

$$
\hat{\rho}_\tau=\frac{\hat{C}_\tau}{\hat{C}_0}, \qquad \tau=0, \dots , m-1
$$

where the least-squares estimate of auto-covariance function is:

$$
\hat{C}_\tau
= \frac{\sum_{i=1}^{m-\tau}(S_i - \mu)(S_{i+\tau} - \mu)}{m-\tau},
\qquad \tau=0, \dots , m-1
$$

For our application we have $\mu_y=0$, as we deal with a zero-mean process. We have to compute $\hat{\sigma}(0)$ and $\hat{\sigma}(1)$ given as:

$$
\hat{C}_0
= \frac{\sum_{i=1}^{m} S_i^2}{m-0}
= \frac{10}{5} = 2
$$

And 

$$
\hat{C}_1
= \frac{\sum_{i=1}^{m-1} S_i S_{i+1}}{m-1}
= \frac{2(1) + 1(0) + 0(-1) + (-1)(-2)}{5 - 1}
= \frac{2 + 0 + 0 + 2}{4}
= 1
$$

Giving

$$
\hat{\rho}_1
= \frac{1}{2}
$$

Keep in mind that Python by default uses the maximum likelihood estimator for $\hat{C}_{\tau}$, i.e. with $\frac{1}{m}$ instead of $\frac{1}{m-\tau}$.

```
:::

% START-CREDIT
% source: time_series_analysis
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Alireza Amiri-Simkooei, Christiaan Tiberius and Sandra Verhagen. {ref}`Find out more here <time_series_analysis_credit>`.
```
% END-CREDIT
