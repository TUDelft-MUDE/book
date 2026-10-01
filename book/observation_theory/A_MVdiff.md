# Multivariate differentiation

(PM_gradient)=
## Gradient vector
For a multivariate function $f(\mathrm{x})$  where $\mathrm{x}=\begin{bmatrix} x_1\\ \vdots\\x_n \end{bmatrix}$, the vector with enteries as partial derivatives with respect to $x_1,x_2,\dots,$ and $x_n$ is called the gradient vector and it is denoted as:

$$
\partial_{\mathrm{x}} f= \begin{bmatrix} \partial f/\partial x_1\\ \vdots\\ \partial f/\partial x_n \end{bmatrix}.
$$

For example, let's assume  $\mathrm{x}=\begin{bmatrix} x_1\\ x_2\\x_3 \end{bmatrix}$ and $f(\mathrm{x})=x_1^2+3x_2+\cos(x_3)$. Then the gradient vector of $f(\mathrm{x})$ is:

$$
\partial_{\mathrm{x}} f= \begin{bmatrix} 2x_1\\3 \\-\sin(x_3)  \end{bmatrix}.
$$

## Gradient of linear functions
If $\mathrm{b}$ and $\mathrm{x}$ are the column vectors with the same size, the gradient of $f(\mathrm{x})=\mathrm{b}^T\mathrm{x}=\mathrm{x}^T\mathrm{b}$ with respect to $\mathrm{x}$  is derived as:

$$
\partial_{\mathrm{x}} f=\mathrm{b}. 
$$

If $\mathrm{b}$ is a $m\times1$ vector, $\mathrm{x}$ is a $n\times1$, and $\mathrm{A}$ is a matrix of size $m\times n$, the gradient of $f(\mathrm{x})=\mathrm{b}^T\mathrm{A}\mathrm{x}=\mathrm{x}^T\mathrm{A}^T\mathrm{b}$ with respect to $\mathrm{A}$  is derived as:

$$
\partial_{\mathrm{x}} f=\mathrm{A}^T\mathrm{b}.
$$

## Gradient of quadratic functions
If $\mathrm{x}$ is the column vector of size $n\times 1$, and $\mathrm{B}$ is an square matrix of size $n\times n$,  the gradient of $f(\mathrm{x})=\mathrm{x}^T\mathrm{B}\mathrm{x}=\mathrm{x}^T\mathrm{B}^T\mathrm{x}$  with respect to $\mathrm{x}$  is derived as:

$$
\partial_{\mathrm{x}} f=(\mathrm{B}+\mathrm{B}^T)\mathrm{x}. 
$$

Note that if $\mathrm{B}$ is a symmetric matrix, then $\mathrm{B}^T=\mathrm{B}$, and so the gradient of $f(\mathrm{x})=\mathrm{x}^T\mathrm{B}\mathrm{x}=\mathrm{x}^T\mathrm{B}^T\mathrm{x}$  with respect to $\mathrm{x}$  is derived as: 

$$
\partial_{\mathrm{x}} f=2\mathrm{Bx}.
$$

(PM_jacobian)=
## Jacobian matrix
Assume $m$ number of different multivariate functions as  $f_1(\mathrm{x}),f_2(\mathrm{x}),\dots, f_m(\mathrm{x})$, where $\mathrm{x}=\begin{bmatrix} x_1\\ \vdots\\x_n \end{bmatrix}$. If we collect all the $f_i(\mathrm{x})$ functions in a column vector $F(\mathrm{x})$ as

$$
F(\mathrm{x})=\begin{bmatrix} f_1(\mathrm{x})\\ \vdots\\f_m(\mathrm{x}) \end{bmatrix},
$$

$F(\mathrm{x})$ is itself a $m$-vector function of an $n$-vector $\mathrm{x}$. For such a vector multivariate function, the $m\times n$ matrix of partial derivatives $\partial f_{i}/ \partial x_{j}$, denoted as $J_{\mathrm{x}}$, is called  Jacobian matrix of $F$ defined as:

$$ 
J_{\mathrm{x}}=\partial_{\mathrm{x}^{T}} F =\left[\begin{array}{ccc}\partial f_{1} / \partial x_{1} & \ldots & \partial f_{1}/ \partial x_{n} \\\partial f_{2} / \partial x_{1} & \ldots & \partial f_{2}/ \partial x_{n} \\ \vdots & & \vdots \\ \partial f_{m} / \partial x_{1} & \ldots & \partial f_{m}/ \partial x_{n}\end{array}\right]. 
$$

For example, let $\mathrm{x}=\begin{bmatrix} x_1\\ x_2\\x_3 \end{bmatrix}$ and  $ F(\mathrm{x})=\begin{bmatrix} x_1+x_2+x_3 \\ x_1^2+2x_2 \\ x_1^2+x_2^3+\cos(x_3)\end{bmatrix} $. Then the Jacobian matrix of $F(\mathrm{x})$ is derived as:

$$ 
J_{\mathrm{x}}=\partial_{\mathrm{x}^{T}} F =\left[\begin{array}{ccc}  1& 1& 1 \\ 2x_1&2 &0  \\ 2x_1 & 3x_2^2& -\sin(x_3) \end{array}\right].
$$