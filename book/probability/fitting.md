
# Fitting a Distribution

In the previous sections, we introduced parametric distributions as mathematical models for the empirical distribution functions of observations. Also, some of the most widely used parametric distributions were presented, such as Exponential or Normal distribution. Those parametric distributions had some parameters which required to be fitted to the observations. For instance, Exponential distribution has a rate parameter ($\lambda$). In this section, the most commonly used methods to fit the parametric distribution functions are first presented.

- Method of moments
- Maximum loglikelihood estimator (MLE)

Note that it assumes that we know the parametric distribution we want to fit. For instance, fitting an Exponential distribution to a sample of observations. So, how do I choose between them? The choice of the appropriate distribution function needs to be based first on the physics of the random variable we are studying. Once we have accounted for those physical characteristics, we can make use of goodness of fit (GOF) techniques to support our decision. In the subsequent sections, some commonly used GOF techniques in the statistics field are also presented.

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre and Robert Lanzafame. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT