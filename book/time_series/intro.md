(tsa)=
# Time Series Analysis 

% START-CREDIT
% source: time_series_analysis
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Alireza Amiri-Simkooei, Christiaan Tiberius and Sandra Verhagen. {ref}`Find out more here <time_series_analysis_credit>`.
```
% END-CREDIT

In this chapter, we introduce the components to describe a time series: trend, seasonal variation, offset and noise. We then show how to estimate the signal-of-interest (which is everything except noise).

Next, we consider stationary time series, meaning that the statistical properties do not depend on the time when the time series was observed. A stationary time series represents an underlying stochastic process, which can then be modelled, for instance using an Autoregressive (AR) model. The final goal is to use the time series for estimating components such as trend and seasonality, as well as to predict future values, for which we do need to take into account also the stochastic process.

```{figure} https://files.mude.citg.tudelft.nl/tsa_cover.png
:name: cover
:width: 600px
:align: center


Recorded and expected global warming from 1960 to 2100, from {cite:t}`ipcc2018`.

```
