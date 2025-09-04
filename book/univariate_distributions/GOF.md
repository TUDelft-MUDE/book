
# Goodness of Fit

In the previous sections, you have studied the different mathematical models (continuous distribution functions) that we can use to model the univariate uncertainty of a random variable and how to fit them based on observations. Also, you have been introduced to some methods to fit those distributions. **But how do we choose between different distributions?**

The choice of the appropriate distribution function needs to be based first on the **physics of the random variable** we are studying. For instance, if we are studying the concentration of a gas in the atmosphere, negative values do not have a physical meaning, so the selected distribution function should have zero probability density for negative values.

Once we have accounted for the physical characteristics of the random variable, we can make use of **goodness of fit (GOF) techniques** to validate our choice. That is to say, GOF techniques are not a ground truth, but an objective way of comparing different distribution choices. Different techniques may lead to different judgments and it is ultimately your task as an expert to balance those outputs and select the best model to your judgment. Thus, it is generally recommended to use more than one GOF technique in the decision-making process. In the subsequent sections, we present some commonly used GOF techniques in the statistics field.

**Let's take a look at an example:** In order to illustrate these techniques, we will use a toy example. The set of observations is represented in the plots below by its pdf and cdf. In the following, we will investigate a number of GOF techniques to determine which distribution best fits the data.

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_empirical_pdf_and_cdf.html
:name: empirical_pdf_and_cdf
:aspectratio: 2 / 1

The data we will use for the GOF demonstrations. Hover over the figure to highlight the corresponding bins in the histogram and CDF.
````

## Graphical methods

GOF graphical methods are useful tools to have a first intuition of how different models are performing and confirm the results of other quantitative analysis. Here, you are introduce to three techniques: (1) QQ-plot, (2) Log-scale, and (3) Probability plot.

### QQ-plot

This technique is as simple as comparing the observations used to fit the model with the predictions of the model. Typically, the observations are represented in the x-axis and the predictions in the y-axis. Therefore, the perfect fit would be represented by the $45 ^\circ$-line.

Let's see it applied to the example data. Note that the term *"quantile"* is used in statistics to denote the values of the random variable.

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_QQ_plot.html
:name: QQ_plot
:aspectratio: 2 / 1

Select a distribution and adjust the parameters using the sliders. Observe how the QQ plot changes in response. The data above is a synthetic example - which distribution do you believe generated the samples?
````

If we select a **Gumbel distributions** with the parameters $\mu=1$ and $\beta=1$, you can see that the samples closely follow the $45 ^\circ$-line[^Gumbeldata]. Those provided by the Exponential distributions (or the Gumbel dsitribution with other parameters) deviate further from the diagonal line. Based on this graphical technique, it is possible to conclude that Gumbel distribution seems to be a suitable model for the data.


**Let's code it!**

Pseudo code to build a QQ-plot is presented below to illustrate the procedure.

    read observations

    # Calculate the empirical cdf
    p_emp, q_emp = empirical CDF of observations

    # Define the parameters of the chosen distribution, e.g., a Gaussian PDF
    mean_gaussian = 5.17
    sd_gaussian = 5.76
    
    # Compute the values of the random variable predicted by the Normal distribution
    q_gaussian = CDF of Normal distribution evaluated in p_emp with parameters mean_gaussian and sd_gaussian

    scatterplot of q_emp versus q_gaussian

### Log-scale

As previously introduced, the tails of the distributions are key to allow the inference of extreme values which have not been observed yet. Therefore, it is important to check whether the distribution used to model the observations is performing properly in that region. A simple trick to do so is to use a logarithmic scale (log-scale) to represent the exceedance probability plot. That way, we "zoom in" on those points in the tail instead of focusing on the bulk of the data:

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_log_scale_plot.html
:name: log_scale_plot
:aspectratio: 2 / 1

Select a distribution and adjust the parameters using the sliders. Observe how the logarithmic exceedance probability plot plot changes in response.
````

If we are interested in extreme events, it is important to find a distribution that fits the tail samples well. Experiment with different distributions and observe how they behave in the tails.

### Probability plot or probability paper

This graphical technique consists on adapting the axis of the plot of the cdf accounting for the parametric distribution fitted so it is presented as a line. This is, the cdf of any Gaussian distribution will be plotted as a line in the Normal probability plot. Thus, in the x-axis a function of the values of the random variable is presented, while in the y-axis a function of the non-exceedance probabilities is shown. 

Let's see it with the example of the Exponential distribution. Its cdf is given by

$$
F(x) = 1 - exp(-\lambda[x-\mu])
$$

where $\lambda$ is the scale parameter and $\mu$ is the location parameter. A transformation is performed on the cdf so a linear relationship is established between the value of the random variable X and the non-exceedance probabilities. In the case of the Exponential distribution, it is just a matter of calculating logarithms to both sides of the equation as

$$
ln[1-F(x)] = -\lambda[x-\mu]
$$

In this manner, there is a linear relationship between $ln[1-F(x)]$ and $x$. Note that in the case of the Exponential distribution, the probability plot is the same as the log-scale! Therefore, the Exponential distribution was shown as a straight line in the previous plot, while the Gaussian distribution was not.

## Formal hypothesis test: The Kolmogorov-Smirnov test

The **Kolmogorov-Smirnov (KS) test** is one of the most popular nonparametric formal hypothesis tests in statistics. It can be used for two purposes: (1) to compare a sample with a reference parametric distribution, or (2) to compare two empirical distributions. Here, we consider first option, since it is the one used for GOF purposes. Thus, this test aims to determine how likely is that a sample was drawn from the reference parametric distribution.

This test is based on the KS statistic, which is (roughly) the maximum distance between the empirical cumulative distribution and the parametric distribution fitted to those observations. This statistic is mathematically defined as

$$
D_n = sup_x|\hat{F}(x)-F(x)|
$$

where $D_n$ is the KS statistic, $sup_x$ is the supremum of the set distances (intuitively, the largest absolute difference between the two distribution functions across all the values of the random variable $X$), $\hat{F}(x)$ is the empirical cumulative distribution and $F(x)$ the fitted parametric cumulative distribution.

Once $D_n$ is computed, a formal hypothesis test is performed. The null hypothesis corresponds to $\hat{F}$ having the same distribution as $F$. In mathematical terms:

$$
H_0: \hat{F} \sim F
$$

The distribution of $D_n$ has been already calculated and included in different statistic packages, since it depends on the considered parametric distribution. These distributions can be used to calculate the probability of the null hypothesis being true (called $p-value$). A significance level needs to be selected (typically, $\alpha=0.05$) as a threshold to determine whether the null hypothesis is rejected or accepted. This is, if the probability of $H_0$ being true ($p-value$) is below $\alpha$, $H_0$ is rejected, so the empirical cumulative distribution is not coming from the fitted parametric cumulative distribution.

Let's see it in an example. In the figure below, both the empirical distribution (step function) and the fitted normal distribution are shown. The maximum distance between both distributions is also presented in red.

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_KS_test.html
:name: KS_test
:aspectratio: 2 / 1

Select a distribution and adjust the parameters using the sliders. Observe how the KS statistic $D_{n}$ changes in response. The red vertical line demarkates the largest deviation between the empirical and theoretical PDF.
````

# Let's practice

An engineer is characterizing the axle loads transmited by the traffic on a bridge. Based on the observations, a Normal and a Gumbel distributions are fitted, as shown in the figure below. 

```{figure} https://files.mude.citg.tudelft.nl/GOF_ex.png

---

---
Comparison between the observations of axel loads and the fitted Normal and Gumbel distributions: (a) PDF, and (b) Exceedance curve.
```

The engineer needs to select a parametric distributions since he/she needs to infer extreme loads that have not been observed yet. In order to decide which distribution to apply for further analysis, the engineer has plotted the Exceedance Curve (1-CDF) in log-scale (previous figure) and has performed the Kolmogorov-Smirnov test. The results are:

- Normal distribution: $p-value \approx 0.07$
- Gumbel distribution: $p-value \approx 0$

Which distribution should be chosen by the engineer?

```{admonition} Answer
:class: tip, dropdown

According to the Kolmogorov-Smirnov test, it is not possible to reject that the observations are coming from a Normal distribution, while it is possible to do so for the Gumbel distribution. Therefore, if we would only trust on the Kolmogorov-Smirnov test, Normal distribution would be chosen.

However, the plot in log-scale is also available. There, it is shown how the Gumbel distribution fits way better the tail of the empirical distribution. Since the goal of the engineer is to infer events that have not been observed yet (extrapolate), the tail is extremely important. Consequently, Gumbel distribution would be preferred in this context to model the axel loads observations.

```

[^Gumbeldata]: In fact, the data has been synthetically generated from a Gumbel distribution with the parameters $\mu = 1$ and $\beta = 1$.

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre, Robert Lanzafame, and Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT