
# Parametric Distributions

In the previous sections, you were introduced to the concepts of random variable, probability density function (PDF) and cumulative distribution function (CDF) and how to compute them using empirical data. We also revisited the Gaussian distribution. Here, the concept of **parametric** distribution as a model of the observed empirical distribution is introduced, where we focus in particular on models that are both commonly used and have a relatively straightforward PDF and/or CDF to study analytically (i.e., with equations, not only pre-existing computer code!).

Parametric distribution functions are mathematical models for the empirical distributions that we observe in our data. In the preceding section, we have seen how we can derive an empirical PDF and CDF from data. As we continue to collect data, we can reduce the width of our histogram bins even further until our bins become infinitesimally thin, and we switch from discrete interval probabilities to **probability densities**. 

You may have noticed already that the height of these histogram bins, and their corresponding interval probabilities, often tend to vary smoothly over $x$. A parametric pdf seeks to identify these variations and defines a function that describes them. Likewise, a parametric CDF is just an equation which relates the non-exceedance probability with the value of the studied random variable. This equation has some parameters or coefficients that need to be fitted using our observations. 

**But why do we need parametric distributions?** 

We typically fit a parametric distribution to our data for several reasons. The most important one is that the empirical distribution is limited to the observations we have. Using the empirical CDF, we can interpolate between the observed values, but we cannot extend it further and infer probabilities higher or lower than those we have observed. 

Another good reason to fit a parametric distribution is more on the practical side: an equation allows us to use all the power of analytic solutions and it is very easy to transfer and handle. Also, we can make use of the properties of the fitted distribution to have a further insight on the random variable we are studying.

In the following sections, you will be introduced to some of the most commonly used distributions in engineering and geosciences and their properties. 

```{admonition} MUDE exam information
:class: tip, dropdown
You do not need to know the equations of the distribution functions by heart. You just need to know how the distribution looks (PDF/CDF), how it responds to changes in the parameters, and some basic properties (symmetry or bounds).
```

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre, Robert Lanzafame, and Maximilian Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT