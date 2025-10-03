(01_LinearProp)=
# Linear propagation of mean and covariance

On this page, we will limit ourselves to linear functions, but expand from one equation $X=q(\mathbf{Y})$ to a linear system of equations $\mathbf{X} = \mathbf{AY}+\mathbf{c}$. Then the uncertainty in $\mathbf{Y}$ needs to be propagated to a covariance matrix for $\mathbf{X}$ as well. 

## Linear function of two random variables

Consider first a linear function of two random variables

$$
X = q(\mathbf{Y})=a_1 Y_1+ a_2 Y_2 + c
$$

We can now show that $\mathbb{E}(q(\mathbf{Y}))= a_1 \mathbb{E}(Y_1)+a_2 \mathbb{E}(Y_2)+c$ using our Taylor approximations. The first-order partial derivatives namely follow as

$$
\frac{\partial q}{\partial Y_1}= a_1, \; \frac{\partial q}{\partial Y_2}= a_2
$$

and all the higher-order derivatives are zero, and consequently all higher-order terms in the Taylor series will be zero. The expectation of $q(\mathbf{Y})$ follows therefore as

$$
\mathbb{E}(q(\mathbf{Y}))= q(\mu_1,\mu_2)=a_1 \mu_1 + a_2\mu_2 + c
$$

which is exact (i.e., not an approximation anymore).

:::{card} Exercise

In a similar fashion derive the variance of $X$, which is also an exact result.

 ```{admonition} Solution
:class: tip, dropdown
First determine the first- and second-order partial derivatives of the function $q(L,T)$ to obtain:

$$
\sigma_X^2 = a_1^2 \sigma_1^2 + a_2^2 \sigma_2^2 + 2a_1 a_2 \mathrm{Cov}(Y_1,Y_2)
$$

Note that it does not depend on the deterministic constant $c$.
```
:::

## Linear system of equations of random variables 
Note that the linear function of two random variables can also be written as $q(\mathbf{Y}) = \begin{bmatrix} a_1 & a_2\end{bmatrix}\begin{bmatrix}Y_1 \\ Y_2\end{bmatrix}+c$. We will now generalize to the case where we have $m$ linear functions of $n$ variables, which can be written as a linear system of equations:

$$ 
\mathbf{X}= \begin{bmatrix} X_1\\ X_2 \\ \vdots \\ X_m \end{bmatrix}= \begin{bmatrix} a_{11}&a_{12}&\dots&a_{1n}\\a_{21}&a_{22}&\dots&a_{2n} \\ \vdots&\vdots&\vdots&\vdots \\ a_{m1}&a_{m2}&\dots&a_{mn} \end{bmatrix} \begin{bmatrix} Y_1\\ Y_2 \\ \vdots \\ Y_n \end{bmatrix} +\begin{bmatrix} c_1\\ c_2 \\ \vdots \\ c_m \end{bmatrix}=\mathbf{AY}+\mathbf{c}
$$

with known $\mathbb{E}(\mathbf{Y})$ and covariance matrix $\Sigma_Y$, and $\mathbf{c}$ a vector with deterministic variables.

The linear propagation laws of the mean and covariance matrix are given by

$$
\mathbb{E}(\mathbf{X}) = \mathbf{A}\mathbb{E}(\mathbf{Y})+\mathbf{c}
$$ 

$$
\Sigma_{X} =\mathbf{A}\Sigma_Y \mathbf{A}^T
$$

These are exact results, since for linear functions the higher-order terms of the Taylor approximation become zero and thus the approximation error is zero.

:::{card} Exercise 
Consider the linear system of equations

$$
\begin{bmatrix} X_1 \\ X_2 \end{bmatrix} =\begin{bmatrix}1&1 \\ 1&-2\end{bmatrix}\begin{bmatrix}Y_1 \\ Y_2\end{bmatrix}
$$

with 

$$
\mu_Y = \begin{bmatrix}0 \\ 0\end{bmatrix},\; \Sigma_Y= \begin{bmatrix}3&0 \\ 0&3\end{bmatrix}
$$

Apply the linear propagation laws to find $\mathbb{E}(X)=\mu_X$ and $\Sigma_X$.

 ```{admonition} Solution
:class: tip, dropdown

$$
\mu_X=\begin{bmatrix}1&1 \\ 1&-2\end{bmatrix}\begin{bmatrix}0 \\ 0\end{bmatrix}=\begin{bmatrix}0 \\ 0\end{bmatrix}
$$

$$
\Sigma_X = \begin{bmatrix}1&1 \\ 1&-2\end{bmatrix}\begin{bmatrix}3&0 \\ 0&3\end{bmatrix}\begin{bmatrix}1&1 \\ 1&-2\end{bmatrix}=\begin{bmatrix}6&-3 \\ -3&15\end{bmatrix}
$$

```
:::

:::{card} Exercise buckets of concrete

You want to measure out 1.5$l$ of concrete in a bucket, but only have a bucket of with lines indicating 5$l$, 2$l$, and 0.5$l$. These buckets are named $a$, $b$, and $c$, respectively. To achieve this you take the 5$l$ bucket, take out 2$l$ using bucket $b$, and then three times 0.5$l$ using bucket $c$: $Y_1 = V_a - V_b - 3V_c$ (with $V_i$ is the volume of bucket $i$). However, you can't read the lines on the buckets perfectly, and the variance of your pouring skills is 1/100th of the volume of the bucket. Assume the volumes to be independent.

You do something similar to achieve 4.5$l$ ($Y_2 = V_a - V_c$) and 1$l$ ($Y_3 = V_a-2V_b$). Compute the covariance matrix of $[Y_1 \ Y_2 \ Y_3]^T$.

Hint: first find the $\mathbf{A}$ matrix of the linear system $\mathbf{Y}=\mathbf{A}\cdot \mathbf{V}$.

 ```{admonition} Solution
:class: tip, dropdown

$$
\mathbf{A} = \begin{bmatrix} 1& -1& -3 \\ 1 & 0& -1\\1&-2&0 \end{bmatrix},\; \Sigma_V = \begin{bmatrix} \frac{5}{100}& 0 & 0 \\ 0 & \frac{2}{100}& 0\\0&0& \frac{0.5}{100}\end{bmatrix}
$$

$$
\begin{align*}
\Sigma_Y &= \mathbf{A}\Sigma_V\mathbf{A}^T \\
&= \begin{bmatrix} 1& -1& -3 \\ 1 & 0& -1\\1&-2&0 \end{bmatrix}\begin{bmatrix} \frac{5}{100}& 0 & 0 \\ 0 & \frac{2}{100}& 0\\0&0& \frac{0.5}{100}\end{bmatrix}\begin{bmatrix} 1& 1& 1 \\ -1 & 0& -2\\-3&-1&0 \end{bmatrix}=\frac{1}{100}\begin{bmatrix} 11.5& 6.5 & 9 \\ 6.5 & 5.5& 5\\9&5& 13\end{bmatrix}
\end{align*}
$$

```
:::

% START-CREDIT
% source: uncertainty_propagation
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Sandra Verhagen. {ref}`Find out more here <uncertainty_propagation_credit>`.
```
% END-CREDIT
