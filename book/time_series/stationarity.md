(stationary)=
# Time Series Stationarity
In Section [Components of time series](forecast) it was pointed out that a time series $Y(t) = [Y(t_1), Y(t_2), \ldots, Y(t_m)]^T$ is a sequence of random variables. Each element $Y(t_i)$ is a random variable, with a probability density function denoted by $f_{Y(t_i)}(y)$.

A time series results from observing a stochastic process. A stochastic process is a phenomenon, taking place as time goes by, which is subject to uncontrolled variability and associated uncertainty, and additional variability is typically involved in the observation of the process.

Would we observe it as a continuous function of time, then $Y(t)$ is a random variable which depends on time, and hence the probability density function of $Y(t)$ would carry also time $t$ as an argument, $f_{Y(t)}(y,t)$, modelling the variability in the outcomes of $Y(t)$.

A time series results from observing the stochastic process at discrete instants in time, resulting in a sequence of random variables $Y(t_i)$ with associated the aforementioned PDF evaluated at times $t_i$: $f_{Y(t_i)}(y,t_i)$, with $i=1,\ldots,m$.

The PDF carries time as an argument, meaning first that it depends on time and that the variability described by it may change as a $\textit{function of time}$ (though soon we will assume that the process is stationary, and hence that it does not), and second that there may exist $\textit{dependence in time}$, such that neighbouring elements of the time series, e.g. $Y(t_2)$ and $Y(t_5)$, are correlated, in which case we could say that the process has a kind of memory. This 'time correlation', very common in practice, must be properly taking into account when we estimate (predict) future values of the time series, and this is the goal of the remaining sections of this chapter on Time Series Analysis.

In the sequel we focus on the noise-component of the time series. We assume that the signal-part has been appropriately taken care of through estimation of the components in the functional model (such as trend and seasonality). We work with time series $S = \hat{\epsilon} = Y - A \hat{X}$, hence the residuals which remain after estimation of the components of the functional model, and ideally have zero mean.


```{admonition} Definition
A stationary time series $S(t)$ is based on an underlying stochastic process of which the statistical properties do not depend on the time at which it is observed.
```

This means that parameters such as *mean* and *(co)variance* should remain constant over time and not follow any trend, seasonality or irregularity:

* Mean of the process is time-independent

$$\mathbb{E}(S(t))=\mathbb{E}(S_t)=\mu$$

* Covariance of the process is independent of $t$ for each time shift $\tau$ (so only a function of $\tau$ and not t):

$$
Cov(S_t,S_{t-\tau})= Cov(S_t,S_{t+\tau}) =\mathbb{E}((S_t-\mu)(S_{t-\tau}-\mu))=c_\tau
$$

* The variance (i.e., $\tau=0$) is then also constant with respect to time :

$$
Var(S_t)=\mathbb{E}((S_t-\mu)^2)=c_0=\sigma^2
$$

Notice that we have introduced the new notation $S_t$ to denote a stationary time series. The time series $Y_t$ is then potentially a non-stationary time series.

The white noise stochastic model introduced here is stationary ([Section 4.2](noiseandstoch)).

## Why stationary time series?

Stationarity is important if we want to use a time series for forecasting (predicting future behaviour), which is not possible if the statistical properties change over time.

In practice, we may in fact be interested in for instance the trend and seasonality of a time series. Also, many real-world time series are of course non-stationary. Therefore the approach is to first "stationarize" the time series (e.g., remove the trend), use this stationary time series to predict future states based on the statistical properties (stochastic process), and then apply a back-transformation to account for the non-stationarity (e.g., add back the trend).

(stationarize)=
## How to "stationarize" a time series?

There are several ways to make a time series stationary. In this course we will focus on detrending the data using least-squares fit.

### Least-squares fit

If we can express the time series $Y=[Y_1, ..., Y_m]^T$ with a linear model of observation equations as $Y = \mathrm{Ax} + \epsilon$, we can apply [best linear unbiased estimation](BLUE) to estimate the parameters $\mathrm{x}$ that describe e.g. the trend and seasonality:

$$
\hat{X}=(\mathrm{A}^T\Sigma_{Y}^{-1}\mathrm{A})^{-1}\mathrm{A}^T\Sigma_{Y}^{-1}Y 
$$

A detrended time series is obtained in the form of the residuals 

$$
\hat{\epsilon} = Y - \mathrm{A}\hat{X}
$$ 

The **detrended $\hat{\epsilon}$ is assumed to be stationary** for further **stochastic analysis**. This is also an admissible transformation because $Y$ can uniquely be reconstructed as $Y=\mathrm{A}\hat{X}+\hat{\epsilon}$. 

Let us take a look into an example:

```{figure} https://files.mude.citg.tudelft.nl/least_squares.png 
---
height: 300px
name: least_squares
---
Example of a time series (right graph) with linear and seasonal trend. The residuals (= stationary time series) after applying BLUE are shown on the left.
```

In the example above, for each observation $Y_i = y_0+ rt_i+a\cos(2\pi f_1t_i)+b \sin(2\pi f_1t_i) +\epsilon_i$, where $a$ and $b$ describe the seasonality and $y_0$ and $r$ the trend. The time series is then:

$$
\begin{bmatrix}
    Y_1 \\ Y_2 \\  \vdots \\ Y_m
\end{bmatrix} = \begin{bmatrix}
    1&t_1&\cos(2\pi f_1 t_1) & \sin(2\pi f_1 t_1) \\
     1&t_2&\cos(2\pi f_1 t_2) & \sin(2\pi f_1 t_2) \\
       \vdots & \vdots & \vdots & \vdots \\ 
     1&t_m&\cos(2\pi f_1 t_m) & \sin(2\pi f_1 t_m)
\end{bmatrix}
\begin{bmatrix}
y_0 \\ r \\ a \\ b \end{bmatrix} + 
\begin{bmatrix}
    \epsilon(t_1) \\ \epsilon(t_2) \\  \vdots \\ \epsilon(t_m)
\end{bmatrix}
$$

The time series of the residuals $\hat{\epsilon} = Y-A\hat{X}$ (left graph) is indeed a stationary time series.

:::{card} Question Stationary Time Series

Which of the four options is a stationary time series?

```{figure} https://files.mude.citg.tudelft.nl/stat_question.png
---
height: 300px
name: stationary_example
---
Example of a stationary time series.
```

````{admonition} Solution
:class: tip, dropdown

The time series in the second panel is stationary. The mean and variance are constant over time.
````
:::



### Other ways to make a time series stationary
When model specification is not straightforward, other methods can be used to make a time series stationary. Two common methods are single differencing and moving average. Single differencing of $Y=[Y_1,...,Y_m]^T$ creates a time series $\Delta Y_t=Y_t - Y_{t-1}$ (long term trends are removed in this way). Another way to create an (almost) stationary time series is by taking the moving average of the time series, where we apply a moving average of $k$ observations to the time series $Y$ to create a new time series $\bar{Y}_t = \frac{1}{k}\sum_{i=1}^{k}Y_{t-i}$ (short term variations are removed in this way), and then take the difference between the original time series and the moving average to obtain a (nearly) stationary time series $\Delta Y_t = Y_t - \bar{Y}_t$.

Both these methods do not require a model specification. So in cases where the model is not known, these methods can be used to make the time series stationary.


## ... and then what?

We have seen different ways of obtaining a stationary time series from the original time series. The reason is that in order to make predictions (forecasting future values, beyond the time of the last observation in the time series) we need to account for both the **signal-of-interest** and the **noise**. [Estimating the signal-of-interest](modelling_tsa) was covered in the previous section. In the next sections we will show how the noise can be modelled as a stochastic process. Given a time series $Y=\mathrm{Ax}+\epsilon$, the workflow for prediction is as follows:

1. Estimate the signal-of-interest $\hat{X}=(\mathrm{A}^T\Sigma_{Y}^{-1}\mathrm{A})^{-1}\mathrm{A}^T\Sigma_{Y}^{-1}Y$ (Section [Modelling and estimation](modelling_tsa)).

2. Model the noise using for instance an Autoregressive (AR) model, using the stationary time series $S:=\hat{\epsilon}=Y-\mathrm{A}\hat{X}$ (Section [AR](AR)).

3. Predict the signal-of-interest: $\hat{Y}_{signal}=\mathrm{A}_p\hat{X}$, where $\mathrm{A}_p$ is the design matrix describing the **functional** relationship between the future values $Y_p$ and $\mathrm{x}$ (Section [Forecasting](forecast)).

4. Predict the **stochastic** noise $\hat{\epsilon}_p$ based on the AR model.

5. Predict future values of the time series: $\hat{Y}_p=\mathrm{A}_p\hat{X}+\hat{\epsilon}_p$ (Section [Forecasting](forecast)).

Resulting in estimates $\hat{Y}_p$ of the time series at future times $t_p$, beyond he time of the last observation $t_m$ in the time series.

% START-CREDIT
% source: time_series_analysis
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Alireza Amiri-Simkooei, Christiaan Tiberius and Sandra Verhagen. {ref}`Find out more here <time_series_analysis_credit>`.
```
% END-CREDIT
