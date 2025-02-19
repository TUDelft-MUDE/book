(summary_dist)=
# Summary of parametric distributions

Here a summary of the main equations for each of the presented distirbution functions is presented.

```{list-table}
:header-rows: 1

* - Distribution
  - PDF
  - CDF
  - Mean and variance
* - Normal/Gaussian
  - $f(x) = \cfrac{1}{\sigma \sqrt{2\pi}}e^{\left(\normalsize-\cfrac{(x-\mu)^2}{2\sigma^2}\right)}$
  - $F(x) = \cfrac{1}{2}\left(1+\text{erf}\left(\cfrac{x-\mu}{\sigma\sqrt{2}}\right)\right)$
  - $\begin{array}{ll} E[X] = \mu \\ Var[X] = \sigma^2  \end{array}$
* - Uniform
  - $\displaystyle f(x) = \begin{cases}\cfrac{1}{b-a} & \text{for }x \in [a,b] \\ 0 & \text{otherwise} \end{cases}$
  - $F(x)=\begin{cases}0 & \text{for } x<a \\ \cfrac{x-a}{b-a} & \text{for } x\in[a,b] 1 & \text{for } x>b\end{cases}$
  - $\begin{array}{ll} E[X]=\frac{1}{2}(a+b) \\ Var[X]=\frac{1}{12}(b-a)^2 \end{array}$ 
* - Exponential
  - $f(x) = \lambda e^{\normalsize-\lambda x}$
  - $F(x) = 1 - e^{\normalsize-\lambda x}$
  - $\begin{array}{ll} E[X] = \cfrac{1}{\lambda} \\ Var[X] = \cfrac{1}{\lambda^2} \end{array}$
* - Gumbel
  - $f(x) = \cfrac{1}{\beta} e^{\normalsize-\left(z + e^{\normalsize-z}\right)}\text{, where }z=\cfrac{x-\alpha}{\beta}$
  - $F(x)=e^{\normalsize-e^{\normalsize-z}}$
  - $\begin{array}{ll} E[X] = \alpha + \beta\gamma,\; \gamma = 0.5772 \\ Var[X] = \cfrac{\pi^2}{6}\beta^2 \end{array}$
* - Lognormal
  - $f(x) = \cfrac{1}{x \sigma \sqrt{2 \pi}}e^{\left( \normalsize-\cfrac{(ln(x)-\mu)^2}{2\sigma^2}\right)}$
  - $
F(x) = \Phi\left( \cfrac{ln(x)-\mu}{\sigma} \right) = \frac{1}{2}\left[ 1+\text{erf}\left( \cfrac{ln(x)-\mu}{\sigma \sqrt{2}}\right)\right]
$
  - $\begin{array}{ll} E[X]=e^{\normalsize\mu + \frac{\sigma^2}{2}} \\ Var[X] = \left( e^{\normalsize\sigma^2}-1 \right)e^{2\mu + \sigma^2} \end{array}$

```

```{admonition} MUDE exam information
:class: tip, dropdown
You do not need to know the equations of the distribution functions by heart. You just need to know how the distribution looks (PDF/CDF), how it responds to changes in the parameters and some basic properties (symmetry or bounds).
```