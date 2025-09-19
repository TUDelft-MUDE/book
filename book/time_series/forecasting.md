(forecast)=
# Forecasting

```{admonition} MUDE Exam Information
:class: tip, dropdown
The material on this page is provided to give you extra insight into time series analysis and how it is used in practice. This material is not part of the exam.
```
Time series analysis focuses on examining data points collected over time to extract meaningful patterns, such as trends, seasonal cycles, and other temporal components. Very often we do so in order to be able to predict future values based on the previously observed ones, which is referred to as **forecasting**.

In this part of the book, you first learned about the components that can be distinguished ([Chapter 4.1](components)) in a time series. Some of the components relate to the *signal-of-interest* and others with the *noise* ([Chapter 4.2](noise)). Modelling and estimating the signal-of-interest was explained in [Chapter 4.3](modelling_tsa), using the concepts of [Observation Theory](ObsTheory).

To be able to estimate future values of the time series (forecasting), we need to first estimate the functional model components of the time series. Additionally, the remaining time series needs to be *stationary*, i.e., the statistical properties do not change over time ([Chapter 4.4](stationary)). We considered a white noise time series, and the AR(1) process with $|\phi| < 1$. To turn a time series into a stationary one, we can detrend it and use the residuals from a least-squares fit for stochastic noise modelling.

After ensuring the time series is stationary, we can perform a stochastic analysis. In some cases the noise is not white but auto-correlated, meaning that the observations at neighbouring time instants depend on each other. This type of noise is referred to as colored noise. The dependence as a function of the time lag can be analysed using the autocovariance function ([Chapter 4.5](ACF)). Based on the ACF, the noise process can often be modelled using the Autoregressive model ([Chapter 4.6](AR)). The order of the AR model depends on the data. Apart from the AR process, many other stochastic processes exist, such as ARMA and ARIMA, but these are outside the scope of MUDE. In this course, we focus on AR with order 1, denoted as AR(1). Based on the AR(1) process, to model the noise in the time series we need to estimate parameter $\phi$.

Once the signal-of-interest and the noise process are characterized and modelled, we can forecast future values of the time series.

In summary, given a time series $Y=\mathrm{Ax}+\epsilon$, the workflow is as follows:

1. Estimate the signal-of-interest $\hat{X}=(\mathrm{A}^T\Sigma_{Y}^{-1}\mathrm{A})^{-1}\mathrm{A}^T\Sigma_{Y}^{-1}Y$.

2. Model the noise, in the MUDE, using the Autoregressive (AR) model, using the stationary time series $S:=\hat{\epsilon}=Y-\mathrm{A}\hat{X}.$

3. Predict the signal-of-interest: $\hat{Y}_{signal}=\mathrm{A}_p\hat{X}$, where $\mathrm{A}_p$ is the design matrix describing the functional relationship between the future values $Y_p$ and $\mathrm{x}$.

4. Predict the noise $\hat{\epsilon}_p$ based on the AR model. $\hat{\epsilon}_p = \Sigma_{Y_pY}\Sigma_Y^{-1}\hat{\epsilon}$, where $\Sigma_{Y_pY}$ is the covariance matrix between the future values $Y_p$ and the observed values $Y$. A mathematical proof of this formula can be found in Chapter 11 of [Surveying and Mapping](https://doi.org/10.5074/T.2021.007); Eq. (11.11) though beyond the scope of the MUDE.

5. Predict future values of the time series: $\hat{Y}_p=\mathrm{A}_p\hat{X}+\hat{\epsilon}_p$.

```{note}
This procedure is a general approach to forecasting time series data. It resembles the process of stochastic inter- and extrapolation, which is used in many fields of science and engineering.
```

% START-CREDIT
% source: time_series_analysis
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Alireza Amiri-Simkooei, Christiaan Tiberius and Sandra Verhagen. {ref}`Find out more here <time_series_analysis_credit>`.
```
% END-CREDIT
