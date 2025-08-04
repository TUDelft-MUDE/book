# Time Series Analysis 

In this chapter, we will first introduce the components to describe a time series: trend, signal, offsets, irregularities and noise. It will then be shown how to estimate the signal-of-interest (everything except noise).

Next, we will consider stationary time series, meaning that the statistical properties do not depend on the time when the time series was observed. The stationary time series describe an underlying stochastic process, which can then be modelled, for instance using an Autoregressive (AR) model. The final goal is to use the time series for estimating the components such as trend and seasonality, as well as to predict future values, for which we do need to take into account the stochastic process.

```{figure} https://files.mude.citg.tudelft.nl/tsa_cover.png
:name: cover
:width: 600px
:align: center

Recorded and expected global warming from 1960 to 2100, from IPCC report ([Masson-Delmotte, et al. (2019)](https://www.ipcc.ch/sr15/))
```
