# Fourier Transform

## Before starting...

Let us start by taking a look into the results found in the previous chapter. We have defined the complex exponential Fourier series for a periodic signal $x(t)$ as:

$$x(t)=\sum_{k=-\infty}^{\infty}X_ke^{jk\omega_0 t}$$

with $\omega_0=2\pi f_0$ and $k\in\mathbb{Z}$ and complex coefficients found as

$$X_k=\frac{1}{T_0}\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)e^{-jk\omega_0 t}dt, \hspace{10px}k\in\mathbb{Z}$$

where the integration period $T_0$ is taken symmetrically about zero.

## Fourier Transform

When the period $T_0$ increases, the frequencies belonging to the Fourier series coefficients ($kf_0$) lie closer and closer together as $f_0=1/T_0$ decreases. Now, what if $T_0$ approaches infinity? That is, what would happen if we have an *a-periodic* signal?

Fourier coefficients will lie infinitesimally close to each other, so they define **continuous function of frequency**, $f\approx kf_0$

![frequencies](https://files.mude.citg.tudelft.nl/frequencies.png "frequencies")

:::{card} Derivation

```{admonition} MUDE Exam Information
:class: tip, dropdown
This derivation is provided for additional insight and will not be part of the exam.
```

Substituting the definition of the series coefficients into $x(t)$, we find

$$x(t)=\sum_{k=-\infty}^{\infty}\left(f_0\int_{-\frac{T_0}{2}}^{\frac{T_0}{2}}x(t)e^{-jk2\pi f_0t}dt\right)e^{jk2\pi f_0t}$$

Now, when $T_0\to\infty$, $f_0$ becomes infinitesimally small, $f_0\to df$. Multiplying $f_0$ with $k$ then becomes a continuous function, $kf_0\to f$. The summation from $k=-\infty$ to $k=\infty$ then becomes an integration in $f$ from $f=-\infty$ to $f=\infty$

$$x(t)=\int_{-\infty}^{\infty}\left(df\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}\,dt\right)e^{j2\pi ft}$$

Re-arranging the terms:

$$x(t)=\int_{-\infty}^{\infty}\underbrace{\left(\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}\,dt\right)}_{X(f)}e^{j2\pi ft}\,df$$


:::

The integral between parentheses is defined as **Fourier integral** or (continuous-time) **Fourier transform**, $\mathcal{F}()$:

$$X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}dt$$

The complex number $X_k$ of the Fourier series is now a complex **function** of the frequency, $f$: $X(f)$.

The **inverse Fourier transform**, $\mathcal{F}^{-1}()$ can also be derived

$$x(t)=\int_{-\infty}^{\infty}X(f)e^{j2\pi ft}df$$

```{note}
To obtain $x(t)$ from $X(f)$, we integrate over frequency, $f$, and the result is a function of time, $t$
```

Hence, Fourier transform and its inverse can be used to transform time signal to the frequency domain, and the other way around. This yields a **Fourier transform pair**:

$$x(t)\xrightarrow{\mathcal{F}}X(f)\xrightarrow{\mathcal{F}^{-1}}x(t)$$

### Conditions

**Sufficient** conditions for convergence of Fourier transform integrals are:

* $x(t)$ absolutely integrable, i.e. $\int_{-\infty}^{\infty}|x(t)|dt<\infty$
* discontinuities, if any, should be finite

### Amplitude and phase

Like the coefficients of complex Fourier series, a Fourier transform can also be written in terms of **magnitude** and **phase**:

$$X(f)=|X(f)|e^{j\theta(f)}$$

with

$$\begin{gather*}|X(f)|=\sqrt{\left(\text{Re}(X(f)) \right)^2+\left(\text{Im}(X(f))\right)^2}\\ \theta(f)=\arctan\left(\frac{\text{Im}(X(f))}{\text{Re}(X(f))}\right)\end{gather*}$$

![complex_plane_2](https://files.mude.citg.tudelft.nl/complex_plane_2.png "complex_plane_2")

When $x(t)$ is real, then

$$|X(f)|=|X(-f)|\hspace{10px}\text{and}\hspace{10px}\theta(f)=-\theta(-f)$$

* Magnitude $|X(f)|$ is an **even** function of $f \to$ **amplitude spectrum**
* Phase $\theta(f)$ is an **odd** function of $f \to$ **phase spectrum**

![odd_even](https://files.mude.citg.tudelft.nl/odd_even.png "odd_even")

The figure above illustrates an example of $|X(f)|$ and $\theta(f)$ both as a function of frequency.

## Summary

A-periodic functions can be written as integrals, **continuous** over **frequency**. This yields the so-called **Fourier tranform** (and its inverse):

$$\begin{gather*}X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}dt\\ x(t)=\int_{-\infty}^{\infty}X(f)e^{j2\pi ft}df\end{gather*}$$

Amplitude and phase spectrum are given by:

$$\begin{gather*}|X(f)|=\sqrt{\left(\text{Re}(X(f)) \right)^2+\left(\text{Im}(X(f))\right)^2}\\ \theta(f)=\arctan\left(\frac{\text{Im}(X(f))}{\text{Re}(X(f))}\right)\end{gather*}$$

## Exercises

:::{card} Fourier Transform Exercise (1 of 2)

The signal $x(t)=\Pi(\frac{t}{\tau})$ is defined by a pulse function with duration $\tau$ [s]:

$$
\Pi\left(\frac{t}{\tau}\right) = 
\begin{cases}
1, & \text{for $-\frac{\tau}{2} \leq t \leq \frac{\tau}{2}$}.\\
0, & \text{otherwise}.
\end{cases}
$$

Derive an expression for the Fourier transform $X(f)$ of signal $x(t)$.

_Hint: you may want to use Euler's formula to turn the difference of two complex exponentials into a sine function. In addition, to turn your answer into an even more compact form, you may want to use the cardinal sine, which is defined as $\textrm{sinc}(z)=\frac{\sin(\pi z)}{\pi z}$._

````{admonition} Solution
:class: tip, dropdown

The video below illustrates how to arrive at the final solution, which is presented here:

$$
X(f) = 
\tau \,\textrm{sinc}(\tau f)
$$

```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/w3hhvGzeXoA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

The solution can also be found using SymPy:
```python
import sympy as sym
```

```python
t = sym.symbols('t')
tau, f = sym.symbols('tau, f', positive=True)
x = sym.Piecewise((0, t < -tau/2), (1, t < tau/2), (0, True))
display(x)
```
$\begin{cases} 0 & \text{for}\: t < - \frac{\tau}{2} \\1 & \text{for}\: t < \frac{\tau}{2} \\0 & \text{otherwise} \end{cases}$

```python
solution = sym.integrate(x*sym.exp(-sym.I*2*sym.pi*f*t), (t,-sym.oo,sym.oo))
simplified_solution = sym.simplify(solution)
display(solution)
display(simplified_solution)
```
$- \frac{i e^{i \pi f \tau}}{2 \pi f} + \frac{i e^{- i \pi f \tau}}{2 \pi f}$

$\frac{\sin{\left(\pi f \tau \right)}}{\pi f}$
````

:::

:::{card} Fourier Transform in the Limit Exercise (2 of 2)

Given the Fourier transform $X(f)=\delta(f)$, find the expression for signal $x(t)$. Then, verify the following two points:

1. When $x(t)=e^{j2\pi f_0 t}$, then $X(f)=\delta(f-f_0)$, and
2. When $x(t)=\cos(2\pi f_0 t)$, then $X(f)=\frac{1}{2}(\delta(f-f_0)+\delta(f+f_0))$.

_Hint: for the first part (finding $x(t)$), use the *inverse* Fourier transform, and use the sifting property of the Dirac delta function (in this case in the frequency domain) when solving the integral._

````{admonition} Solution
:class: tip, dropdown

The video below illustrates how to arrive at the final solution, which is presented here:

$$
x(t) = \cos (2\pi f_0 t)
$$

```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/VigjJtHXNY4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

````

:::