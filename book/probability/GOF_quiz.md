
# Goodness of fit: let's practice

An engineer is characterizing the axle loads transmited by the traffic on a bridge. Based on the observations, a Normal and a Gumbel distributions are fitted, as shown in the figure below. 

```{figure} /probability/figures/GOF_ex.png

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
