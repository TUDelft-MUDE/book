(machine_learning)=
# Introduction to Machine Learning

% START-CREDIT
% source: machine_learning
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Iuri Rocha, Anne Poot, Joep Storm and Leon Riccius. {ref}`Find out more here <machine_learning_credit>`.
```
% END-CREDIT

_Machine learning_ is a set of techniques that uses computer algorithms to fit the parameters of a model. In the context of MUDE, it is a set of data-driven modelling techniques, closely related to the methods used in observation theory. However, whereas in observation theory we constructed the design matrix ourselves, based on some physics-based knowledge of the system of interest, in machine learning applications, we allow the algorithm more freedom to build (and refine) the model. Although this comes at the cost of less control over model parameters (the "unknowns" from observation theory) and increased complexity, the benefit is a more flexible model that is capable of capturing key characteristics of the problem at hand. For example, a neural network can be defined using thousands of weights (model parameters); far more than we can create with more "hands-on" techniques!

The problem we would like to solve:

- Given: Some complex process $p(x,t)$, usually highly nonlinear
- Goal: Construct a model $y(x)$ that explains it
- In practice: We do not know $p(x,t)$, but only have $N$ observations of it

Typically, these techniques are well-suited to applications that have large data sets, which is required to fit many parameters. As such, the resulting model is generally better suited to _interpolation_, rather than _extrapolation._ In other words: better to use the model to evaluate situations "between" the data, rather than "outside" them.


The field of _machine learning_ is multidisciplinary, which means it comes with a new set of terms and conceptual perspectives. Some examples are provided here:

- The observations of the process (i.e., the "answer") is often called the _target_
- The process of fitting a model to data (i.e., computing the model parameters) is called _training_ the model
- Rather than simply fit a model to data and validate it (e.g., by computing and evaluating the residuals), it is standard practice to withhold a portion of the data set and use it to validate the model _after_ the parameters have been computed. The concept of model _validation_ itself is unchanged.
- When the data is partitioned into two sets for model validation, the set used to find the model parameters is referred to as the _training_ set, whereas the remainder is the _validation_ set.
- As the optimization of model parameters can computationally expensive for large data sets, incorporating iterative cycles during the _training_ process can significantly improve the model and modelling process. This is referred to as _tuning_ the model.
- It is common practice to create a _third_ partition of the original data that can be used during the _tuning_ process; this is referred to as the _test_ set.
- Parameters that are used to control the model _training_ process, and related characteristics of the model, are called _hyperparameters._ For example, the $k$ in the k-Nearest neighbors approach. These parameters are often what is found during the _validation_ process, and can be improved during the _tuning_ process.
- _Loss_ is a term used for quantitative measures of model error. Although the mathematical definition will change for various model approaches and, also, when it is used in different phases of the modelling process (train, validate, test), the general use of _loss_ as a measure of error remains unchanged.

**Contents**

The story in this set of chapters is told through videos, along with interactive pages to work with the methods directly.

Contents:

- Decision theory for regression, k-Nearest Neighbors estimator
- Linear regression with nonlinear basis functions
- Introduction to neural networks for regression

By the end of this series, you will be able to:

- Understand and compare different approaches for regression modeling
- Construct parsimonious regression models for general applications
- Critically assess model performance from a probabilistic standpoint