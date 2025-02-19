
# Method of moments: let's practice

As part of the quality control of the construction of a building, lab tests are performed to determine the compressive strengths of concrete. The following values in $N/mm^2$ are obtained: 60.5, 59.8, 53.4, 56.9 and 61.9. 

The engineer responsible for quality assumes that the compressive strength follows a uniform distribution, whose CDF is given by 

$$
F(x) = 0   \hspace{1cm}   for \ x<a
$$

$$
F(x) = \frac{x-a}{b-a}   \hspace{1cm}   for \ a\leq x \leq b
$$

$$
F(x) = 0  \hspace{1cm} for \ x>b
$$

Determine the value of $a$ and $b$ based on the observations using the method of moments.

```{admonition} Answer
:class: tip, dropdown

The mean and variance of the observations can be calculates as:

$$
   \overline{X} = 58.5
$$


$$
   \sigma^2 = 11.46
$$

We know that the expectation and variance of the uniform distribution is given by

$$
E[X]=\frac{1}{2}(a+b)
$$

$$
Var[X] = \frac{1}{12}(b-a)^2
$$

Thus, equating the mean and variance in the observations to those of the distribution, we obtain the following system

$$
58.5=\frac{1}{2}(a+b)
$$

$$
11.46 = \frac{1}{12}(b-a)^2
$$

Solving the system, $a \approx 52.64$, and $b \approx 64.36$. Note that $a \approx 64.36$, and $b \approx 52.64$ is also a solution to the system, so we choose $a<b$ based on our definition of the uniform distribution.

```

Now that the engineer knows the uniform distribution which characterizes the compressive strength of the concrete samples, he needs to compute the probability of being above $55N/mm^2$, since it is the required resistance for the construction.

```{admonition} Answer
:class: tip, dropdown

$$
P[X>55N/mm^2] = 1 - F(55) = 1 - \frac{55-52.64}{64.36-52.64} \approx 0.80
$$

Thus, there is a probability of 0.80 to fulfill the required resistence and a probabiltiy of 0.20 of not doing it. He will have to contact the contractor!
```