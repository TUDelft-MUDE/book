
# Fitting a Distribution

In the previous sections, we introduced parametric distributions as mathematical models for the empirical distribution functions of data. We discussed some of the most widely used univariate parametric distributions, such as Exponential or Normal distribution. Those parametric distributions each have some parameters which must be fitted to the data. For instance, the Exponential distribution has a rate parameter ($\lambda$), and the Gaussian distribution has a mean ($\mu$) and a standard deviation ($\sigma$). In this section, we will discuss the most commonly used methods to fit a parametric distribution function to data:

- Method of moments
- Maximum loglikelihood estimator (MLE)

Note that we have to decide in advance which parametric distribution we want to fit. This raises the question: How we can choose an appropriate parametric distribution? The choice of the distribution function has to be based first and foremost on the properties of the random variable we are studying: is it physically viable for the random variable to take on negative values? How do the tails of the distribution look like? To answer these questions, it can often be useful to study the empirical distributions, as we discussed in the previous sections. Once we have accounted for those physical characteristics, and chosen an appropriate distribution, we can make use of **goodness of fit** (GOF) techniques to support our decision. In the subsequent sections, some commonly used GOF techniques in the statistics field are also presented.

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Maximilian Ramgraber, Patricia Mares Nasarre, and Robert Lanzafame. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT