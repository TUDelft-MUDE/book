# TSA Exercises

## Exercises

MMMMM from 231129 word doc from Alireza: move these to the right page, or keep all here? If on other page, put under a second-level heading, as above

:::{card} Exercise 1

A time series exhibits a linear regression model $Y(t)=y_0 + rt + \epsilon(t)$. The measurements have also been taken at a measurement frequency of 10 Hz, producing epochs of $t=0.1,0.2, \dots,100$ seconds, so $m=1000$. Later an offset was also detected at epoch 260 using statistical hypothesis testing. For the linear model $Y=\mathrm{Ax}+\epsilon$, establish an appropriate design matrix that can capture all the above effects.

```{admonition} Solution
:class: tip, dropdown

In the linear regression case, the design matrix consists of two columns, one for the unknown $y_0$ (a column on ones), and the other for $r$ (a column of time, $t$). Due to the presence of an offset, the mathematical model should be modified to:

$$
Y(t) = y_0 =rt +o_k u_k(t) + \epsilon(t)
$$

where $u_k(t)$ is the Heaviside step function:

$$
u_k(t) = 
\begin{cases}
0, & \textrm{if} & t<t_k=26 \\
1, & \textrm{if} & t\geq t_k=26
\end{cases}
$$

and $o_k$ is the magnitude of the offset. This means that we have to add a third column to the design matrix having zeros before the epoch 260, and ones afterwards. Since epoch 260 corresponds to $t=26$ s (noting that we have 10 Hz data), in $\mathrm{A}$ we begin to have 1's in that row:

$$
\mathrm{A} = 
\begin{bmatrix}
1 & t_1 & 0 \\
\vdots & \vdots & \vdots\\
1 & t_{259} & 1\\
1 & t_{260} & 1\\
\vdots & \vdots & \vdots \\
1 & t_{1000} & 1 \\
\end{bmatrix}
= 
\begin{bmatrix}
1 & 0.1 & 0 \\
\vdots & \vdots & \vdots\\
1 & 25.9 & 0 \\
1 & 26 & 1\\
\vdots & \vdots & \vdots \\
1 & 100 & 1 \\
\end{bmatrix}
$$
```
:::

:::{card} Exercise 2

In a zero-mean first order autoregressive process, abbreviated as AR(1), we have $m=3$ observations, $\beta=0.8$, and the generated white noise errors are $\epsilon_t = [\epsilon_1,\, \epsilon_2,\, \epsilon_3]=[1,\, 2,\, -1]$. What is the generated AR(1) process $Y_t = [Y_1,\, Y_2,\, Y_3]$?

a. $Y_t = \begin{bmatrix}1 & 2.8 & 1.24\end{bmatrix}^T$  
b. $Y_t = \begin{bmatrix} 0 & 2 & 0.6 \end{bmatrix}^T$  
c. $Y_t = \begin{bmatrix} 1 & 2 & -1 \end{bmatrix}^T$  

```{admonition} Solution
:class: tip, dropdown

The correct answer is **a**. The AR(1) process can be initialized as $Y_1=\epsilon_1=1$. The next values can be obtained through:

$$
Y_t = \beta Y_{t-1} + \epsilon_t
$$

Giving $Y_2=0.8 Y_1 + \epsilon_2 = 0.8\cdot 1 + 2 = 2.8$ and $Y_3=0.8 Y_2 + \epsilon_3 = 0.8\cdot 2.8 - 1= 1.24$, so we have:

$$
Y_t = 
\begin{bmatrix}1 & 2.8 & 1.24\end{bmatrix}^T 
$$

```
:::

:::{card} Exercise 3

A zero-mean stationary noise process consists of $m=5$ observations:

$$
Y = \begin{bmatrix} 2 & 1 & 0 & -1 & -2 \end{bmatrix}^T
$$

What is the _least-squares estimate_ of the normalized ACF at $\tau=1$; so compute $\hat{\rho}_{1}$?

```{admonition} Solution
:class: tip, dropdown

The normalized auto-covariance function (ACF) can be estimated from the auto-covariance function as:

$$
\hat{\rho}_\tau=\frac{\hat{C}_\tau}{\hat{C}_0}, \qquad \tau=0, \dots , m-1
$$

where the least-squares estimate of auto-covariance function is:

$$
\hat{C}_\tau
= \frac{\sum_{i=1}^{m-\tau}(Y_i - \mu)(Y_{i+\tau} - \mu)}{m-\tau},
\qquad \tau=0, \dots , m-1
$$

For our application we have $\mu_y=0$, as we deal with a zero-mean process. We have to compute $\hat{\sigma}(0)$ and $\hat{\sigma}(1)$ given as:

$$
\hat{C}_0
= \frac{\sum_{i=1}^{m} Y_i^2}{m-0}
= \frac{10}{5} = 2
$$

And 

$$
\hat{C}_1
= \frac{\sum_{i=1}^{m} Y_i Y_{i+1}}{m-1}
= \frac{2(1) + 1(0) + 0(-1) + (-1)(-2)}{5 - 1}
= \frac{2 + 0 + 0 + 2}{4}
= 1
$$

Giving

$$
\hat{\rho}_1
= \frac{1}{2}
$$

```

:::

:::{card} Exercise 4

The linear model of observation equations of a time series measured at $t=\begin{bmatrix}1 & 2 &3 & 4\end{bmatrix}^T$ is as $Y(t)=y_0+rt+\epsilon(t)$, where the errors $\epsilon(t)\sim \textbf{N}(0,1)$ contain independent standard normal errors. The observations are given as $Y=\begin{bmatrix}0.1 & 1 2.2& 3\end{bmatrix}^T$. Estimate the rate $r$ and its standard deviation using BLUE. In other words, find $\hat{r}$ and $\sigma_{\hat{r}}$.

```{admonition} Solution
:class: tip, dropdown

Based on the information provided, the design matrix, the unknown parameters and the covariance matrix of observations are as follows:

$$
\mathrm{A} =
\begin{bmatrix}
1&1\\1&2\\1&3\\1&4\\
\end{bmatrix},
\quad
x = 
\begin{bmatrix}
y_0\\r\\
\end{bmatrix},
\quad
\Sigma_{Y} = 
\begin{bmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1\\
\end{bmatrix}
= I_4,
$$

This gives the BLUE of $x$ as

$$
\hat{X} 
= \bigl(A^T \Sigma_{Y}^{-1} A\bigr)^{-1} A^T \Sigma_{Y}^{-1}Y
= (A^TA)^{-1}A^TY
$$

with the variance matrix of 

$$
\Sigma_{\hat{X}}
= \bigl(A^T \Sigma_{Y}^{-1} A\bigr)^{-1}
= (A^TA)^{-1}
$$

Working out the above formulas gives

$$
\Sigma_{\hat{X}} = (A^TA)^{-1}
= \Biggl(
\begin{bmatrix}
1&1&1&1\\1&2&3&4
\end{bmatrix}
\begin{bmatrix}
1&1\\1&2\\1&3\\1&4\\
\end{bmatrix}
\Biggr)^{-1}
= 
\begin{bmatrix}
4&10\\10&30
\end{bmatrix}^{-1}
= \frac{1}{10}
\begin{bmatrix}
15&-5\\-5&2\\
\end{bmatrix}^{-1}
$$

And

$$
\hat{X} = (A^TA)^{-1}A^TY
= \frac{1}{10}
\begin{bmatrix}
15 & -5 \\ -5 & 2 \\
\end{bmatrix}
\begin{bmatrix}
1&1&1&1\\1&2&3&4\\
\end{bmatrix}
\begin{bmatrix}
0.1\\1\\2.2\\3\\
\end{bmatrix}
$$

or

$$
\hat{X} = (A^TA)^{-1}A^TY
= \frac{1}{10}
\begin{bmatrix}
15 & -5 \\ -5 & 2 \\
\end{bmatrix}
\begin{bmatrix}
6.3\\20.7
\end{bmatrix}
= \frac{1}{10}
\begin{bmatrix}
-9\\9.9
\end{bmatrix}
= 
\begin{bmatrix}
-0.9\\0..99
\end{bmatrix}
$$

We therefore have

$$
\hat{r} = 0.99,
\quad \textrm{and} \quad
\sigma_{\hat{r}} = \sqrt{\Sigma_{\hat{X}}(2.2)}=\sqrt{0.2}=0.458
$$

or

$$
\hat{r}\pm \sigma_{\hat{r}} = 0.99 \pm 0.45
$$

```
:::

:::{card} Exercise 5

For the stationary AR(2) process, calculate the ACF at lag 1. In other words, calculate $\rho_1$.

```{admonition} Solution
:class: tip, dropdown

For the AR($p$) process we know that $\mathbb{E}(Y_t)=0$, and $Var(Y_t)=\sigma^2$ ($\forall t$), and

$$Y_t = \beta_1Y_{t-1}+\beta_2Y_{t-2}+\epsilon_t=
\begin{bmatrix}\beta_1 & \beta_2 & 1\end{bmatrix}\begin{bmatrix}Y_{t-1} \\ Y_{t-2} \\ \epsilon_t\end{bmatrix}$$

Applying the variance propagation law gives:

$$Var(Y_t) = \begin{bmatrix}\beta_1 & \beta_2 & 1\end{bmatrix} \begin{bmatrix} \sigma^2 & 0 & 0 \\ 0 & \sigma^2 & 0\\ 0&0& \sigma_{\epsilon}^2\end{bmatrix}\begin{bmatrix}\beta_1 \\\beta_2 \\ 1\end{bmatrix} = \sigma^2(\beta_1^2 + \beta_2^2)$$

Therefore, for AR(2):

$$
Var(Y_t)=\sigma^2=\sigma^2(\beta_1^2 + \beta_2^2)+\sigma_{\epsilon}^2
$$

or

$$
\sigma^2 (1 - \beta_1^2 - \beta_2^2)
= \sigma_{\epsilon}^2
$$

which is a condition for the AR(2) process to be stationary. To compute the autocovariance function at lag 1, $c_1$, we need to compute the covariance between $Y_{t-1}$ and $Y_t$, which is given as

$$
\begin{align*}
c_1 &= \mathbb{E}(Y_{t-1}Y_t)
= \mathbb{E}\left(Y_{t-1}
(\beta_1 Y_{t-1} + \beta_2 Y_{t-2} + \epsilon_t)
\right)
\\
&= \beta_1 \mathbb{E}(Y_{t-1}^2)
+ \beta_2 \mathbb{E}(Y_{t-2}Y_{t-1})
+ \mathbb{E}(Y_{t-1}\epsilon_t)\\
&= \beta_1 \sigma^2
+ \beta_2 c_1
\end{align*}$$


which gives

$$
\beta_1 \sigma^2 = c_1(1-\beta_2)
$$

or, because $\rho_1=c_1/\sigma^2$:

$$
\rho_1=\frac{\beta_1}{1-\beta_2}
$$

```
:::

:::{card} Exercise 6

Consider a random process time series as:

$$
Y_t
= U \cos (\theta t) + V \sin (\theta t)
$$

where $U$ and $V$ are two uncorrelated random variables with zero means, and unit variances and $\theta$ is a deterministic value in the interval $\theta \in [-\pi, \pi]$. Show that this noise process is stationary.

```{admonition} Solution
:class: tip, dropdown

Because $\mathbb{E}(U)=\mathbb{E}(V)=0$, it simply follows that 

$$
\mathbb{E}(Y_t)=0
$$

For a given $\tau$, the covariance between $Y_t$ and $Y_{t+\tau}$ is obtained as:

$$
\begin{align*}
Cov(Y_t, Y_{t+\tau})
&= \mathbb{E}(Y_tY_{t+\tau}) - \mathbb{E}(Y_t)\mathbb{E}(Y_{t+\tau})
= \mathbb{E}(Y_t Y_{t+\tau})\\
&= \mathbb{E}
\biggl(
    \bigl[ U \cos(\theta t) + V \sin(\theta t) \bigr]
    \bigl[ U \cos(\theta t + \theta \tau)
         + V \sin(\theta t + \theta \tau) \bigr]
\biggr)
\end{align*}
$$

The multiplication consists of four terms in which the terms $U^2$, $V^2$, $UV$ and $VU$ appear. Because the two random variables $U$ and $V$ are uncorrelated with zero means and unit variances, it follows that:

$$
\mathbb{E}(U^2) = \mathbb{E}(V^2) = 1
\quad \mathrm{and} \quad
\mathbb{E}(UV) = \mathbb{E}(VU) = 0
$$

This, with the previous equations, gives:

$$
Cov(Y_t, Y_{t+\tau})
= \cos(\theta t) \cos(\theta t + \theta \tau)
+ \sin(\theta t) \sin(\theta t + \theta \tau)
$$

Using the identity $\cos(a-b)=\cos(a)\cos(b)+\sin(a)\sin(b)$, it follows:

$$
Cov(Y_t, Y_{t+\tau})
= \cos(\theta t + \theta \tau - \theta t)
= \cos(\theta \tau)
$$

Which is a function of $\tau$, but not a function of time $t$. This shows that the random process is stationary.

```
:::
