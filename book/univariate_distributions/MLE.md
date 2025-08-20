# Maximum Likelihood Estimation

*Maximum Likelihood Estimation* (MLE) is a statistical method used to estimate the parameters of a probability distribution based on observed data $\mathbf{x} = x_1, x_2, ..., x_n$. Evaluating the joint density of the data given a parametric family $\theta$ gives the likelihood function, which is a function that measures how well the observed data fits the probability distribution with the given parameters:

$$
L(\theta \mid \mathbf{x}) = f(\mathbf{x} \mid \theta) = \prod_{i=1}^{n} f(x_i \mid \theta)
$$ 

Since the likelihood is computed from a product of the PDF evaluations for each data point, a PDF $f$ that maximizes the likelihood is one that 
1) has high densites around regions where many samples $x_i$ cluster, but at the same time
2) has low but *non-zero* densities where few samples cluster. ince we take a product, a single zero-likelihood sample ($f(x_i \mid \theta) = 0$) can zero out the entire likelihood ($L(\theta \mid \mathbf{x})$).

The goal of MLE is consequently to find the values of the parameters for our chosen PDF $f$ that maximize ths likelihood function. The maximum likelihood estimate $\hat{\theta}$ is the set of parameters for which the observed data is the most probable with the assumed probability distribution:

$$
\hat{\theta} = \arg \max _{\theta} L(\theta \mid \mathbf{x})
$$ 

In practice, taking a product of many entries can quickly lead to numerical underflow issues. In consequence, it is more common to use the log-likelihood, which is the natural logarithm of the likelihood function:

$$
\ln (L(\theta \mid \mathbf{x})) = \ln (\prod_{i=1}^{n} f(x_i \mid \theta)) = \sum{i=1}^{n} \ln f(x_i \mid \theta),
$$ 

where the product becomes a sum. To find the maximum likelihood estimate $\hat{\theta}$, the following steps should be taken:

1. Define the likelihood function $L(\theta \mid \mathbf{x})$.
2. Take natural logarithm of the likelihood function to get the log-likelihood function $\ln (L(\theta \mid \mathbf{x}))$.
3. Differentiate the log-likelihood function and set it to zero: $\cfrac{\partial L(\theta \mid \mathbf{x})}{\partial \theta} = 0$.
4. Solve the equation for $\hat{\theta}$.

Note that the maximum can also occur at the boundary of the domain.

## Let's see it with an example!

The following dataset describes the time elapsed between consecutive arrivals of passengers at a bus stop (in minutes):

$$
\mathbf{x} = [1.2, 0.5, 3.7, 2.3, 0.9, 1.5, 2.1, 3.0, 1.8, 2.5]
$$

Assume that the observations can be described by the exponential distribution, for which the PDF is given by

$$
f(x, \lambda) = \lambda e^{\normalsize-\lambda x} \text{ for } x>0
$$

with $\lambda$ being the parameter that has to be estimated. There dataset consists of $n$ observations. Find the maximum likelihood estimate $\hat{\lambda}$ following the four steps defined above:

1. Define the likelihood function $L(\lambda \mid \mathbf{x})$.
2. Take natural logarithm of the likelihood function to get the log-likelihood function $\ln (L(\lambda \mid \mathbf{x}))$.
3. Differentiate the log-likelihood function and set it to zero: $\cfrac{\partial \ln L(\lambda \mid \mathbf{x})}{\partial \lambda} = 0$.
4. Solve the equation for $\hat{\lambda}$.

**1. Define the likelihood function $L(\lambda \mid \mathbf{x})$.**

According to the definition, the likelihood function is given by:

$$
L(\lambda \mid \mathbf{x}) = \prod_{i=1}^{n} f(x_i \mid \lambda)
$$

For the exponential distribution, $f(x_i \mid \lambda) = \lambda e^{\normalsize -\lambda x}$.

Therefore, the likelihood function for the exponential distribution is given by:

$$
L(\lambda \mid \mathbf{x}) = \prod_{i=1}^{n} \lambda e^{\normalsize -\lambda x_i} = \lambda^{\normalsize n} e^{\normalsize -\lambda \sum_{i=1}^{n} x_i}
$$

**2. Take natural logarithm of the likelihood function to get the log-likelihood function $\ln (L(\lambda \mid \mathbf{x}))$.**

Taking the natural logarithm of the likelihood function to obtain the log-likelihood function:

$$
\ln (L(\theta \mid \mathbf{x})) = \ln (\lambda^{\normalsize n} e^{\normalsize -\lambda \sum_{i=1}^{n} x_i} ) = n \ln (\lambda) -\lambda \sum_{i=1}^{n} x_i
$$

**3. Differentiate the log-likelihood function and set it to zero: $\cfrac{\partial \ln L(\lambda \mid \mathbf{x})}{\partial \lambda} = 0$**

Taking the derivative of the log-likelihood function with respect to $\lambda$ and setting it to zero:

$$
c\frac{\partial \ln (L(\lambda \mid \mathbf{x}))}{\partial \lambda} = \cfrac{\partial (n \ln (\lambda) -\lambda \sum_{i=1}^{n} x_i )}{\partial \lambda} = \cfrac{n}{\hat \lambda} - \sum_{i=1}^{n} x_i = 0
$$

**4. Solve the equation for $\hat{\lambda}$.**

We have the following equation to solve:

$\cfrac{n}{\hat \lambda} - \sum_{i=1}^{n} x_i = 0$

which results in the maximum likelihood estimate:

$$
\hat \lambda = \cfrac{n}{\sum_{i=1}^{n} x_i} = \cfrac{1}{\bar x}
$$

where $\bar x = \cfrac{\sum_{i=1}^{n} x_i}{n}$ is the sample mean of the obsrved data.

This means that the maximum likelihood estimate of the exponential distribution is the inverse of the sample mean. Therefore:

$$
\hat \lambda = \cfrac{n}{\sum_{i=1}^{n} x_i} = \cfrac{10}{19.5}=0.513
$$

The best fitting parameter of the Exponential distribution for the given data according to MLE is $\lambda = 0.513$.

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Maximilian Ramgraber, Patricia Mares Nasarre, and Robert Lanzafame. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT