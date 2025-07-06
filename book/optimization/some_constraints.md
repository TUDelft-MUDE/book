# Some constraints that take advantage of integer/binary variables

At most two of the projects 1, 2, 3, 4 and 5 can be done:

$$x_1+x_2+x_3+x_4+x_5\leq 2$$

If project 1 is done then also project 2 is done:

$$x_2\geq x_1$$

Restrict the variable $x_i$ to have just one of a given set of integers {2,3,5,7} $\to$ let $y_1$,$y_2$,$y_3$,$y_4$ be binary, and add the constraints:

$$\begin{cases}x_i=2y_1+3y_2+5y_3+7y_4\\ y_1+y_2+y_3+y_4=1\end{cases}$$

## Either-or constraints

Satisfy only one of these two constraints depending on something else in the model:

$$\begin{cases}3x_1+5x_2\leq 7\\ 2x_1+2x_2\leq 4\end{cases}$$

Replace with the following two constraints:

$$3x_1+5x_2\leq 7+My\\ 2x_1+2x_2\leq 4+M(1-y)$$

where $y$ is a binary variable and M is sufficiently large. When $y$ is 1 the second constraint is active and the first is relaxed ($\leq$ big number), when $y$ is 0, the inverse happens.

If $x_1$ happens (it has the value 1) then $x_2$ cannot happen and vice-versa. Both can be zero as well meaning both will not happen, as $x_1+x_2\leq 1$.

## Discontinuous variables

If you want to impose that in some situations $x$ can only be defined as:

$$x=0\text{ or } l\leq x\leq u$$

Introduce the binary variable $y$ and add the following constraints:

$$\begin{gather*}x\leq uy\\ x\geq ly\end{gather*}$$

In this way when $y$ is 0, $x$ is zero, and when it is 1 then $x$ is between $u$ and $l$.

## The product of two binary variables

As you know, in linear programming you cannot multiply two variables but this does not mean that you cannot use some constraints to produce that product. The product $x_1x_2$ of two binary variables $x_1$ and $x_2$ can be replaced by additional binary variable $y$ by adding the following constraints:

$$\begin{gather*}y\leq x_1\\ y\leq x_2\\ y\geq x_2-M(1-x_1)\end{gather*}$$

with $M$ sufficiently large. The $y$ variable will be the result of multiplying $x_1$ for $x_2$.

## The product of a binary and a continuous variable

The product $x_1x_2$ of the binary variable $x_1$ and the continuous variable $x_2$ with $0\leq x_2\leq u$ can be replaced by an additional continuous variable $y$ by adding the following constraints:

$$\begin{cases}y\leq ux_1\\ y\leq x_2\\ y\geq x_2-u(1-x_1)\\ y\geq 0\end{cases}$$

$y$ is obviously the continuous variable you want to get.

% START-CREDIT
% source: optimization
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Gonçalo Homem de Almeida Correia, Maria Nogal Macho, Jie Gao and Bahman Ahmadi. `{ref}`Find out more here <optimization_credit>`.
```
% END-CREDIT