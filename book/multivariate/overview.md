
(mulitivar)=
# Multivariate Distributions

Challenges in all branches of science and engineering involve working in situations where uncertainty plays a significant role: prior chapters of this book focused a lot on _error_, but often we must also deal with data scarce scenarios (often categorized as _epistemic_ uncertainty) and natural phenomena with a significant _stochastic_ nature (often categorized as _aleatoric_ uncertainty). As seen in the previous chapter, univariate continuous distributions can assist us in modelling uncertainty associated with a specific variable in order to quantitatively account for uncertainty in general; the distribution helps inform the decision-making process or risk analysis. However, our problems of interest are typically complex and usually involve more than one variable: a _multivariate_ situation.

Consider, for example, when assessing algae blooms in a water body (e.g., a freshwater lake), different variables must be considered, such as nutrients in the water (nitrogen and phosphorus) and their concentration, dissolved oxygen and temperature of the water body. Sometimes (although not frequently), these variables are not related to each other, so we can consider them _independent._ For example, one may assume (for simplicity) that the amount of nitrogen and phosphorous that reaches the lake is not be related to the water temperature of the lake. However, truly _independent_ situations rarely occur in reality, and the variables are _dependent_ on each other. For example, the concentration of nitrogen and phosphorous changes with time and the reaction rates are dependent on the temperature of the water; thus if you are interested in these quantities over time, temperature is certainly a _dependent variable_ of interest.

Although dependent relationships can often be quantified using deterministic relationships (e.g., mechanistic or phenomenological models), probability distributions are also capable of capturing this behavior. This is where _multivariate probability distributions_ are helpful, as they allow us to model the distribution of not only one variable but several at the same time, thus accounting for their dependence.

**Revisiting correlation**

Probabilistic dependence between random variables is usually quantified through correlation coefficients. Previous, you have already been introduced to the concept of [correlation](correl) and Pearson correlation coefficient, which is given by

$$ 
\rho(X_1,X_2)=\frac{Cov(X_1,X_2)}{\sigma_{X_1} \sigma_{X_2}} 
$$ 

where $X_1$ and $X_2$ are random variables, $Cov(X_1,X_2)$ is their covariance, and $\sigma_{X_1}$ and $\sigma_{X_2}$ are the standard deviations of $X_1$ and $X_2$. $-1 \leq \rho(X_1,X_2) \leq 1$, being $\rho(X_1,X_2)=-1$ a perfect negative linear correlation, and $\rho(X_1,X_2)=1$ a perfect positive linear correlation. If $X_1$ and $X_2$ are independent, then $\rho(X_1,X_2) \to 0$[^note]. This is, that having information about $X_1$ does not provide us with information about $X_2$. The interactive element below allows you to play around with the correlation value yourself. Observe how the distribution's _density_ contours, or a scatter plot of _samples,_ change when you adjust the correlation.

<iframe src="../_static/elements/element_correlation.html" width="600" height="400" frameborder="0"></iframe>

**Overview of this Chapter**

Our ultimate goal is to construct and validate a model to quantify probability for combinations of more than one random variable of interest (i.e., to quantify various types of uncertainty). Specifically, 

$$
f_X(x) \;\; \textrm{and} \;\; F_X(x)
$$

where $X$ is a vector of continuous random variables and $f$ and $F$ are the multivariate probability density function (PDF) and cumulative distribution functions (CDF), respectively. Often we will use _bivariate_ situations (two random variables) to illustrate key concepts, for example:

$$
f_{X_1,X_2}(x_1,x_2) \;\; \textrm{and} \;\; F_{X_1,X_2}(x_1,x_2)
$$

This chapter begins with a refresher on some fundamental aspects of probability theory that are typically covered in BSc courses on the subject, for example, dependence/independence, probability of binary events and conditional probability. Using the _bivariate_ case, we will build a foundation on which to apply the multivariate Gaussian distribution (introduced in earlier chapters), as well as introduce alternative _multivariate distributions._ The theoretical part of the chapter ends with a brief introduction to _copulas_ as a straightforward approach for evaluating two random variables that are dependent _and_ described by non-Gaussian marginal distributions (the previous chapter). The last section revisits functions of random variables and takes an applied perspective by putting the univariate and multivariate probability concepts in a simple case study (design of a flood protection system).

[^note]: That is an intuitive definition of independence. For a more formal definition of independence, visit the next page of the chapter.