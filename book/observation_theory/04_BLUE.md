(BLUE)=
# Best linear unbiased estimation

Best Linear Unbiased estimation (BLUE) is based on a fundamentally different  principle than (weighted) least-squares (WLS), but still it turns out to be a special case of WLS.

Comparing the weighted least-squares estimator:

$$ 
\hat{X}_{\text{WLS}}= \mathrm{(\mathrm{A^T} W \mathrm{A})^{-1} \mathrm{A^T} W} Y
$$

with the estimator of the vector of unknowns following from BLUE:

$$
\hat{X}_{\text{BLU}}= (\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1} \mathrm{A^T} \Sigma_Y^{-1} Y
$$

We see that the weight matrix $\mathrm{W}$ is now replaced by the inverse of the covariance matrix $\Sigma_Y$ (our stochastic model). 

This makes sense intuitively: suppose the observables are all independent and thus uncorrelated, such that the covariance matrix is a diagonal matrix with the variances as its diagonal element. The weights for the individual observables are then equal to the inverse of their variances, which implies that a more precise observable (smaller variance) receives a larger weight.

Taking this particular weight matrix, i.e., $\mathrm{W}=\Sigma_Y^{-1}$, has a special meaning. It has the “Best” property. This means that using this particular weight matrix, we obtain a linear unbiased estimator which has minimal variance. In other words, with this particular weight matrix we get the best possible estimator among all linear unbiased estimators, where ‘best’ represents optimal precision or minimal variance.

Given the BLU-estimator for $\hat{X}$, we can also find the BLU-estimators for $\hat{Y} =\mathrm{A}\hat{X}$,and for $\hat{\epsilon} =  Y-\hat{Y} $,

$$
\hat{Y}= \mathrm{A}(\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1} \mathrm{A^T} \Sigma_Y^{-1} Y
$$

$$
\hat{\epsilon}= Y-\mathrm{A}(\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1} \mathrm{A^T} \Sigma_Y^{-1} Y
$$

:::{card} Exercise stochastic model

<iframe src="https://tudelft.h5p.com/content/1292061604348573907/embed" aria-label="quiz_stochastic_model2" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>

:::

:::{card} Exercise least-squares versus BLUE

Let's consider an estimation problem with $m$ observables and functional model $\mathbb{E}(Y)=\mathrm{Ax}$ and stochastic model $\Sigma_Y = \sigma^2 I_m$ (i.e., the covariance matrix is a scaled identity matrix). 

Find the expressions for the ordinary (unweighted) least-squares estimator and the best linear unbiased estimator.

**True or False:** The ordinary least-squares and best linear unbiased estimator are equal to each other if $\Sigma_Y$ is a scaled identity matrix?

```{admonition} Solution
:class: tip, dropdown

True:

$$
\hat{X}_{\text{BLU}}= (\mathrm{A^T} \frac{1}{\sigma^2}I_m\mathrm{A})^{-1} \mathrm{A^T} \frac{1}{\sigma^2}I_m Y = (\mathrm{A^T}  \mathrm{A})^{-1} \mathrm{A^T} Y = \hat{X}_{\text{LS}}
$$

```
:::

### Video

```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/EIZvJrlxZhs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

### BLUE decomposed

In BLUE, Best Linear Unbiased Estimation, the parts of the acronym ‘B’, ‘L’, and ‘U’ refer to specific properties.

*Linear* means that there is a linear (matrix) relation between the variables. Such linear relations imply that if we have a normally distributed vector $Y\sim N(\mathrm{Ax},\Sigma_Y)$, which is multiplied with a matrix $\mathrm{L}$, this product will be normally distributed as well:

$$
\hat{X}=\mathrm{L^T}Y\sim N(\mathrm{L^T Ax},\mathrm{L^T} \Sigma_Y \mathrm{L})
$$ 

where we use the linear propagation laws of the mean and covariance.

*Unbiased* means that the expected value of an estimator of a parameter is equal to the value of that parameter. In other words: 

$$
\mathbb{E}(\hat{X})= \mathrm{x}.
$$

The unbiased property also implies that:

$$
\begin{align*}\mathbb{E}(\hat{Y} ) &=\mathrm{A} \mathbb{E}(\hat{X} )=\mathrm{Ax} \\ \mathbb{E}(\hat{\epsilon} )  &= \mathbb{E}(Y)-\mathbb{E}(\hat{Y})= \mathrm{Ax-Ax}= 0 \end{align*}
$$

*Best* means that the estimator has minimum variance (best precision), when compared to all other possible linear estimators:

$$
\text{trace}(\Sigma_{\hat{X}}) = \sum_{i=1}^m \sigma^2_{\hat{X}_i} = \text{minimum}
$$


(Note that this is equivalent to "minimum mean squared errors" $\mathbb{E}(\|\hat{X}-\mathrm{x}\|^2)$. )

(04_cov)=
### Covariance matrices of the BLU estimators

The precision of the estimator is expressed by its covariance matrix. For the ‘best linear unbiased’ estimator of $\hat{X}$, $\hat{Y}$  and $\hat{\epsilon}$ we obtain (by applying the [linear covariance propagation laws](99_proplaw)):

$$
\begin{align*}
\Sigma_{\hat{X}} &= \mathrm{L^T} \Sigma_Y \mathrm{L} \\ &= (\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1}\mathrm{A^T} \Sigma_Y^{-1} \cdot \Sigma_Y \cdot \Sigma_Y^{-1} \mathrm{A} (\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1}\\ &=(\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1}\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A} (\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1}\\ &= (\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1}\\ \\ \Sigma_{\hat{Y}} &=\mathrm{A}\Sigma_{\hat{X}} \mathrm{A^T} \\ &=\mathrm{A} (\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1} \mathrm{A^T} \\ \\
\Sigma_{\hat{\epsilon}} &= (\mathrm{I}_m - \mathrm{A} (\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1}\mathrm{A^T} \Sigma_Y^{-1}) \cdot \Sigma_Y \cdot (\mathrm{I}_m - \mathrm{A} (\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1}\mathrm{A^T} \Sigma_Y^{-1})^T \\ &= (\Sigma_Y - \mathrm{A}(\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1}\mathrm{A^T}) (\mathrm{I}_m -\Sigma_Y^{-1}\mathrm{A} (\mathrm{A^T} \Sigma_Y^{-1} \mathrm{A})^{-1}\mathrm{A^T})\\ &= \Sigma_Y - \Sigma_{\hat{Y}}-\Sigma_{\hat{Y}}+\Sigma_{\hat{Y}}\\ &= \Sigma_Y - \Sigma_{\hat{Y}}\end{align*}
$$

In summary, by applying the BLUE method, we obtain the best estimator among all linear unbiased estimators, where ‘best’ is quantitatively expressed via the covariance matrix.

### Additional note on the linearity condition of BLUE 

The BLUE estimator is the best (or minimum variance) among all linear unbiased estimators. However, if we drop the condition of linearity, then BLUE is not necessarily the best.  It means that there may be non-linear estimators that have even better precision than the BLUE. However, it can be proven that, in the case of normally distributed observations, the BLUE is also the best among all possible unbiased estimators. So we can say: for observations $Y$ that are normally distributed, the BLUE is BUE (best unbiased estimator). 

:::{card} Exercises

<iframe src="https://tudelft.h5p.com/content/1292062185757789447/embed" aria-label="quiz-RoC_glacier" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>

:::

% START-CREDIT
% source: observation_theory
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Sandra Verhagen. {ref}`Find out more here <observation_theory_credit>`.
```
% END-CREDIT