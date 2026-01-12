(Bernoulli)=
# Bernoulli and Binomial

> Bernoulli processes and the Binomial distribution: why is this relevant?

Extreme value analysis and the study of extremes has a foundational basis in the theory of Bernoulli processes and the Bernoulli and Binomial distributions.

```{admonition} MUDE exam information
:class: tip

In this section, a refresher about Bernoulli processes and Binomial distribution is provided. You will not have questions in the exam about them and you don't need to know the presented derivations. You need to know how Bernoulli processes and Binomial distribution are applied to model extremes and the assumptions which are made for that.

```

## Bernoulli trials and Bernoulli process: do I need to study for my probability exam?

One student wants to know if she will pass her favourite course (of course, probability) without studying. Thus, she has the simplest possible experiment: one trial with two possible outcomes, pass (success!) and not pass (usually called failure). Note that they are mutually exclusive (if you pass, you haven't failed) and collectively exhaustive (there's no third possible outcome from the experiment). The results from such a trial are a two-sided Bernoulli random variable and, thus, the distribution of probabilities of the two outcomes is a Bernoulli distribution. The **Bernoulli distribution** is a discrete distribution function whose probability mass function (pmf) is given by

$
p_X(x) = P[X=x|p] = p^x(1-p)^{1-x}  \hspace{1cm}  for \ x = 0 \ or \ 1 \ and \ p \in [0,1]$

$
p_X(x) = P[X=x|p] = 0       \hspace{2.7cm}          otherwise
$

where $p$ is the probability of success ($x = 1$), and $x = 0 \ and \ 1$ are the possible outcomes. This is, $p(success)=p$.

Imagine that the student is not studying and wants to leave it to chance. She would have to take the course several times (several trials) and since she is not studying between trials, each trial would be independent (she is not learning from previous experiences). This will constitute what it's called a **Bernoulli process**.

```{admonition} Bernoulli process criteria
:class: tip

The governing criteria for a Bernoulli process are:
 1. There are only two possible outcomes which are mutually exclusive and collectively exhaustive: success vs. failure.
 2. There is a constant probability of success, $p$.
 3. Each trial is independent. That is, the result of the next trial does not depend on the previous one.
```

## Binomial distribution

The student loved the probability course and she doesn't mind retaking it, but since she doesn't want to delay her graduation, she needs to pass the course in the current year. In the course, there are three exams and needs to pass at least two of them. Therefore, she is interested in determining the probability of passing two exams out of the three without studying.

The student knows that needs to know the probability of success, $p$, since she remembers from the probability lectures that it is a Bernoulli process. Thus, she performs a survey to other students from previous courses. 50 students admitted not studying for a probability exam and 2 of them passed it. Then, she determines the success probability as $p = 2/50  = 0.04$.

**And now?**

Let's go step by step. Considering that the exam's outcomes (failure/success) are independent, the probability of having two successes and one failure is $p^2(1-p)$ (remember that events are independent!). However, there are three different sequences which may lead to that situation: passing the first two exams, passing the first and the third exam or passing the last two exams. Hence, the probability of two successes and one failure in three trials can be obtained from the addition rule[^addition] as follows:

$
p_Y(2)=P[Y=2|3, p]=\binom{3}{2}p^2(1-p)^{3-2}=\frac{3!}{2!(3-2)!}p^2(1-p)=3p^2(1-p)
$

which is the pmf of the **Binomial distribution**. Thus, we went from the **Bernoulli** distribution to the **Binomial** distribution. The pmf of the Binomial distribution is then defined as

$
p_Y(y) = P[Y=y|n, p] = \binom{n}{x}p^x(1-p)^{n-x}  \hspace{1cm}  \rm{for} \ y = 0, 1, ..., n; \ p \in [0,1]$

$
p_Y(y) = P[Y=y|n, p] = 0       \hspace{3.7cm}          \rm{otherwise}
$

where

$
\binom{n}{y} = \frac{n!}{x!(n-y)!}
$

which is the total number of possible combinations when selecting y successes from n trials. Thus, in our example, the random variable Y represents the number of successes in n trials and follows a Binomial distribution with parameters $p$ (probability of success) and $n$ (number of trials). The cumulative distribution function (cdf) of a Binomial distribution is given by

$
F_Y(y) = \sum_{k=0}^x\binom{n}{y}p^k(1-p)^{n-k}
$

Note that the maximum value of the cdf is reached for $Y = n$.

```{admonition} Binomial-distributed variable
:class: tip

The conditions for a random variable to follow a Binomial distribution are:
 1. A series of Bernoulli trials is made with two possible outcomes: success or failure.
 2. There is a constant probability of success, $p$.
 3. There is a fixed number of trials, $n$.
 4. The outcomes of the trials are independent.
 5. The random variable X is the total number of successes in $n$ trials and the order of the successes is irrelevant.
```

Finally, **let's answer the student questions**. Applying the Binomial distribution: 
$
p_Y(y) = P[Y=2|3, 0.04] = \binom{3}{2}p^2(1-p)^{3-2} \approx 0.005
$

Sadly, there is a very low chance that the student can make it without studying! However, now she knows Bernoulli processes and Binomial distribution and that for sure increases the chances of passing!

[^addition]: The addition rule is a basic probability axiom which states that for any sequence of k mutually exclusive events $A_1, A_2,..., A_k$ is true that the probability of all of them together is the same as the sum of the individual probabilities.
$
P[A_1+A_2+...+A_k] = P[A_1]+P[A_2]+...+P[A_k]
$


% START-CREDIT
% source: extreme_value_analysis
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Patricia Mares Nasarre. {ref}`Find out more here <extreme_value_analysis_credit>`.
```
% END-CREDIT
