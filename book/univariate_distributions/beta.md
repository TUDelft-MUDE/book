
# Beta distribution

## PDF

Beta distributions are a very useful choice for univariate variables that have a natural lower and upper bound. By default, a beta distribution is defined for $0 \leq x \leq 1$ as

$$
p(x) = \frac{x^{\alpha - 1} (1 - x)^{\beta - 1}}{B(\alpha, \beta)}, 
$$

where $B(\alpha, \beta)$ is the *Beta function*. This Beta function is, defined as

$$
B(\alpha, \beta) = \int_0^1 t^{\alpha - 1} (1 - t)^{\beta - 1} dt = \frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha + \beta)},
$$

where $\Gamma$ is the Gamma function. The parameters $\alpha$ and $\beta$ must both be larger or equal to one ($\alpha,\beta \geq 1$) and affect the shape of the pdf: high values of $\alpha$ shift the pdf towards the right, high values of $\beta$ shift the pdf towards the left.

## CDF

The cdf of the Beta distribution describes the probability that a Beta-distributed random variable $X$ takes a value less than or equal to some $x \in [0, 1]$. It is defined as

$$
F(x; \alpha, \beta) = \int_0^x p(t) \, dt = \frac{1}{B(\alpha, \beta)} \int_0^x t^{\alpha - 1} (1 - t)^{\beta - 1} dt,
$$

where $p(t)$ is the probability density function given above. This integral does not, in general, have a closed-form solution, but it is commonly expressed in terms of the **regularized incomplete Beta function** $I_x(\alpha, \beta)$:

$$
F(x; \alpha, \beta) = I_x(\alpha, \beta) = \frac{1}{B(\alpha, \beta)} \int_0^x t^{\alpha - 1} (1 - t)^{\beta - 1} dt.
$$

The regularized incomplete Beta function maps $x \in [0, 1]$ to $F(x) \in [0, 1]$ and provides a numerically stable way to evaluate the CDF. It is available in most scientific computing libraries. We list this cdf here only for completeness' sake.


## Interactive Element

Below, you find an interactive element that shows the pdf and cdf of a beta distribution. The element also includes sliders for the **location** and **scale** which allow us to scale this element to intervals other than $[0,1]$.

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_beta_pdf.html
:name: beta_pdf

Interactively visualize the relationship between the PDF and the CDF of a beta distribution.
````

<iframe src="../_static/elements/element_beta_pdf.html" style="width: 100%; aspect-ratio: 1.5 / 1; border: none; border-radius: 8px;"></iframe>

## Intuition & Interesting Properties

The beta pdf can be useful in many settings you will encounter in your professional lives. Beta pdfs (and their multivariate counterpart, Dirichlet pdfs) are often used for **simplex variables**, which are variables that must add up to a certain value. Examples of simplex variables include 
- the **sea ice area fraction**, which describes the percentage of a certain area of sea that is covered by sea ice (naturally, the open and ice-covered percentages must add to 100%). 
- the **expected value of a coin**, that is to say the probability that a flipped coin comes up either head (zero) or tails (one). Since a flipped coin only has binary outcomes (head *or* tails; we neglect the chance that it may land on its side), the expected value of repeated coin flipping must lie between zero (a loaded coin that only ever lands on "head") and one (a loaded coin that only ever lands on "tails").
- similarly, this can be used for other binary choices, such as the **path drivers take at a fork in the road**. If we designate left as zero and right as one, then the average choice must be between zero (all drivers go left) over 0.5 (exactly half the drivers go left, and half go right) to one (all drivers go right).
More generally, beta pdfs can also be rescaled and used for variables that have natural lower and upper bounds, such as *dissolved concentrations* of a chemical compound. Such concentrations can never be negative (i.e., $x \geq 0$) but cannot exceed some saturation concentration ($x \leq C_{\text{sat.}}$), which makes beta pdfs a natural choice for such quantities.





Blorb

```

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Maximilian Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT