(01_monte_carlo_propagation)=
# Monte Carlo simulations for uncertainty propagation

In the previous parts we learned how a transformation of random variables lead to random outputs with a different distribution. Moreover, we also saw how to propagate **means** and **(co)variances** via linearization, including the exact linear case. Alternatively, Monte Carlo (MC) simulations are very effective tools when models are highly non-linear, or when inputs are non-Gaussian, or when we need the **full distribution** rather than just principal moments. 

:::{card} Historic curiosity
The **Monte Carlo** method traces its roots to early probability puzzles (e.g., Buffon’s needle), but it consolidated during the **1940s** at **Los Alamos** for **neutron transport** in the Manhattan Project. **Stanislaw Ulam** conceived the idea after card‐game thought experiments; practical algorithms and early random number routines were later developed by **John von Neumann** and **Nicholas Metropolis**. Still, the name “Monte Carlo” (Metropolis) actually nods to the Monaco casino — randomness as a computational tool. In fact, foundationally, the MC approach relies on the **law of large numbers** to estimate expectations by sampling, with examples in the 50s-60s related to **variance-reduction** ideas (e.g., importance sampling). Since then, faster computers and better random-number generators have made Monte Carlo a standard tool in science and engineering.
:::

---

## Simulating Mean and Variance of transformed variable
**Goal.** Given a model $X = q(Y)$ and an input univariate distribution $p_Y$, estimate mean and variance by random sampling.

From the general analytical expression provided for **Expectation law** and **Variance law**, we observe that we can replace the equalities by a numerical approximation such as

$$
\mathbb{E}(X) = \mathbb{E}( q(Y) ) \approx \frac{1}{N}\sum_{i=1}^{N} q(Y_i) = \hat{\mu}_X
$$

$$
\mathrm{Var}(X) = \mathrm{Var}( g(Y) ) \approx \frac{1}{N-1}\sum_{i=1}^{N} [ q(Y_i) - \hat{\mu}_X ] [ q(Y_i) - \hat{\mu}_X ]^T
$$

which refer to the sample mean and the sample variance, respectively. The standard error on the mean will decrease with $1/\sqrt{N}$. Observe that in the second expression we have $N-1$ in the denominator since we do not know the true mean $\mathbb{E}( q(Y) )$ and therefore we first estimate it by the **sample mean** of the data $\{Y_1, ...Y_N\}$. This means that we have used one degree of freedom and an unbiased estimator of the variance is obtained by using $N-1$ instead of $N$.

**NOTE** The expressions for multivariate functions and distributions follow trivially adopting the same definition in $\mathbb{R}^n$.


## Comparing Taylor approximation and MC simulations
At this point, we can look at a numerical example where we aim to compute the sample mean and variance for a given non-linear transformation $X = q(\mathbf{Y})$, where $q: \mathbb{R}^n \rightarrow \mathbb{R}$. Then, we will find the mean and variance of $X$ based on a Taylor expansion, as well as Monte Carlo simulations. In the latter case we will adopt the following procedure:
1. Generate $N$ samples from $\mathbf{Y} \sim \mathcal{N}(\boldsymbol\mu_Y,\boldsymbol\Sigma_Y)$, e.g. assumed to be normally distributed;
2. Propagate each sample $\mathbf{Y}_i$ via this non-linear transformation, i.e. $X_i = q(\mathbf{Y}_i)$;
3. Compute sample mean and variance from $X_i,\forall i=1...N,$ using the aforementioned expressions.

### Barometric formula for an adiabatic atmosphere
The problem considered concerns ideal gas with tropospheric constant lapse rate (change of temperature with altitude). A dependence of atmospheric pressure on altitude is given by the barometric law, i.e.

$$
p(h) = p_0 \left( 1 -\frac{L}{T_0} h \right)^\kappa, \qquad \kappa = \frac{g}{R_d L}
$$

where 
* $p_0$ is the standard atmospheric pressure at sea level, e.g. $101,325 \; \rm{Pa}$;
* $L$ is the temperature lapse rate, e.g. $0.0065 \; \rm{K°/m}$;
* $h$ is the height (in meters) above mean sea level;
* $T_0$ is the sea-level reference temperature (in Kelvin), e.g. $288.15 \; \rm{K°}$;
* $g$ is the gravitational acceleration near Earth’s surface, e.g. $9.80665 \; \rm{m/s^2}$;
* $R_d$ is the specific gas constant for dry air, e.g. $287.05 \; \rm{J (kg/K°)^{-1}} $;

and in many cases we can generally approximate $\kappa \approx 5.256$ for the sake of simplicity.

### Example (univariate distribution)
We assume to be at an altitude of 6 km ($\mu_h$), with an uncertainty given by a standard deviation of 100 m ($\sigma_h$). Then, we assume $h \sim \mathcal{N}(6 \; km, 100^2 \; m^2)$, so normally distributed, and we seek the mean and standard deviation of $p(h)$, where its derivative with respect to $h=\mu_h$ is given by

$$
\frac{dp(\mu_h)}{dh} = -\frac{\alpha \kappa}{1-\alpha \mu_h}p(\mu_h), \qquad \alpha = \frac{L}{T_0}
$$

therefore the Taylor (1st order) approximation leads to

$$
\mathbb{E}(p(h)) \approx p(\mu_h)
$$

$$
\mathrm{Var}(p(h)) \approx \sigma_h^2 \cdot \left( \frac{dp(\mu_h)}{dh} \right)^2
$$

Let's now observe how this compares with MC simulations for different number of samples between $10^3$ and $10^7$. In the following plots we observe - for Mean (left) and Standard Deviation (right) - the results based on Taylor (1st order) approximation in red, along with MC results in blue color.  

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/PLOT_BarometricLaw_uncertainty_propagation_1D.png
:align: center

Mean and Standard Deviation computed via Taylor (1st order) approximation and Monte Carlo simulations.
```

It is visible how results become stable using over $10^6$ samples, nonetheless the Taylor method provides only good results for the standard deviation. For the mean, an offset is visible and this is consequence of higher order terms (i.e. mean-bias correction) that has been neglected in the Taylor approximation.

We attempt now to introduce the mean-bias correction from Taylor second order approximation, where second derivative in $h=\mu_h$ is given by

$$
\frac{d^2p(\mu_h)}{dh^2} = \frac{\alpha^2 \kappa(\kappa-1)}{(1-\alpha \mu_h)^2}p(\mu_h)
$$

therefore the Taylor (2nd order) approximation leads to

$$
\mathbb{E}(p(h)) \approx p(\mu_h) + \frac{\sigma^2_h}{2}\frac{d^2p(\mu_h)}{dh^2}
$$

The results below demonstrates how thanks to Monte Carlo simulations it was possible to identify errors in the Taylor-based approximation, considering that an analytic expression for second derivate was relatively simple for this illustrative example. Moreover, we also saw how a large number of samples is necessary in order to correctly approximate the Mean and Variance of transformed variables, especially if subject to high non linearities. 

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/PLOT_BarometricLaw_uncertainty_propagation_1D_with_MeanCorr.png
:align: center

Mean and Standard Deviation computed via Taylor (2nd order) approximation and Monte Carlo simulations.
```

However, in real world problems these analytical approximations are generally not trivial, especially for multivariate cases, and MC methods offers a highly effective numerical approach for propagation of Mean and Variance quantities. Moreover, MC methods also provide an important tool to computing the full distribution of transformed variables, which can be really useful for hypothesis testing, computation of confidence levels, and many other statistical applications.


% START-CREDIT
% source: uncertainty_propagation
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Sandra Verhagen and Lotfi Massarweh. {ref}`Find out more here <uncertainty_propagation_credit>`.
```
% END-CREDIT
