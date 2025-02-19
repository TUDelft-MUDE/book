# Time Series Analysis 

In this chapter, we will first introduce the components to describe a time series: trend, signal, offsets, irregularities and noise. It will then be shown how to estimate the signal-of-interest (everything except noise).

Next, we will consider stationary time series, meaning that the statistical properties do not depend on the time when the time series was observed. The stationary time series describe an underlying stochastic process, which can then be modelled, for instance using an Autoregressive (AR) model. The final goal is to use the time series for estimating the components such as trend and seasonality, as well as to predict future values, for which we do need to take into account the stochastic process.

```{figure} ./figs/tsa_cover.png
:name: cover
:width: 600px
:align: center

Recorded and expected global warming from 1960 to 2100, from IPCC report ([Masson-Delmotte, et al. (20219)](https://www.researchgate.net/profile/Peter-Marcotullio/publication/330090901_Sustainable_development_poverty_eradication_and_reducing_inequalities_In_Global_warming_of_15C_An_IPCC_Special_Report/links/6386062b48124c2bc68128da/Sustainable-development-poverty-eradication-and-reducing-inequalities-In-Global-warming-of-15C-An-IPCC-Special-Report.pdf))
```
