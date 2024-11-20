(ACF)=
# Autocovariance function (ACF)

Before we can look into the modelling of a stochastic process using an Autoregressive (AR) model, we first need to introduce the autocovariance function (ACF) for a stationary time series, and describe the relationship between ACF and a power spectral density (PSD).

As in the Chapter on #TODO (add reference to obs theory), the variance component is often determined based on the precision of an observation (at a given epoch), and the covariance components quantitatively indicate the statistical dependence (or independence) between observations. In this case, dependence is inherently introduced by the physical processes that produce the signal (of which our time series is a sample), and in fact our time series methods seek to (mathematically) account for this.

## Autocovariance and autocorrelation

Let us assume an arbitrary (discrete) stationary time series, $S=[S_1,S_2,...,S_m]^T$, with mean $\mathbb{E}(S)=\mu$ and variance $Var(S_{i})=\sigma^2$. Remember that stationarity implies that the statistical properties of the time series do not depend on the time at which it is observed, i.e. expectation and variance are constant over time.

The *formal* (or: theoretical) autocovariance is defined as

$$
Cov(S_t, S_{t-\tau}) =\mathbb{E}(S_tS_{t-\tau})-\mu^2
=c_{\tau}
$$

We have that $Cov(S_t, S_{t-\tau}) =Cov(S_t, S_{t+\tau})$.


:::{card} Exercise covariance

Show that the covariance can be written as: 

$$Cov(S_t, S_{t-\tau}) = \mathbb{E}(S_tS_{t-\tau})-\mu^2
=c_{\tau}$$ 


````{admonition} Solution
:class: tip, dropdown

$$
 Cov(S_t, S_{t-\tau})= \mathbb{E}[(S_t - \mathbb{E}(S_t))(S_{t-\tau} - \mathbb{E}(S_{t-\tau}))]\\
 = \mathbb{E}((S_t-\mu)(S_{t-\tau}-\mu))\\
 = \mathbb{E}(S_tS_{t-\tau} - \mu S_{t-\tau} - \mu S_t + \mu^2)\\
 = \mathbb{E}(S_tS_{t-\tau}) - \mu \mathbb{E}(S_{t-\tau}) - \mu \mathbb{E}(S_t) + \mu^2\\
= \mathbb{E}(S_tS_{t-\tau}) - 2\mu^2 + \mu^2\\
= \mathbb{E}(S_tS_{t-\tau}) - \mu^2\\
$$
````
:::

:::{card} Exercise covariance

Prove that $Cov(S_t, S_{t-\tau}) =Cov(S_t, S_{t+\tau})$: 



````{admonition} Solution
:class: tip, dropdown

From the definition of covariance, we know that
$$ Cov(a,b) = Cov(b,a)$$

Hence, we have that

$$ Cov(S_t, S_{t-\tau}) = Cov(S_{t-\tau}, S_t)$$

Due to the stationarity of the time series, we have that

$$ Cov(S_{t-\tau}, S_t) = Cov(S_t, S_{t+\tau})$$

Therefore, we have that

$$ Cov(S_t, S_{t-\tau}) = Cov(S_t, S_{t+\tau})$$


````
:::



The *formal* autocorrelation is defined as

$$
r_{\tau} = \mathbb{E}(S_tS_{t-\tau})
$$

```{note}
When we have a zero-mean time series, $\mu=0$, it follows that $c_{\tau}=r_{\tau}$
```

### Empirical autocovariance

The autocovariance function of a time series is not known beforehand, and hence needs to be estimated based on the actual observed values. The least-squares method or maximum likelihood method can be used to estimate this *empirical* autocovariance function of a time series. Let us see how!

**Least-squares estimation**

For a given stationary time series $S = [S_1,S_2,...,S_m]^T$, the least-squares estimator of the **autocovariance function** is given by

$$\
\hat{C}_{\tau} = \frac{1}{m-\tau}\sum_{i=1}^{m-\tau}(S_i-\mu)(S_{i+\tau}-\mu), \hspace{25px} \tau=0,1,...,m-1$$

The least-squares estimator of **autocorrelation** (also called empirical autocorrelation function) is then

$$
\hat{R}_{\tau}=\frac{1}{m-\tau}\sum_{i=1}^{m-\tau}S_i S_{i+\tau}, \hspace{25px} \tau=0,1,...,m-1
$$

**Maximum likelihood estimations**

The maximum likelihood estimator of **autocovariance** is given by

$$
\hat{C}_{\tau} = \frac{1}{m}\sum_{i=1}^{m-\tau}(S_i-\mu)(S_{i+\tau}-\mu), \hspace{25px} \tau=0,1,...,m-1
$$

Note that this is a biased estimator, $\mathbb{E}(\hat{C}_{\tau})\neq c_{\tau}$.

Similarly, the maximum likelihood estimate of the autocorrelation follows as:

$$
\hat{R}_{\tau}=\frac{1}{m}\sum_{i=1}^{m-\tau}S_i S_{i+\tau}, \hspace{25px} \tau=0,1,...,m-1
$$

```{note}
Here we use capitals for $\hat{C}_{\tau}$ and $\hat{R}_{\tau}$ since **estimators** are always a function of the random observables $S_t$.
```

### Covariance matrix based on autocovariance

The structure of a covariance matrix for a stationary time series is purely symmetric and it looks like

$$
\Sigma_{S} = \begin{bmatrix} 
\sigma^2 & c_1 & c_2 & \dots & c_{m-1}\\ 
c_1 & \sigma^2 & c_1 & \ddots  & \vdots \\ 
c_2 & c_1 & \sigma^2 &  \ddots & c_2  \\ 
\vdots & \ddots & \ddots & \ddots & c_1\\ c_{m-1} &  & c_2 & c_1 & \sigma^2\end{bmatrix}$$

There are $m$ (co)variance components - **one** variance component, $\sigma^2 = c_0$, and $m-1$ covariance components, $c_i$.


(NACF)=
## Normalized ACF

The least-squares estimator of the autocovariance function (ACF) has some important properties (derivations are outside the scope of MUDE).

The empirical autocovariance function is an unbiased estimator of the formal autocovariance function

$$
\mathbb{E}(\hat{C}_{\tau}) =  c_\tau
$$

The *normalized* autocovariance estimator can directly be obtained from the autocovariance estimator as

$$
\hat{\rho}_{\tau} = \frac{\hat{C}_{\tau}}{\hat{C_0}}, \hspace{20px}\tau = 0,...,m-1 \implies \hat{\rho}_0 = 1
$$

```{note}
The estimated normalized autocovariance is the same as  the time dependent Pearson correlation coefficient.

In literature $\hat{\rho}_{\tau}$ is often referred to as the *autocorrelation function*.
```

The variance of the normalized ACF can be approximated as

$$
\sigma_{\hat{\rho}_{\tau}}^2 = \frac{1}{m-\tau}+\frac{2\hat{\rho}^2_{\tau}}{m}
$$

If $m$ is sufficiently large, $\hat{\rho}_{\tau}$ is normally distributed:

$$
\hat{\rho}_{\tau} \sim N(\rho_{\tau},\sigma^2_{\hat{\rho}_{\tau}})
$$

### Worked example

Let us consider a time series of $m=100$ observations, such that

$$
\hat{\rho}_1 = 0.4
$$

We know that 

$$
\hat{\rho}_1 \sim N(\rho_1,\sigma^2_{\hat{\rho}_1})
$$

with $\rho_1$ unknown and

$$
\sigma^2_{\hat{\rho}_1}=\frac{1}{m-1}+\frac{2\hat{\rho}^2_1}{m}=0.0133\implies\sigma_{\hat{\rho}_1}=0.1153
$$

We will now apply a test whether the estimated autocorrelation is significant. The null hypothesis assumes there is **no** correlation:

* $\mathcal{H}_0$: $\rho_1=0$
* $\mathcal{H}_a$: $\rho_1 \neq 0$

Since we know the distribution of $\hat{\rho}_1$, a suitable test statistic would be:

$$
T = \frac{\hat{\rho}_1}{\sigma_{\hat{\rho}_1}} \sim N(0,1)
$$

where we would reject $\mathcal{H}_0$ if $|T|>k_{\alpha}$. With a false alarm rate of $\alpha = 0.01$, we find that the critical value can be obtained from the [table of the standard normal distribution](tabl\epsilon_standardnormal). Note that we have a 2-sided critical region, hence we need to look up the value for $0.5\alpha$.

In this example, we obtain:

$$
(T = 3.47 ) > (k_{\alpha}=2.58)
$$

and hence the null hypothesis is rejected, implying that the autocorrelation is significant.

:::{card} Exercise

A zero-mean stationary noise process consists of $m=5$ observations:

$$
S = \begin{bmatrix} 2 & 1 & 0 & -1 & -2 \end{bmatrix}^T
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
= \frac{\sum_{i=1}^{m} S_i S_{i+1}}{m-1}
= \frac{2(1) + 1(0) + 0(-1) + (-1)(-2)}{5 - 1}
= \frac{2 + 0 + 0 + 2}{4}
= 1
$$

Giving

$$
\hat{\rho}_1
= \frac{1}{2}
$$

```
:::

<!-- ## Power spectral density

The power spectral density (PSD) explains how the power (variance) of the signal is distributed over different frequencies. For instance, the PSD of a pure sine wave is flat *except* at its constituent frequency, where it will show a peak. Purely random noise has a flat power spectrum, indicating that all frequencies have an identical contribution to the variance of the signal! -->

<!-- The power spectral density (PSD) explains how the power (variance) of the signal is distributed over different frequencies. For instance, the PSD of a pure sine wave is flat *except* at its constituent frequency, where it will show a peak. Purely random noise has a flat power spectrum, indicating that all frequencies have an identical contribution to the variance of the signal!

### PSD vs ACF

Knowledge on ACF, in time domain, is mathematically equivalent to knowledge on PSD, in the frequency domain, and vice-versa. And, from here, you might have a clue of where this is taking us... The PSD is the **discrete Fourier transform (DFT)** of the ACF.

$$
\begin{align*}
\text{DFT}(\hat{c}_{\tau})&=\text{DFT}\left(\frac{1}{m}\sum_{i=1}^m s_i s_{i+\tau}\right)\\&=\frac{1}{m\Delta t}F_S(k) F_S(k)^*\\&=\frac{1}{m\Delta t}|F_S(k)|^2
\end{align*}$$

where the Fourier coefficients (see [DFT section](FFT)) are:

$$F_S(k)  = \Delta t\sum_{i=1}^my_ie^{-j\frac{2\pi}{m}(k-1)(i-1)}$$

```{note}
In signal processing, it is common to write a sampled (discrete) signal as a small letter $s_i$ and the Fourier coefficients with capitals $S_k$. Since we also use capitals to indicate that $S$ is a random variable, we describe the DFT here for a realization $s_i$ of $S_i$, and use the notation $F_S(k)$ for the Fourier coefficients.
```

Conversely, the inverse discrete Fourier transform (IDFT) of the PSD is the ACF, so

$$\text{IDFT}(F_{S}(k))=\hat{c}_{\tau}, \hspace{35px} \tau = 1,...,m \hspace{5px}\text{and}\hspace{5px} k = 1,...,m$$

```{figure} ./figs/ACF_PSD.png
---
height: 300px
name: ACF_PSD
---
Time series data, autocovariance and its power spectral density plots of white noise above and colored noise (not purely random) below.
```

The PSD explains how the power (variance) of the signal is distributed over different frequencies. The PSD of a pure sine wave is flat except at its constituent frequency.
Purey random noise (i.e., white noise) has a flat power, indicating that all frequencies have identical contribution in making the variance of the signal. This is however not the case for time-correlated noise because different frequencies have different power values in making the total signal variability.
 -->
