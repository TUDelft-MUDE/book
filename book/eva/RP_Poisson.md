
# Return Period & Design Life
In the previous sections, we have covered the process of how to perform EVA using POT sampling technique and GPD distribution. Also, Poisson distribution function and its relationship with EVA was introduced. Here, $RT$ will be again extended to cover the concepts related to the design life in the context of POT sampling technique and Poisson process.

As previously introduced, there are four key concepts to parameterize safety in the design phase:
- Probability of failure in one year ($p_{f,y}$).
- Return period ($RT$), usually given in years. According to the previous definition, $RT = 1/p_{f,y}$.
- Design life ($DL$): lifetime of the infrastructure.
- Probability of failure in the design life of the structure ($p_{f,DL}$).

We saw that the number of excesses per time block (typically a year) follows a Poisson distribution and can be used together with the GPD distribution to determine the yearly exceedance probabilities. However, **how can we obtain the exceedance probability along the design life?**

```{admonition} MUDE exam information
:class: tip

In this section, the derivation of the formula which relates the above mentioned parameters is presented based on the Poisson model. You are not required to know the derivation, it is shown as background information so you know the assumptions which are done in the process. You need to understand the concepts of yearly probability of failure, return period, design life and the probability of failure in the design life. Also, you need to be able to apply the derived equation.

```

## Deriving the probability of failure along the design life
We already saw that extremes could be assimilated as a Bernoulli process: for each year (trial), we check if the observed value exceeds our design value (success) or not (failure). Thus, the number of exceedances over a design value (successes) in an infinite number of years (trials) will follow the Poisson distribution if each trial is independent and the probability of success (exceeding the threshold) is very small.

Let's calculate the probability of observing an event $z_0$ higher than the design value $z_q$ at least once in $DL$ years ($p_{f,DL}$). 

First, we calculate the probability of not failing along $DL$ applying the Poisson distribution. Remember that $\lambda = np$, being $n$ the number of trials and $p$ the probability of success.

$
p_X(0) = P[X=0|DL, p_{f,y}] = \frac{\lambda^0 \ e^{-\lambda}}{0!} = e^{-DL \times p_{f,y}}
$

The probability of failing at least once in $DL$ can be computed as $1 - p_X(0)$ (1 - no failure), so

$
p_{f,DL} = 1 - p_X(0) = 1 - e^{-DL \times p_{f,y}}
$

We defined $RT = 1/p_{f,y}$, so

$
p_{f,DL} = 1 - e^{-DL/RT} = 1 - e^{-DL/RT}
$

Rewriting it in terms of $RT$, we obtain

$
RT = \frac{-DL}{ln(1-p_{f,DL})}
$

And now you can compute the design $RT$ based on the $DL$ and $p_{f,DL}$ recommended in design guidelines!

## Let's practice!

An scientist is designing a *thingamajig*. According to the recommendations, any *thingamajig* should be designed for a lifespan of 25 years with a probability of failure along the design life of $p_{f,DL}=0.05$.

What is the design return period using the [Binomial model](Bernoulli)?

```{admonition} Answer
:class: tip, dropdown

Applying the expression for the return period derived applying a Binomial distribution

$RT = 1/p_{f,y} = \frac{1}{1 - (1 - p_{f,DL})^{1/DL}} = \frac{1}{1 - (1 - 0.05)^{1/25}} \approx 487.7$ years

```

What is the design return period using the Poisson model?

```{admonition} Answer
:class: tip, dropdown

Applying the expression for the return period derived applying a Poisson distribution

$RT = 1/p_{f,y} = \frac{-DL}{ln(1-p_{f,DL})} = \frac{-25}{ln(1-0.05)} \approx 487.4$ years

```

Is there a significant difference between both approaches?

```{admonition} Answer
:class: tip, dropdown

In terms of the computed return periods ($RT$), there is not a significant difference. Although Poisson model is formally more correct since it assumes an infinite number of trials, both models can be applied.

```


% START-CREDIT
% source: extreme_value_analysis
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Patricia Mares Nasarre. {ref}`Find out more here <extreme_value_analysis_credit>`.
```
% END-CREDIT
