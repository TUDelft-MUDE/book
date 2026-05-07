# Univariate Continuous Distributions

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre, Robert Lanzafame, and Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT

This chapter contains the prerequisites for the [multivariate distributions chapter](../multivariate/overview.md) in the main part of the book. This chapter is not assessed on its own in the final exam, but the content is required for understanding the numerical methods chapter.

Civil engineering and the Geosciences involve working with nature which comes with unavoidable [uncertainties](uncertainty_classification). Natural phenomena have an intrinsic aleatoric uncertainty that we need to model, however, we don't always have the resources to take into account all possible scenarios. For example, it is impractical to design a system to protect against the largest imaginable flood, earthquake, chemical spill, climate change or sea level rise scenario. As a consequence, we often need to make decisions for uncertain conditions and data-scarce situations.

To this end, statistics and its key ingredient **probability** are indispensable. Continuous probability distributions, also known as *probability density functions* (PDFs) model this uncertainty explicitly, allowing us to quantify the probability associated with specific outcomes of our decisions, and to incorporate it rigorously in our decision-making.

To accomplish this, we first return to the fundamental concepts for describing probability for univariate continuous random variables and their distributions: the PDF and CDF. After using the **Gaussian** distribution to illustrate, the **empirical** distribution will be introduced. Observing that the Gaussian distribution cannot be used to model all uncertain random variables encountered science and engineering, we consider a wide range of **non-Gaussian** distributions, in particular those that can be described by relatively simple equations (i.e., **parametric** distributions), as well as a special form of parameterization used in Python (**location**, **shape** and **scale** used by `scipy.stats` Python module). We close by considering qualitative an quantitative approaches for modelling data with parametric distributions, including tools for verification and validation of the models: **Goodness of Fit** (GOF).
