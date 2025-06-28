## Introduction

From experience we know that various uncertain phenomena can be modeled as a random variable (or a random vector), say $Y$. In this part the random variables are measurements (e.g., sensor readings), which are uncertain due to random errors. We will refer to these random variables (our input data) $Y$ as the *observables*.

The unknown model parameters will be denoted as $\mathrm{x}$. The ingredients for this part on sensing and observation theory can then be summarized as follows:
* a model to describe the relation between observables $Y$ and parameters of interest $\mathrm{x}$
* estimation method(s) to estimate the parameters as function of $Y$: $\hat{X}=q(Y)$ (i.e., the estimation method defines the function $q$)
* uncertainty propagation to assess the precision of the estimated parameters $\hat{X}$
* hypothesis testing to account for errors in data and/or to choose best model from different candidates

```{admonition} Definition
The *functional model* describes the functional relationship between the observed variables (*observables*) and the unknown parameters. 

In case the functional relationship is linear, the functional model will have the form:

$$
\mathbb{E}(Y) = \mathrm{Ax}\quad \text{or} \quad Y=\mathrm{Ax}+\epsilon
$$

where $\mathrm{x}$ is a vector with the unknown model parameters, and $\mathrm{A}$ is referred to as the *design matrix*. $\mathbb{E}(.)$ is the expectation operator. The random errors are given by $\epsilon$ and are assumed to have zero mean: $\mathbb{E}(\epsilon)=0$.
```

A functional model can be mechanistic, phenomological or even data-driven, see the [Model classification section](modelclass).

:::{card} Exercise

Show that the two expressions for the functional model are indeed equivalent.

```{admonition} Solution
:class: tip, dropdown

$$
\mathbb{E}(Y)=\mathbb{E}(\mathrm{Ax+\epsilon})=\mathrm{Ax}+\mathbb{E}(\epsilon)=\mathrm{Ax}
$$

Recall that the unknown parameters are deterministic.
```
:::

Next, we will develop the principles and underlying theory of (1) Least-squares estimation, (2) Best linear unbiased estimation, and (3) Maximum likelihood estimation. 

Special attention is then given to how the uncertainty in the measurements propagates into parameter estimation results, such that we can assess the precision of the estimated parameters. For that purpose we need the stochastic model.

```{admonition} Definition
The *stochastic model* describes the uncertainty of the observables in the form of the covariance matrix $\Sigma_Y=\Sigma_{\epsilon}$.
```

This covariance matrix is assumed to be known here. In practice, it can be determined based on a calibration campaign: taking repeated measurements and calculate the empirical (co-)variances. Note that the uncertainty in the observations is fully attributed to the random errors, therefore we have that the covariance matrix of the observables is equal to that of the random errors.

:::{card} Quiz question
<iframe src="https://tudelft.h5p.com/content/1292060553773045247/embed" aria-label="Quiz_precision" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>
:::

Parameter estimation requires specification of the underlying functional and stochastic models. It may happen, however, that some parts of the models are misspecified, thereby invalidating the results of estimation. Some measurements, for instance, may be corrupted by blunders (which are not random!), or the chosen model may fail to give an adequate description of physical reality. Testing for such misspecifications is the topic of the last sections of this chapter.

(01_funcmodel)=
### Functional model: examples

#### Linear trend model 
The unknown parameters are the intercept $x_1$ and rate of change (velocity) $x_2$. The observation equation of a single observable $Y_i$ is:

$$
\mathbb{E}(Y_i)= x_1 + x_2 t_i
$$

where the observation times, or epochs, $t_i$ are assumed to be known and therefore deterministic.

The linear functional model for $m$ observables becomes:

$$
\mathbb{E}(\begin{bmatrix} Y_1 \\ Y_2 \\ \vdots \\ Y_m \end{bmatrix} )= \underset{\mathrm{A}}{\underbrace{\begin{bmatrix} 1 & t_1 \\ 1 & t_2  \\ \vdots & \vdots \\ 1 & t_m \end{bmatrix}}}\underset{\mathrm{x}}{\underbrace{\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}}}
$$

Examples where as a first guess the linear trend model could be applied (but might be too simplistic): subsidence due to gas extraction, uplift due to water injection, location on a line of a target with constant velocity, sea level rise of last 10 years.

:::{card} Exercise

What is the functional model if the observation equations are given by the quadratic function $\mathbb{E}(Y_i)= x_1 + x_2 t_i + x_3 t_i^2$. Is this a linear model?

```{admonition} Solution
:class: tip, dropdown

$$
\mathbb{E}(\begin{bmatrix} Y_1 \\ Y_2 \\ \vdots \\ Y_m \end{bmatrix} )= \underset{\mathrm{A}}{\underbrace{\begin{bmatrix} 1 & t_1 & t_1^2\\ 1 & t_2 & t_2^2 \\ \vdots & \vdots \\ 1 & t_m & t_m^2 \end{bmatrix}}}\underset{\mathrm{x}}{\underbrace{\begin{bmatrix} x_1 \\ x_2 \\x_3\end{bmatrix}}}
$$

This is model is linear in $\mathrm{x}$, therefore we refer to it as a linear model.
```
:::

#### Step function
Consider a process with unknown parameter $x_1$ assumed to be constant up till time $t_{i-1}$, and a sudden change (step) at time $t_i$, after which the parameter remains constant at $x_2$. See {numref}`stepfun`.

```{figure} https://files.mude.citg.tudelft.nl/00_step.png
---
height: 300px
name: stepfun
---
Observations with fitted step function.
```

The functional model can be written as:

$$
\mathbb{E}(\begin{bmatrix} Y_1 \\ \vdots \\ Y_{i-1} \\ Y_i \\ \vdots \\ Y_m \end{bmatrix} )= \underset{\mathrm{A}}{\underbrace{\begin{bmatrix} 1 & 0 \\ \vdots & \vdots \\ 1 & 0 \\ 0 & 1 \\ \vdots & \vdots \\ 0& 1 \end{bmatrix}}}\underset{\mathrm{x}}{\underbrace{\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}}}
$$

Such model may apply when considering deformation events in the subsurface, but can also be applicable in case of sensor replacement where one sensor has an offset with respect to the other (which would have to be calibrated).

:::{card} Exercise

The functional model of the step function can also be parameterized in terms of the initial value $x_1$ plus the step size $s=x_2-x_1$. Give the corresponding functional model.

```{admonition} Solution
:class: tip, dropdown

$$
\mathbb{E}(\begin{bmatrix} Y_1 \\ \vdots \\ Y_{i-1} \\ Y_i \\ \vdots \\ Y_m \end{bmatrix} )= \underset{\mathrm{A}}{\underbrace{\begin{bmatrix} 1 & 0 \\ \vdots & \vdots \\ 1 & 0 \\ 1 & 1 \\ \vdots & \vdots \\ 1& 1 \end{bmatrix}}}\underset{\mathrm{x}}{\underbrace{\begin{bmatrix} x_1 \\ s \end{bmatrix}}}
$$

```
:::

:::{card} Exercise
<iframe src="https://tudelft.h5p.com/content/1292060588665722877/embed" aria-label="Quiz_subduction" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>
:::

(positioning)=
#### Positioning model
As a final example we will consider a non-linear functional model for estimating the unknown position $\mathrm{x}=\begin{bmatrix} x, y, z\end{bmatrix}^T$ of a satellite. The observables are distance measured with laser ranging from $m$ ground stations at known positions $\begin{bmatrix} x_i, y_i, z_i\end{bmatrix}^T$.

```{figure} https://files.mude.citg.tudelft.nl/01_laser.png
---
height: 200px
name: LSfit
---
Positioning of satellite in orbit using laser ranging from multiple ground stations on knonw locations.
```

The functional model comprises $m$ non-linear functions of the unknown parameter vector $\mathrm{x}$:

$$
\mathbb{E}(\begin{bmatrix} Y_{1} \\ Y_{2} \\ \vdots \\ Y_{m} \end{bmatrix} )= \begin{bmatrix} \sqrt{(x_1-x)^2+(y_1-x)^2+(z_1-x)^2}\\ \sqrt{(x_2-x)^2+(y_2-x)^2+(z_2-x)^2} \\ \vdots \\ \sqrt{(x_m-x)^2+(y_m-x)^2+(z_m-x)^2}\end{bmatrix}
=\begin{bmatrix} q_{1}(\mathrm{x}) \\ q_{2}(\mathrm{x}) \\ \vdots \\ q_{m}(\mathrm{x}) \end{bmatrix}
$$

### Redundancy
Later we will see that the *redundancy* of our model plays an important role regarding the precision of our estimated parameters. For a model with $m$ observables and $n$ unknown parameters, the [redundancy](redundancy) is given by:

$$
\text{redundancy} = m-n
$$

this is true since we assume to work with $\mathrm{A}$-matrices (size $m\times n$) that have full column rank: $rank(\mathrm{A})=n$.

### Estimation and linear regression

The goal of estimation is the estimate *model parameters* from a set of observations. In Civil Engineering, Applied Earth Sciences and Environmental Engineering this is needed in many monitoring and sensing applications, such as:
* Sea level rise
* Land subsidence / uplift
* Air quality
* Settlement of soils 
* Tunnel deformation
* Bridge motions
* Traffic flow rates
* Water vapor content for numerical weather prediction
* Ground water level

In this part, we will introduce different estimation principles, starting with (weighted) least-squares. Next, Best Linear Unbiased estimation and Maximum Likelihood estimation will be introduced, providing the probabilistic framework  for estimating *model* parameters from *uncertain data*.

*Linear regression* aims to estimate the relationship between so-called *dependent* and *independent* variables, the latter also referred to as *predictors*, since once the relationship is known, these can be used to predict the behaviour of the dependent variables. Examples of bivariate regression model applications:
* predict *river run-off* (dependent variable) based on *amount of rainfall* (independent variable), see {numref}`Regres`
* predict *house prices* (dependent variable) based on their *energy label* (independent variable)
* predict *geothermal power production* (dependent variable) based on *brine temperature* (independent variable)
* predict *structural deformation* (dependent variable) based on *wind load* (independent variable)

Note that regression analysis is not restricted to linear nor to bivariate cases.

```{figure} https://files.mude.citg.tudelft.nl/01_Regression.png
---
height: 350px
name: Regres
---
Linear regression example for amount of rainfall (independent variable) and river runoff (dependent variable).
```

The estimation principles discussed in this part are needed for estimating these relationships.

Supervised machine learning (MUDE topic in Q2) is all about finding relationships between target (dependent) variables and certain features (predictors), and therefore regression analysis.
