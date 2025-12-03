# Failure distributions

A failure distribution is a model that describes mathematically the lifetime of a material, a devise or a structure or system. For instance, it may describe the uncertainty in the amount months before a light bulb burns out. 

In this case, let $X$ be a life variable. An important concept is the _failure rate_ or _hazard rate_ at a time $t$, denoted as $r_X(t)$ and given by

$$
r_X(t)=\lim_{\Delta\to\infty}\frac{⁡P(X≤t+\Delta|X>t)}{\Delta}
$$

The failure rate is the probability of the component or system failing at a given instant, the probability of “instantaneous” failure. Note that in the denominator of the equation above, we compute for a given time $t$ the probability of the lifetime of the component ($X$) being higher than $t$ but smaller than $t+\Delta$. For small $\Delta>0$, $r_X (t)\approx P(X≤t+\Delta|X>t)$. That is, the probability of observing a failure right after time $t$ given that the component has survived until $t$.

The failure rate can also be computed with the concepts learned in previous weeks. If the life variable $X$ has density $f(t)$ and cumulative distribution function $F(t)$ then 


$$
r_X (t)=\frac{f(t)}{1-F(t)}
$$

Some common life distributions used in the literature are Exponential, Gamma and Weibull, as we will see in the next subsections.

## Exponential failure rate

Given that the lifetime of a component follows an exponential distribution, $X \sim Exp(\lambda)$, the failure rate of the variable $X$ is given by 

$$
r(t)=\frac{f(t)}{1-F(t)}=\frac{\lambda e^{-λt}}{1-(1-e^{-\lambda t}) }=λ 
$$

for $\lambda>0$ and $t\geq 0$. Therefore, the failure rate of the variable $X$ is equal to a constant value $\lambda$ regardless the instant $t$. Figure below shows different failure rates associated with the corresponding pdfs of $t$.

Recall that the PDF of the exponential distribution is given by

$$f(t)=\lambda e^{-\lambda t}$$

while the CDF of the exponential distribution is given by 

$$ F(t) = 1-e^{-\lambda t} $$

```{figure} https://files.mude.citg.tudelft.nl/expon.png

---

---
Exponential distribution for $t$: (a) pdf, and (b) failure rate.
```

## Gamma failure rate

Given that the lifetime of a component follows an gamma distribution, $X \sim gamma(\lambda, \alpha)$, the failure rate of the variable $X$ is given by 

$$
r(t) = \lambda (\lambda t )^{\alpha -1 } \frac{1}{\Gamma(\alpha)}e ^{-\lambda t}
$$

for $\lambda$, $\alpha > 0$, $t\geq 0$ and $\Gamma$ being the gamma function. 

Figure below depicts the influence of the parameters of the gamma distribution , $\lambda$ and $\alpha$ in their corresponding failure rate. When $\alpha=1$, the gamma distribution reduces to the exponential and, thus, the failure rate is constant; $\alpha$ controls the shape of the distribution and, thus, the shape of the failure rate. The gamma distribution has increasing failure rate for $\alpha >1$. To get an intuition of the influence of the parameters $\alpha$ and $\lambda$ in the failure rate, you can play with the interactive element below. 

```{figure} https://files.mude.citg.tudelft.nl/gamma.png

---

---
Gamma distribution for $t$: (a) pdf, and (b) failure rate.
```

Notice that a common parameterization for the gamma density is 

$$
f(t) =  t^{\alpha -1 } \frac{\lambda^{\alpha}}{\Gamma(\alpha)}e ^{-\lambda t}
$$

## Weibull failure rate

Given that the lifetime of a component follows an Weibull distribution, $X \sim Weibull(\lambda, \alpha)$, the failure rate of the variable $X$ is given by 

$$
r(t) = \lambda \alpha t^{\alpha-1}
$$

for $\lambda$, $\alpha > 0$, $t\geq 0$. 

Figure below depicts the influence of the parameters of the Weibull distribution , $\lambda$ and $\alpha$ in their corresponding failure rate.

```{figure} https://files.mude.citg.tudelft.nl/weibull_min.png

---

---
Weibull distribution for $t$: (a) pdf, and (b) failure rate.
```

The Weibull distribution has increasing failure rate for $\alpha >1$. Similarly to the gamma distribution, $\alpha$ controls the shape of the distribution and, thus, the shape of the failure rate. To get an intuition of the influence of the parameters $\alpha$ and $\lambda$ in the failure rate, you can play with the interactive element below.

Notice that some common parameterizations for the Weibull density are

$$
f(t) = \lambda\alpha  t^{\alpha-1}e^{-\lambda t^\alpha}
$$

$$
f(t) = \frac{b}{a}\left(\frac{t}{a}\right)^{b-1} e^{-\left(\frac{t}{a}\right)^b}
$$

for $a$, $b > 0$, $t\geq 0$. $a$ is usually called the scale parameters and $b$, the shape parameter.

## Play with the parameters!

````{iframe-figure} ../_static/elements/element_failure_rate.html
:name: failure_rate
:aspectratio: 2 / 1

Interactively visualize the influence of the parameters in the failure rate for the Exponential, Gamma and Weibull distribution.
````
.