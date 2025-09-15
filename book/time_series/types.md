(timetypes)=
# Types of time series

Time series can be classified based on different properties. Thus, let us start by distinguishing the different types of time series we can find.

### Continuous vs discrete

When observations are made continuously through time, that gives rise to a **continuous** time series.

In practice, we deal with **discrete** time series, since observations are taken only at specific time instances. They are usually equally spaced, even the measured variable can in
principle be a continuous variable.


```{note}
In this course, we will only focus on **discrete** time series, with a focus on continuous modelling.
```

### Parametric vs non-parametric

**Parametric** time series analysis consist of a trend, signal and noise. We can apply estimation theory to estimate the trend and signal, for which we need the functional model, while also taking into account the noise via the stochastic model (see [Chapter Observation Theory](OT)).

For **non-parametric time series analysis** we need data-driven methods, such as:
  * Singular spectrum analysis (SSA)
  * Wavelet transform
  * Machine learning methods

```{note}
Here, we will only take a deeper look to parametric time series!
```

### Univariate vs multivariate

We call a time series **univariate** when only a single sequence of data is analyzed. Usually we study the time evolution of that one single variable!

On the other hand, it can be useful to consider a **multivariate** time series - several sets of data for the same sequence of time periods are analyzed. As an example, we can look at the figure {numref}`pollution_concentration` here presented that describes the evolution of pollution concentration, which is a function of all the other variables plotted (e.g. dew, temperature, pressure, wind direction, etc.).

```{note}
We will mainly focus on univariate time series analysis from here on!
```

```{figure} ./figs/pollution_concentration.png
:name: pollution-concentration
:width: 600px
:align: center

Multivariate time series of pollution concentration (top) as a function of itself and other time series such as dew, temperature, pressure, wind direction, etc.
```

### Static vs dynamic

When analyzing time series, prediction and analysis of events can be performed in two different ways:

* Sequentially in a **recursive form**, called dynamic mode.
* In a **batch form**, the so-called static mode.

**Static mode** can be considered when the standard least-squares method can be used to estimate time-invariant parameters, for example velocity.

On the other hand, the **dynamic mode** can be considered when dynamic least-squares (e.g. Kalman filter) is used to study and estimate time-varying parameters.

```{note}
We will only focus on static time series from here on!
```

## Additional concepts

In [Signal Processing](SP) the data is just considered to be the signal of interest, whereas here we assume the data is "contaminated" with noise, i.e.

$$Y = \text{signal} + \text{noise} $$

Time series analysis means understanding patterns and, hence, extracting the **signal of interest** from the noisy data.

### Signal and noise

How can we describe both signal and noise?

* **Signal** - the meaningful information that we want to detect: deterministic characteristics by means of mathematical expressions to capture for example trend, seasonality and offsets.

* **Noise** - random and undesired fluctuation that interferes with the signal: stochastic process are needed to describe this. Parts of the time-correlated noise  needs to be accounted for in prediction, see later {ref}`ARMA`. 

The example in {numref}`signal_noise` shows that the *signal* can be described by $\cos(2\pi t f + \phi)$, where frequency $f$ and phase $\phi$ may be the unknown parameters of interest. The stochastic model (assuming independent observations) would be a scaled identity matrix with variance equal to 1 (middle panel) and 3 (bottom panel), respectively. The signal of interest has been entirely hidden in the background noise in the bottom panel. {ref}`psd` and {ref}`LS-HE` can be used to detect the frequency.

```{figure} ./figs/signal_noise.png
:name: signal_noise
:width: 600px
:align: center

Example of a time series (top graph) affected by noise with different strengths (middle and bottom figures). Note the different scales on the vertical axes.
```

### Prediction, filtering and smoothing

Time series analysis can have two main goals:

* To explain the *past* and *present* state of a process:
identifying the nature of the phenomenon represented by the time series data to study long term
trend, seasonality and noise process of the time series

* To use the past data for predicting *future* values: prediction or forecasting uses the past observed values of the time series, try to model, and
hence predict future time series values. Think of forecasting sales of a particular product,
forecasting of stock price, or weather forecasting.

Estimating a state in the past and future is referred to as *smoothing* and *filtering*, respectively.


![prediction](./figs/prediction.png "prediction")

% START-CREDIT
% source: time_series_analysis
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Alireza Amiri-Simkooei, Christiaan Tiberius and Sandra Verhagen. {ref}`Find out more here <time_series_analysis_credit>`.
```
% END-CREDIT