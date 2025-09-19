(summary_dist)=
# Summary of parametric distributions

Here a summary of the main equations for each of the presented distribution functions is presented.

```{admonition} MUDE exam information
:class: tip, dropdown
You do not need to know the equations of the distribution functions by heart. You just need to know how the distribution looks (PDF/CDF), how it responds to changes in the parameters, and some of its basic properties (particularly symmetry or bounds).
```

## Choosing a distribution

If you need help to choose a distribution type for your data, the table below may help you make a choice:

<table>
  <thead>
    <tr><th>Distribution</th><th>left bound</th><th>right bound</th><th>left-tailed</th><th>symmetric</th><th>right-tailed</th><th>scipy name</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Uniform</td>
      <td style="background:#dfd;">yes</td>
      <td style="background:#dfd;">yes</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#dfd;">yes</td>
      <td style="background:#fdd;">no</td>
      <td>uniform</td>
    </tr>
    <tr>
      <td>Gaussian</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#dfd;">yes</td>
      <td style="background:#fdd;">no</td>
      <td>norm</td>
    </tr>
    <tr>
      <td>Lognormal</td>
      <td style="background:#dfd;">yes</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#dfd;">yes</td>
      <td>lognorm</td>
    </tr>
    <tr>
      <td>Gumbel (right-tailed)</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#dfd;">yes</td>
      <td>gumbel_r</td>
    </tr>
    <tr>
      <td>Gumbel (left-tailed)</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#dfd;">yes</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td>gumbel_l</td>
    </tr>
    <tr>
      <td>exponential</td>
      <td style="background:#dfd;">yes</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#fdd;">no</td>
      <td style="background:#dfd;">yes</td>
      <td>expon</td>
    </tr>
    <tr>
      <td>beta</td>
      <td style="background:#dfd;">yes</td>
      <td style="background:#dfd;">yes</td>
      <td style="background:#ffe8a1;">possible</td>
      <td style="background:#ffe8a1;">possible</td>
      <td style="background:#ffe8a1;">possible</td>
      <td>beta</td>
    </tr>
  </tbody>
</table>

```{admonition} Notation
:class: tip

One challenge when dealing with distributions is notation, for two main reasons: 1) the symbols used to represent random variables and parameters vary across different fields (and even _within_ a given field); and 2) the formulation of key equations (i.e., the PDF and CDF) can vary depending on the parameterization used.

Why such variation? Let's just say tradition, history, and stubbornness play a big role here. But more importantly, one should recognize that the equations or parameters often have physical meaning, which makes a certain formulation more logical. Symbols often must be chosen carefully to not conflict with others used in a given field.

To illustrate the point, consider the following three formulations of the PDF of the exponential distribution (along with a link to the page ):

- [Wikipedia](https://en.wikipedia.org/wiki/Exponential_distribution), [Excel](https://support.microsoft.com/en-us/office/expon-dist-function-4c12ae24-e563-4155-bf3e-8b78b6ae140e): $f(x) = \lambda \operatorname{exp}(-\lambda x)$
- [Matlab](https://www.mathworks.com/help/stats/exponential-distribution.html):  $f(x) = \frac{1}{\mu} \operatorname{exp}(\frac{-x}{\mu})$
- [Scipy Stats Module](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.expon.html#scipy.stats.expon):  $f(x) = \operatorname{exp}(- x)$

Note that the formulation is very different between each case, and either $\lambda$ or $\mu$ is used. If you are not careful when using distributions from different textbooks or software packages, it is very easy to make mistakes! The scipy stats formulation is especially striking; you will learn more about this later (location, shape and scale).

Our advice: **always check the formulation of the PDF, CDF, and parameters of a distribution and be sure to use them consistently.**

In this case, "consistency" can mean, for example, using the right equations to compute the distribution parameters from the moments (mean and standard deviation) of the distribution. In general, there is no "correct" formulation or set of parameters; in this book we present a set of parameters and formulations that are consistent with each other and commonly used in civil engineering and geosciences.
```

## Statistical moments

Below, we will list the equations for the PDF, CDF, mean, and variance for the parametric distributions we have discussed.


#### Uniform

```{list-table}
:header-rows: 1

* - Object 
  - Equation
* - PDF
  - $\displaystyle f(x) = \begin{cases}\cfrac{1}{b-a} & \text{for }x \in [a,b] \\ 0 & \text{otherwise} \end{cases}$
* - CDF
  - $F(x)=\begin{cases}0 & \text{for } x<a \\ \cfrac{x-a}{b-a} & \text{for } x\in[a,b] 1 & \text{for } x>b\end{cases}$
* - Mean and variance
  - $\begin{array}{ll} E[X]=\frac{1}{2}(a+b) \\ Var[X]=\frac{1}{12}(b-a)^2 \end{array}$ 
```

#### Gaussian

```{list-table}
:header-rows: 1

* - Object 
  - Equation
* - PDF
  - $f(x) = \cfrac{1}{\sigma \sqrt{2\pi}}e^{\left(\normalsize-\cfrac{(x-\mu)^2}{2\sigma^2}\right)}$
* - CDF
  - $F(x) = \cfrac{1}{2}\left(1+\text{erf}\left(\cfrac{x-\mu}{\sigma\sqrt{2}}\right)\right)$
* - Mean and variance
  - $\begin{array}{ll} E[X] = \mu \\ Var[X] = \sigma^2  \end{array}$
```

#### Lognormal

```{list-table}
:header-rows: 1

* - Object 
  - Equation
* - PDF
  - $f(x) = \cfrac{1}{x \sigma \sqrt{2 \pi}}e^{\left( \normalsize-\cfrac{(ln(x)-\mu)^2}{2\sigma^2}\right)}$
* - CDF
  - $F(x) = \Phi\left( \cfrac{ln(x)-\mu}{\sigma} \right) = \frac{1}{2}\left[ 1+\text{erf}\left( \cfrac{ln(x)-\mu}{\sigma \sqrt{2}}\right)\right]$
* - Mean and variance
  - $\begin{array}{ll} E[X]=e^{\normalsize\mu + \frac{\sigma^2}{2}} \\ Var[X] = \left( e^{\normalsize\sigma^2}-1 \right)e^{2\mu + \sigma^2} \end{array}$
```

#### Gumbel

```{list-table}
:header-rows: 1

* - Object 
  - Equation
* - PDF
  - $f(x) = \cfrac{1}{\beta} e^{\normalsize-\left(z + e^{\normalsize-z}\right)}\text{, where }z=\cfrac{x-\alpha}{\beta}$
* - CDF
  - $F(x)=e^{\normalsize-e^{\normalsize-z}}$
* - Mean and variance
  - $\begin{array}{ll} E[X] = \alpha + \beta\gamma,\; \gamma = 0.5772 \\ Var[X] = \cfrac{\pi^2}{6}\beta^2 \end{array}$
```

#### Exponential

```{list-table}
:header-rows: 1

* - Object 
  - Equation
* - PDF
  - $f(x) = \lambda e^{\normalsize-\lambda x}$
* - CDF
  - $F(x) = 1 - e^{\normalsize-\lambda x}$
* - Mean and variance
  - $\begin{array}{ll} E[X] = \cfrac{1}{\lambda} \\ Var[X] = \cfrac{1}{\lambda^2} \end{array}$
```

#### Beta

```{list-table}
:header-rows: 1

* - Object 
  - Equation
* - PDF
  - $f(x) = \frac{x^{\alpha - 1} (1 - x)^{\beta - 1}}{B(\alpha, \beta)}$
* - CDF
  - $F(x) = \frac{1}{B(\alpha, \beta)} \int_0^x t^{\alpha - 1} (1 - t)^{\beta - 1} dt$
* - Mean and variance
  - $\begin{array}{ll} E[X] = \frac{\alpha}{\alpha + \beta} \\ Var[X] = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha+\beta+1)}  \end{array}$
```

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre, Robert Lanzafame, and Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT