
# Exponential distribution: let's practice

An engineer is the manager of the construction of a bridge across a river and is concerned about large floods (floods with discharges higher than $50 m^3/s$) in the river, since they may damage the construction works. Higher floods than that occur in average every 10 years.

Assume that floods are independent and identically distributed. This means that they can be modelled using a Poisson process and, thus, the time between floods can be modelled using an Exponential distribution.


What is the rate ($\lambda$) of the Exponential distribution?


```{admonition} Answer
:class: tip, dropdown

The rate ($\lambda$) represents the frequency which is the inverse of the average waiting time. Therefore:

$$
   \lambda = 1/10 = 0.1
$$

```


The construction time is planned to be 2 years. Under the previous hypothesis, what is the probability of not observing a flood in those 2 years?


```{admonition} Answer
:class: tip, dropdown

The probability of not observing a flood in two years can be computed as the probability of the waiting time between floods being higher than 2 years. Therefore:

$$
   P[X>2] = 1 - F(x) = 1 - (1 - e^{-0.1 \cdot 2}) = e^{-0.1 \cdot 2} \approx 0.82
$$

This means that there is a probability of observing a flood of 1 - 0.82 = 0.18, which is actually pretty high! Maybe the engineer should think about a tighter schedule or using some adaptive techniques so the construction works are not affected by events that low.

```

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre and Robert Lanzafame. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT