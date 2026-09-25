# System of linear equations
Vectors and matrices play an important role in describing and solving systems of linear equations. Let a linear system of $m$ equations in $n$ unknown parameters $x_{i}$, $i=1, \ldots, n$, be given as

$$
\begin{array}{ccc} y_{1} & = & a_{11}x_{1}+a_{12}x_{2}+\ldots + a_{1n}x_{n} \\ y_{2} & = & a_{21}x_{1}+a_{22}x_{2}+\ldots + a_{2n}x_{n} \\ \vdots & & \vdots \\ y_{m} & = & a_{m1}x_{1}+a_{m2}x_{2}+\ldots + a_{mn}x_{n} \end{array} 
$$

This system of linear equations can be written in a matrix form as:

$$ 
\begin{bmatrix} y_1\\ y_2 \\ \vdots \\ y_m \end{bmatrix}= \begin{bmatrix} a_{11}&a_{12}&\dots&a_{1n}\\a_{21}&a_{22}&\dots&a_{2n} \\ \vdots&\vdots&\vdots&\vdots \\ a_{m1}&a_{m2}&\dots&a_{mn} \end{bmatrix} \begin{bmatrix} x_1\\ x_2 \\ \vdots \\ x_n \end{bmatrix}
$$

By introducing  

$$
\mathrm{y}=\begin{bmatrix} y_1\\ y_2 \\ \vdots \\ y_m \end{bmatrix},  ~  \mathrm{A}=\begin{bmatrix} a_{11}&a_{12}&\dots&a_{1n}\\a_{21}&a_{22}&\dots&a_{2n} \\ \vdots&\vdots&\vdots&\vdots \\ a_{m1}&a_{m2}&\dots&a_{mn} \end{bmatrix}, ~ \mathrm{x}=\begin{bmatrix} x_1\\ x_2 \\ \vdots \\ x_n \end{bmatrix},
$$ 

the linear system can be written in the compact matrix form $\mathrm{y} = \mathrm{A} \mathrm{x}$.

Note that the right-hand side of the system $\mathrm{y} = \mathrm{A} \mathrm{x}$ can be re-written as the linear combinations of the column vectors of $\mathrm{A}$:

$$
\mathrm{A}\mathrm{x}=\begin{bmatrix} a_{11}\\a_{21}\\ \vdots \\ a_{m1} \end{bmatrix}x_1+\begin{bmatrix} a_{12}\\a_{22}\\ \vdots \\ a_{m2} \end{bmatrix}x_2 + \dots +\begin{bmatrix} a_{1n}\\a_{2n}\\ \vdots \\ a_{mn} \end{bmatrix}x_n.
$$

The linear system of equations is solved, once it is known which linear combination(s) of the columns of $\mathrm{A}$ produces $\mathrm{y}$.

Example: Assume the following system of three equations with two unknowns:

$$
1 =x_1-x_2\\
-1=x_1-3x_2\\
3 =x_1+x_2
$$

These three equations can be written in a matrix form as

$$
\begin{bmatrix} 1\\-1\\3 \end{bmatrix} = \begin{bmatrix} 1&-1\\1&-3\\1&1 \end{bmatrix} \begin{bmatrix} x_1\\x_2 \end{bmatrix}
$$

The solution of this system is $x_1=2$ and $x_2=1$. We can see that the particular linear combination of columns of $\mathrm{A}$ using $x_1=2$ and $x_2=1$ produces the vector $\begin{bmatrix} 1\\-1\\3 \end{bmatrix}$ :  

$$
\begin{bmatrix} 1\\1\\1 \end{bmatrix}2 + \begin{bmatrix} -1\\-3\\1 \end{bmatrix}1=\begin{bmatrix} 1\\-1\\3 \end{bmatrix}.
$$

(LinearSystems)=
## Properties of linear systems of equations
Consider a linear system of $m$ equations in $n$ unknowns:

$$ \begin{bmatrix} y_1\\ y_2 \\ \vdots \\ y_m \end{bmatrix}= \begin{bmatrix} a_{11}&a_{12}&\dots&a_{1n}\\a_{21}&a_{22}&\dots&a_{2n} \\ \vdots&\vdots&\vdots&\vdots \\ a_{m1}&a_{m2}&\dots&a_{mn} \end{bmatrix} \begin{bmatrix} x_1\\ x_2 \\ \vdots \\ x_n \end{bmatrix}$$

In compact form this is written as $\mathrm{y} = \mathrm{A}\mathrm{x}$.

Such a system may or may not have a solution, and if a solution exists, this solution may or may not be unique.

(PM_consistent)=
## Consistent systems: at least one solution exists

If a solution exists, the system of equations is called consistent. A solution exists if and only if $y$ can be written as a linear combination of the column vectors of matrix $\mathrm{A}$:

$$\mathrm{y}=\begin{bmatrix} a_{11}\\a_{21}\\ \vdots \\ a_{m1} \end{bmatrix}x_1+\begin{bmatrix} a_{12}\\a_{22}\\ \vdots \\ a_{m2} \end{bmatrix}x_2 + \dots +\begin{bmatrix} a_{1n}\\a_{2n}\\ \vdots \\ a_{mn} \end{bmatrix}x_n$$ 

In that case $\mathrm{y}$ is an element of the range space of $\mathrm{A}$: $\mathrm{y} \in \mathcal{R}(\mathrm{A})$.

For a consistent system of equations it is always possible to find a solution $x$ such that $\mathrm{y}=\mathrm{A}\mathrm{x}$. If it is not possible to find a solution, the system is called inconsistent.

### Consistency is guaranteed if $\text{rank}(\mathrm{A}) = m$

Explanation: $ \mathrm{y} \in \mathbb{R}^{m}$ and the system is consistent if  $ \mathrm{y} \in \mathcal{R}(\mathrm{A}) $, hence consistency is guaranteed if $\mathcal{R}(\mathrm{A})=\mathbb{R}^{m}$. This means that the columns of $\mathrm{A}$ must span the complete space of reals $\mathbb{R}^{m}$, which is true if $\text{rank}(\mathrm{A})  = m$.

If $\text{rank}(\mathrm{A}) < m$, the system may or may not be consistent, this depends then on the actual entries of the vector $\mathrm{y}$.

## Unique solution

A consistent system has a unique solution if and only if the column vectors of matrix $\mathrm{A}$ are independent, i.e. if $ \text{rank}(\mathrm{A}) = n$.

This can be seen as follows: assume that $\mathrm{x}$ and $\mathrm{x}' \neq \mathrm{x}$ are two different solutions. Then $\mathrm{A}\mathrm{x}=\mathrm{A}\mathrm{x}’$ or $\mathrm{A}(\mathrm{x}-\mathrm{x}')=0$. But this can only be the case if some of the column vectors of $\mathrm{A}$ are linear dependent, which contradicts the assumption of full column rank.

(determined)=
## Determined, overdetermined and underdetermined systems

A system of equations $\mathrm{y}=\mathrm{A}\mathrm{x}$ with $\text{rank}(\mathrm{A}) =m=n$ is consistent and has a unique solution: $\hat{\mathrm{x}} = \mathrm{A}^{-1}\mathrm{y}$. Such a system is called *determined*.

A system is *underdetermined* if $\text{rank}(\mathrm{A})  < n$, i.e. if it does not have a unique solution.

A system is *overdetermined* if $\text{rank}(\mathrm{A})  < m$, i.e. the system may or may not be consistent.

(redundancy)=
## Redundancy

The redundancy of a system of equations is equal to $m - \text{rank}(\mathrm{A})$.

If we restrict ourselves to systems of observation equations that are of full column rank: $\text{rank}(\mathrm{A}) = n $, the system can either be

*Determined systems*: $\text{rank}(\mathrm{A}) =n =m$, the redundancy is equal to 0

*Overdetermined systems*: $\text{rank}(\mathrm{A}) =n < m$, the redundancy is equal to $m-n>0$




