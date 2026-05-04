
(Poisson)=
# Intermezzo: Poisson

As you already know, the [Binomial distribution](./Bernoulli.md) models the probability of $x$ successes in $n$ Bernoulli trials with a probability of success in each trial, $p$. When $n$ is large and $p$ is small, the Binomial distribution can be approximated by a Poisson distribution. Thus, the Poisson distribution is also based on the assumption of independence and identical distribution. 

```{admonition} MUDE exam information
:class: tip

In this section, theory regarding the Poisson distribution is provided as a refresher from previous courses. You are not required to know the derivation of the distribution and you will not have questions about the Poisson distribution in the exam. You need to understand how the Poisson process is used to model extremes and the assumptions you make when you apply this model. You might have questions about these points in the exam.

```

## Deriving the Distribution
Let's start with the pmf of a Binomial random variable.

$
p_X(x) = P[X=x|n, p] = \binom{n}{x}p^x(1-p)^{n-x}
$

Now, let $\lambda=np$ be the expected number of successes in a series of $n$ Bernoulli trials with probability $p$. 

$
p_X(x) = P[X=x|n, p] = \binom{n}{x}(\lambda/n)^x(1-\lambda/n)^{n-x}
$

$
= \frac{n(n-1)(n-2)...(n-x+1)}{n^x x!}\lambda^x(1-\lambda/n)^{n}(1-\lambda/n)^{-x}
$

If the number of trials is large, $n \rightarrow \infty$, and $x$ and $p$ are fixed and finite:

$
\lim_{n \to \infty}\frac{n(n-1)(n-2)...(n-x+1)}{n^x} = 1
$

$
\lim_{n \to \infty} (1-\lambda/n)^{-x} = 1
$

$
\lim_{n \to \infty} (1-\lambda/n)^{n} = e^{-\lambda} 
$

So, we can simplify it as

$
p_X(x) = P[X=x|n, p] = \frac{\lambda^x \ e^{-\lambda}}{x!} \hspace{1cm}  for \ x = 0, 1, 2, ... \ and \ \lambda > 0$

$
p_X(x) = P[X=x|p] = 0       \hspace{2cm}          otherwise
$

which is the **Poisson distribution**! Therefore, if $n \to \infty$ and $p$ is small so $\lambda = np$, the random variable $X$ is Poisson distributed with parameter $\lambda$. 

```{admonition} Binomial vs. Poisson distribution
:class: tip

Although both the Binomial and Poisson distribution are discrete distributions which measure the number of successes within a certain time block, Binomial is based on discrete events, while the Poisson is based on continuous events. That is, in Poisson distribution $n \to \infty$ and $p$ is very small, so you have an infinite number of trials with infinitesimal chance of success. In the Binomial distribution, the number of trials $n$ is finite. 
 ```

## Poisson distribution and Poisson process

If we integrate the pmf of the Poisson distribution, we can obtain its cdf defined as

$
F_X(x) = \sum_{k=0}^x \frac{\lambda^x e^{-\lambda}}{x!} \hspace{2.5cm}  for \ x = 0, 1, 2, ... \ and \ \lambda > 0$

Since Poisson distribution is derived by imposing that $E[X]=\lambda$, it is not a surprising property. However, the Poisson distribution also satisfied $E[X]=Var[X]=\lambda$.

```{admonition} Poisson-distributed variable
:class: tip

The conditions for a random variable to follow a Poisson distribution are:
 1. A series of Bernoulli trials is made with two possible outcomes: success or failure.
 2. There is a **small** constant probability of success, $p$.
 3. There is a **very large** number of trials, $n \to \infty$.
 4. The outcomes of the trials are independent.
 5. The random variable X is the total number of successes in $n$ trials and the order of the successes is irrelevant.

 It is also referred as the Poisson approximation to the Binomial.
```

A Poisson process is a particular form of a random process, where the average time between events is known, but the exact timing of events is random.

```{admonition} Poisson process criteria
:class: tip

The governing criteria for a Poisson process are:
 1. It is a Bernoulli process, so:

    a. There are only two possible outcomes which are mutually exclusive and collectively exhaustive: success vs. failure.

    b. There is a constant probability of success, $p$.

    c. Each trial is independent. That is, the result of the next trial does not depend on the previous one.

2. It is based on a continuous process (infinite number of trials, $n$)
3. The average number of events ($\lambda$) or average rate ($\nu = \lambda/t$, where $t$ is the length of the time block) is constant.
4. Two events cannot occur at the same time.

```

Under this Poisson process conditions, the Poisson distribution models the probability of a observing $x$ number of events in a fixed time block if these events occur with a known constant rate ($\nu$) and independently of the time since the last event.

## Poisson process to model extremes sampled with POT

Let's go back to our example on the design wave for a breakwater. Each hour within my register (each trial in $n \to \infty$), I have a value of $H_s$ which can be over (success) or below (failure) my threshold. Since I am interested in extreme observations (the tail of the distribution), the probability of being above my threshold ($p$) is very small. I am interested in the yearly probability of failure ($p_{f,y}$), so my time block is one year. If I count the number of excesses over my threshold (number of successes) each year, **that is a Poisson process**!

**And what is interesting about this?**

 It means that if I do my POT to sample extremes and I check if the number of extremes per year follow a Poisson distribution, I am ensuring that the sampled events are independent and, thus, my threshold and declustering time are appropriate. 

Almost all the techniques to formally select the threshold and declustering time for POT are based on the assumption that the sampled extremes should follow a Poisson distribution. You will see some of these techniques in further detail in the following sections.





% START-CREDIT
% source: extreme_value_analysis
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Patricia Mares Nasarre. {ref}`Find out more here <extreme_value_analysis_credit>`.
```
% END-CREDIT
