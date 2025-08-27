# Notation and formulas

```{admonition} MUDE exam information
:class: tip, dropdown
This overview with Notation and Formulas will be given on the MUDE exam.
```

```{list-table}
:header-rows: 1

* - Description
  - Notation / formula
* - Observables (random)
  - $Y=\begin{bmatrix} Y_1,Y_2,\ldots, Y_m \end{bmatrix}^T$
* - Observations (realization of $Y$)
  - $\mathrm{y}=\begin{bmatrix} y_1,y_2,\ldots, y_m \end{bmatrix}^T$
* - Unknown parameters (deterministic)
  - $\mathrm{x}=\begin{bmatrix} x_1,x_2,\ldots, x_n \end{bmatrix}^T$
* - Random errors
  - $\epsilon = \begin{bmatrix} \epsilon_1,\epsilon_2,\ldots, \epsilon_m \end{bmatrix}^T$ with $\epsilon\sim N(0,\Sigma_{\epsilon})$
* - Functional model (linear)
  - $\mathbb{E}(Y) = \mathrm{A} \mathrm{x}\;$  or  $\;Y = \mathrm{A} \mathrm{x} + \epsilon$
* - Stochastic model
  - $\mathbb{D}(Y) = \Sigma_{Y}=\Sigma_{\epsilon}$
* - Estimator of $\mathrm{x}$ 
  - $\hat{X}$ 
* - Estimate of $\mathrm{x}$ (realization of $\hat{X}$) 
   - $\hat{\mathrm{x}}$
* - Adjusted (or predicted) observations 
  - $\hat{\mathrm{y}}=\mathrm{A}\hat{\mathrm{x}}$
* - Residuals 
  - $\hat{\epsilon}=\mathrm{y}-\mathrm{A}\hat{\mathrm{x}}$
```

## Estimators of $\mathrm{x}$
```{list-table}
:header-rows: 1

* - Estimators
  - Formula
* - Least-squares (LS) 
  - $\hat{X}=\left(\mathrm{A}^T \mathrm{A} \right)^{-1} \mathrm{A}^T Y $
* - Weighted least-squares (WLS)
  - $\hat{X}=\left(\mathrm{A}^T\mathrm{WA} \right)^{-1} \mathrm{A}^T\mathrm{W} Y $
* - Best linear unbiased (BLU) 
  - $\hat{X}=\left(\mathrm{A}^T\Sigma_Y^{-1} \mathrm{A} \right)^{-1} \mathrm{A}^T\Sigma_Y^{-1} Y $
```

## Test statistics (with distribution under $\mathcal{H}_0$)
```{list-table}
:header-rows: 1

* - Test statistic
  - Formula
* - Generalized likelihood ratio test 
  - $T_q = \hat{\epsilon}^T\Sigma_Y^{-1}\hat{\epsilon}-\hat{\epsilon}_a^T\Sigma_Y^{-1}\hat{\epsilon}_a\sim \chi^2(q,0)$
* - Overall model test 
  - $T_{q=m-n} = \hat{\epsilon}^T\Sigma_Y^{-1}\hat{\epsilon}\sim \chi^2(q,0)$
* - w-test 
  - $W = \frac{\mathrm{C}^T\Sigma_Y^{-1} \hat{\epsilon}}{\sqrt{\mathrm{C}^T\Sigma_Y^{-1}\Sigma_{\hat{\epsilon}}\Sigma_Y^{-1} \mathrm{C}}} \sim N(0,1)$
```

(99_proplaw)= 
## Linear propagation laws if $\hat{X}=\mathrm{L^T} Y $
```{list-table}
:header-rows: 1

* - Propagation law of the ...
  - Formula
* - ... mean 
  -  $\mathbb{E}(\hat{X}) = \mathrm{L^T}\mathbb{E}(Y)$ 
* - ... covariance matrix 
  - $\Sigma_{\hat{X}} =\mathrm{L^T}\Sigma_Y \mathrm{L} $ 
```

% START-CREDIT
% source: observation_theory
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Sandra Verhagen. {ref}`Find out more here <observation_theory_credit>`.
```
% END-CREDIT