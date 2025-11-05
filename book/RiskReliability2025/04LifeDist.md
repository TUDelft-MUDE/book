## Reliability analysis & Failure distributions

A failure distribution is a model that describes mathematically the lifetime of a material, a devise or a structure or system. In this case let $X$ be a life variable. An important concept is the failure rate  $r_X(t)=\lim_{\Delta\to\infty}\frac{⁡P(X≤t+\Delta|X>t)}{\Delta}$ For small $\Delta>0$, $r_X (t)\approx P(X≤t+\Delta|X>t)$. The failure rate is the probability of “instantaneous” failure. That is, the probability of observing a failure right after time $t$ given that the component has survived until $t$. The hazard rate can also be computed with the concepts learned in previous weeks. If the life variable $X$ has density $f(t)$ and cumulative distribution function, $F(t)$ then 


$$r_X (t)=\frac{f(t)}{1-F(t)}$$

Some common life distributions are:

* Exponential 

$f(t)=\lambda e^{-\lambda t}, r(t)=\frac{f(t)}{1-F(t)}=\frac{\lambda e^{-λt}}{1-(1-e^{-\lambda t}) }=λ $ for $\lambda>0$ and $t\geq 0$

 * Gamma 

 $f(t) = \lambda (\lambda t )^{\alpha -1 } \frac{1}{\Gamma(\alpha)}e ^{-\lambda t}$, $\lambda$, $\alpha > 0$, $t\geq 0$. Notice that a common parametrization for the gamma density is $f(t) =  t^{\alpha -1 } \frac{1}{b^\alpha \Gamma(\alpha)}e ^{-t/b}$

 * Weibull 

 $f(t) = \lambda\alpha t^{\alpha-1}e^{-\lambda t^\alpha}$, $r(t) = \lambda \alpha t^{\alpha-1}$, $\lambda$, $\alpha$ $>0$, $t\geq 0$. Another common parametrization of the Weibull density is $f(t) = \frac{b}{a}\left(\frac{t}{a}\right)^{b-1} e^{-\left(\frac{t}{a}\right) t^b}$ 

```{figure} https://files.mude.citg.tudelft.nl/failure_rate.png
 
---
 
---
Failure rate curves of the gamma distribution $\lambda =1$.
```

```{figure} https://files.mude.citg.tudelft.nl/failure_rate2.png
 
---
 
---
Failure rate curves of the Weibull distribution for $\lambda = 1$.
```

The exponential distribution has constant failure rate. The gamma and the Weibull distribution have increasing failure rate for $\alpha >1$.