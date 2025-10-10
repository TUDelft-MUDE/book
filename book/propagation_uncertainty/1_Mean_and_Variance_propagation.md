(01_errorprop)=
# Mean and Variance propagation laws

Now, will only consider the propagation of the mean (= expectation) and variance, and not the transformation of the full PDF or CDF.

The general form of our problem is given as follows. Consider the single function of $m$ random variables

$$
X = q(\mathbf{Y})=q(Y_1,\ldots,Y_m)
$$

with the mean and covariance matrix of $\mathbf{Y}$ known:

$$
\mathbb{E}(\mathbf{Y})=\boldsymbol\mu_Y, \quad \mathbb{D}(\mathbf{Y})=\boldsymbol\Sigma_Y
$$


## Video

In this video the first part of this chapter is explained. You can also first read this section, and only watch the video if you like someone to explain it.

```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/EiuX9a7SIzc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## What are the mean and variance of $X$?

Let's start with the mean for the case that the function is linear: 

$$
q(\mathbf{Y})=a_1 Y_1+ a_2 Y_2 +\cdots+ a_m Y_m + c
$$

with the $a_i$ and $c$ deterministic constants. Since the expectation operator is a linear operator, we have:

$$
\mathbb{E}(q(\mathbf{Y}))=\mathbb{E}(a_1 Y_1+ a_2 Y_2 +\cdots a_m Y_m + c)= a_1 \mathbb{E}(Y_1)+\cdots+ a_m \mathbb{E}(Y_m)+c
$$

But what if the function is non-linear? Then we can use the [Taylor series](taylor-series) approximation of $q(\mathbf{Y})$. 

## Function of one random variable 

We will first look at the simplest case, where we have a function of a single random variable, $X=q(Y)$, with the Taylor approximation:

$$
q(Y)\approx q(\mu_Y) +\left(\frac{\partial q}{\partial Y}\right)_0(Y-\mu_Y) + \frac{1}{2!} \left(\frac{\partial^2 q}{\partial Y^2}\right)_0(Y-\mu_Y)^2 + \text{H.O.T}
$$

where we take the mean $y_0=\mu_Y$ as the logical initial guess of the random vector $Y$. (H.O.T. stands for higher-order terms). The subscript $_0$ indicates that the partial derivatives are evaluated at $y_0=\mu_Y$.

Due to the linearity of the expectation we then find as a second-order approximation of $\mathbb{E}(q(Y))$, known as *mean propagation law*:

$$
\begin{align*}
\mathbb{E}(X)=\mathbb{E}(q(Y))&\approx \mathbb{E}(q(\mu_Y) +\left(\frac{\partial q}{\partial Y}\right)_0(Y-\mu_Y) + \frac{1}{2!} \left(\frac{\partial^2 q}{\partial Y^2}\right)_0(Y-\mu_Y)^2)\\
&= \mathbb{E}(q(\mu_Y)) +\left(\frac{\partial q}{\partial Y}\right)_0\mathbb{E}\left((Y-\mu_Y)\right) + \frac{1}{2} \left(\frac{\partial^2 q}{\partial Y^2}\right)_0\mathbb{E}\left((Y-\mu_Y)^2\right)\\
&= q(\mu_Y)+\frac{1}{2} \left(\frac{\partial^2 q}{\partial Y^2}\right)_0\sigma_Y^2
\end{align*}
$$
where in order to arrive at the last equation we should recognize that:
* $\mathbb{E}(q(\mu_Y))=q(\mu_Y)$ (since $\mu_Y$ is deterministic and known) 
* $\mathbb{E}(Y-\mu_Y)=\mathbb{E}(Y)-\mu_Y= 0$ 
* $\mathbb{E}\left((Y-\mu_Y)^2\right)=\sigma_Y^2$.

For the variance of $X=q(Y)$ it generally suffices to use a first-order approximation. The result follows as:

$$
\sigma_X^2 =\left(\frac{\partial q}{\partial Y}\right)_0^2\sigma_Y^2
$$

and is referred to as the *variance propagation law*.

:::{card} Example $X=Y^2$

$$
\begin{align*}
\mathbb{E}(X)&\approx \mu_Y^2 + \frac{1}{2}\cdot 2 \cdot \sigma_Y^2= \mu_Y^2+\sigma_Y^2\\
\sigma_X^2 &\approx \left( 2\mu_Y\right)^2\sigma_Y^2 = 4\mu_Y^2\sigma_Y^2
\end{align*}
$$
:::

:::{card} Example gravitational force
<iframe src="https://tudelft.h5p.com/content/1292060618387216967/embed" aria-label="Quiz_gravity" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>
:::

## Function of two random variables 
Let's consider the case that we have one function of two random variables, $\mathbf{Y} = [Y_1\; \;Y_2]^T$ with known mean and covariance matrix:

$$
\mathbb{E}(\mathbf{Y})=\boldsymbol\mu_Y =\begin{bmatrix}\mu_1\\ \mu_2 \end{bmatrix}, \quad \boldsymbol\Sigma_Y= \begin{bmatrix}\sigma_1^2 & \mathrm{Cov}(Y_1,Y_2)\\ \mathrm{Cov}(Y_1,Y_2)&\sigma_2^2 \end{bmatrix}
$$

The Taylor series approximations of $X=q(Y_1,Y_2)$ follow as:

$$
\begin{align*}
\mathbb{E}(X)&\approx q(\boldsymbol\mu_Y)+\frac{1}{2} \left(\frac{\partial^2 q}{\partial Y_1^2}\right)_0\sigma_1^2 +\frac{1}{2} \left(\frac{\partial^2 q}{\partial Y_2^2}\right)_0\sigma_2^2 + \left(\frac{\partial^2 q}{\partial Y_1 \partial Y_2}\right)_0\mathrm{Cov}(Y_1,Y_2)\\
\sigma_X^2 &\approx \left(\frac{\partial q}{\partial Y_1}\right)_0^2\sigma_1^2 + \left(\frac{\partial q}{\partial Y_2}\right)_0^2\sigma_2^2 + 2\left(\frac{\partial q}{\partial Y_1}\right)_0\left(\frac{\partial q}{\partial Y_2}\right)_0\mathrm{Cov}(Y_1,Y_2)
\end{align*}
$$

These are thus the mean and variance propagation laws for a function of two random variables. Pay attention to the $\approx$-sign.

If $Y_1$ and $Y_2$ are independent, we have that $\mathrm{Cov}(Y_1,Y_2)=0$, such that the last term in both equations disappears.


:::{card} Exercise mathematical pendulum

We will measure the period on one oscillation $T$ of a pendulum, and also the length $L$ of the pendulum. Both measurements are affected by random errors, and therefore the 'calculated' gravitational acceleration $G$ is a function of two random variables:

$G=q(L,T)= 4\pi^2 \frac{L}{T^2}$ 

Apply the mean and variance propagation laws to approximate the mean and variance of $G$ given that the expectations 
$\mathbb{E}(L)= \mu_L$ and $\mathbb{E}(T)= \mu_T$, as well as the variances $\sigma^2_L$ and $\sigma^2_T$ are known, and the covariance $\mathrm{Cov}(L,T)=0$.

```{admonition} Solution
:class: tip, dropdown
First determine the first- and second-order partial derivatives of the function $q(L,T)$ to obtain:

$$
\mathbb{E}(X)\approx 4\pi^2 \frac{\mu_L}{\mu_T^2} + 12\pi^2 \frac{\mu_L}{\mu_T^4}\sigma_T^2
$$


$$
\sigma^2_G \approx 16\pi^4\frac{1}{\mu_T^4}\sigma_L^2 +64\pi^4 \frac{\mu_L^2}{\mu_T^6}\sigma_T^2
$$

```
:::

:::{card} Exercise moment of inertia
<iframe src="https://tudelft.h5p.com/content/1292060624442937017/embed" aria-label="Quiz_inertia" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>
:::


## Functions of $n$ random variables
The propagation laws for functions of $n$ random variables are as follows:

$$
\mathbb{E}(X)\approx q(\boldsymbol\mu_Y)+\frac{1}{2} \sum_{i=1}^{n}\left(\frac{\partial^2 q}{\partial Y_i^2}\right)_0\sigma_i^2 + \frac{1}{2} \sum_{i=1}^{n}\sum_{j=1,j\neq i}^{n} \left(\frac{\partial^2 q}{\partial Y_i \partial Y_j}\right)_0\mathrm{Cov}(Y_i,Y_j)
$$

$$
\sigma_X^2 \approx \sum_{i=1}^{n}\left(\frac{\partial q}{\partial Y_i}\right)_0^2\sigma_i^2  + \sum_{i=1}^{n}\sum_{j=1,j\neq i}^{n}\left(\frac{\partial q}{\partial Y_i}\right)_0\left(\frac{\partial q}{\partial Y_j}\right)_0\mathrm{Cov}(Y_i,Y_j)
$$

:::{card} Exercises wind load
We have the following equation, corresponding to the wind loading equation $F$, 

$$
F=A \cdot P \cdot C_d
$$

Assume $A$, $P$, and $C_d$ are independent random variables.

What is the covariance matrix of the random vector $\mathbf{Y}=[A, P, C_d]^T$? 

```{admonition} Solution
:class: tip, dropdown

$$
\boldsymbol\Sigma_Y =\begin{bmatrix}\sigma^2_A & 0 & 0\\ 0& \sigma^2_P &0 \\ 0 & 0 & \sigma^2_{C_d}\end{bmatrix}
$$

```

What is the approximation of the mean $\mu_F$?

```{admonition} Solution
:class: tip, dropdown

$$
\mu_F \approx q(\mu_A ,\mu_P, \mu_{C_d}) = \mu_A \mu_P \mu_{C_d}
$$

(second-order partial derivatives are all 0, and also the covariances are all 0)

```

What is the approximation of $\sigma^2_F$?

```{admonition} Solution
:class: tip, dropdown

$$
\sigma^2_F \approx \left(\mu_P \cdot \mu_{C_d} \cdot \sigma_A\right)^2 + \left(\mu_A \cdot \mu_{C_d} \cdot \sigma_P\right)^2+ \left(\mu_A \cdot \mu_P \cdot \sigma_{C_d}\right)^2
$$

```
:::

:::{card} Exercise evaporation
The evaporation $Q$ is given as function of net radiation $R_n$, ground heat flux $G$ and Bowen ratio $B$:

$$
Q=\frac{R_n-G}{1-B}
$$

Assume that the random variables $R_n$, $G$, $B$ are independent.

What is the approximation of $\sigma^2_Q$:

```{admonition} Solution
:class: tip, dropdown

$$
\sigma^2_Q \approx \frac{1}{1-2\mu_B+\mu_B^2}\cdot(\sigma^2_{R_n}+\sigma^2_{G})+\left(\frac{\mu_{R_n}-\mu_G}{(1-\mu_B)^2}\right)^2\sigma^2_B
$$
```
:::

## Video

In this video the functions of $n$ random variables is discussed, as well as the [linear propagation laws]((01_LinearProp)). 

```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/sRkjvpHTrBw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

% START-CREDIT
% source: uncertainty_propagation
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Sandra Verhagen and Lotfi Massarweh. {ref}`Find out more here <uncertainty_propagation_credit>`.
```
% END-CREDIT
