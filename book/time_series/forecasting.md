(forecast)=
# Forecasting

```{admonition} MUDE Exam Information
:class: tip, dropdown
The material on this page is provided to give you extra insight into time series analysis and how it is used in practice. This material is not part of the exam.
```

Time series analysis is about analyzing time series of data points of a variable, with the goal to extract meaningful characteristics and statistics of the data, e.g., to study the trend and seasonality. Very often we do so in order to be able to predict future values based on the previously observed ones, which is referred to as **forecasting**.

In this part of the book, you first learned about the components that can be distinguished ([Chapter 4.1](components)) in time series. Some of the components may relate to the *signal-of-interest*. However, another important component that we have to deal with is the noise.

Modelling and estimating the signal-of-interest ([Chapter 4.3](modelling_tsa)) using the concepts of observation theory. The remainder of this chapter focused on the noise modelling. In order to do so, we need to work with *stationary*, i.e., time series of which the statistical properties do not depend on the time of observation ([Chapter 4.4](stationary)). An example of a stationary time series are the residuals after best linear unbiased estimation. Using these residuals as the input for noise modelling makes sense, since in fact the residuals are estimates of the noise. 

A problem with the noise process of a time series is that often there is auto-correlation: in contrast to a white noise signal, the observations with different time lags depend on each other - this is referred to as colored noise. The dependence can be modelled by the autocovariance function ([Chapter 4.5](ACF)). With that, the noise process can be modelled using the Autoregressive model ([Chapter 4.6](AR)).

Now that we are able to model both signal-of-interest and the noise process, we can start forecasting.

In summary, given a time series $Y=\mathrm{Ax}+\epsilon$, the workflow is as follows:

1. Estimate the signal-of-interest $\hat{X}=(\mathrm{A}^T\Sigma_{Y}^{-1}\mathrm{A})^{-1}\mathrm{A}^T\Sigma_{Y}^{-1}Y$.

2. Model the noise using the Autoregressive (AR) model, using the stationary time series $S:=\hat{\epsilon}=Y-\mathrm{A}\hat{X}$.

3. Predict the signal-of-interest: $\hat{Y}_{signal}=\mathrm{A}_p\hat{X}$, where $\mathrm{A}_p$ is the design matrix describing the functional relationship between the future values $Y_p$ and $\mathrm{x}$.

4. Predict the noise $\hat{\epsilon}_p$ based on the AR model. $\hat{\epsilon}_p = \Sigma_{Y_pY}\Sigma_Y^{-1}\hat{\epsilon}$, where $\Sigma_{Y_pY}$ is the covariance matrix between the future values $Y_p$ and the observed values $Y$.

5. Predict future values of the time series: $\hat{Y}_p=\mathrm{A}_p\hat{X}+\hat{\epsilon}_p$.

```{note}
This procedure is a general approach to forecasting time series data. It resembles the process of stochastic inter- and extrapolation, which is used in many fields of science and engineering.
```

