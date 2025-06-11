# Augmented form of a mathematical program

In the augmented form of a mathematical program:

* All the constraints must be equations (equality sign)
* The independent term must always be positive
* All the variables must be positive defined
* The objective function can be of type maximization or minimization

## Augmented form of a LP problem

Let us take a look, considering an objective function given by:

$$\text{Max (Min) }Z=c_1x_1+c_2x_2+...+c_nx_n$$

subject to:

$$\begin{cases}a_{11}x_1+a_{12}x_2+...+a_{1n}x_n=b_1\\ a_{21}x_1+a_{22}x_2+...+a_{2n}x_n=b_2\\...\\a_{m1}x_1+a_{m2}x_2+...+a_{mn}x_n=b_m\\ x_1,x_2,...,x_n\geq 0\\ b_1,b_2,...,b_m\geq 0\end{cases}$$

As you can see, all the constraints here presented are equations, all the decision variables $x_i$ are positive and all the independent coefficients $b_i$ are positive as well. Using a more condensed mathematical notation:

$$\text{Max (Min) }Z=\sum_jc_jx_j$$

such that:

$$\sum_{j=1}^na_{ij}x_j=b_i\hspace{5px}(i=1,2,...,m)$$

and with $x_j\geq 0$ $(j=1,2,...,n)$ and $b_i\geq 0$ $(i=1,2,...,m)$. $n$ here is being used to represent the number of variables and $m$ for the number of constraints.

### But what if you have an inequality as a constraint?

To solve those kind of situations you introduce a **slack variable**, let us say $s_1$, that will convert your constraint into an equality:

$$a_{11}x_1+a_{12}x_2+...+a_{1n}x_n\leq b_1 \to \underbrace{a_{11}x_1+a_{12}x_2+...+a_{1n}x_n}_{\text{consumption of a resource}}+\overbrace{s_1}^{\text{available resources which were not consumed}}=\underbrace{b_1}_{\text{available resources}}$$

If, on the other hand, instead of $\leq$ we have an inequality dictated by $\geq$, then we write:

$$a_{11}x_1+a_{12}x_2+...+a_{1n}x_n\geq b_1 \to \underbrace{a_{11}x_1+a_{12}x_2+...+a_{1n}x_n}_{\text{expression of consumption}}-\overbrace{s_1}^{\text{resources consumed above the minimum limit (surplus variable)}}=\underbrace{b_1}_{\text{minimum number to consume}}$$

### But what if we have negative independent coefficients?

Transform the negative independent coefficients into positive ones:

$$a_{11}x_1+a_{12}x_2+...+a_{1n}x_n=-b_1 \to -a_{11}x_1-a_{12}x_2-...-a_{1n}x_n=b_1$$

### And what if we have variables that can take negative values?

$$x_2\leq 0 \to x_2=-x'_2 (x_2'\geq 0)$$

And our equation could be written as:

$$a_{11}x_1+a_{12}x_2+...+a_{1n}x_n\leq b_1 \to a_{11}x_1-a_{12}x'_2+...+a_{1n}x_n\leq b_1$$

```{note}

When one solves the problem, one must not forget to get the original value of $x_2$ in the end by multiplying $x'_2$ by $-1$

```

### And, finally, what if we have continuous variables defined in ALL the domain?

$$x_2\in\mathbb{R}\to x_2=(x_2'-x_2'')$$

and, in this case, both $x_2'$ and $x_2''$ will be $\geq 0$. Replacing in our equation would give:

$$a_{11}x_1+a_{12}x_2+...+a_{1n}x_n\leq b_1 \to a_{11}x_1+a_{12}x'_2-a_{12}x_2''+...+a_{1n}x_n\leq b_1$$

```{note}

When one solves the problem, one must not forget to get the original value of $x_2$ in the end by subtracting $x''_2$ to $x'_2$

```

## Example: Getting the augmented form of an LP problem

Consider the optimization problem defined by:

$$\text{Max }Z=2x_1+6x_2+13x_3+7x_4$$

such that:

$$\begin{cases}3x_1+4x_2+12x_3\geq 300\\ 8x_1+6x_2-x_4\leq 220\\ 6x_1+5x_2+3x_3\leq 150\\ x_1,x_3,x_4\geq 0\\ x_2\leq 0\end{cases}$$

We have a problem with the last condition, as we should have $x_2\geq 0$. Therefore, we introduce a new variable given by $x_2'=-x_2$, and then we write:

$$\text{Max }Z=2x_1-6x'_2+13x_3+7x_4$$

with:

$$\begin{cases}3x_1-4x'_2+12x_3-s_1 = 300\\ 8x_1-6x'_2-x_4+s_2 = 220\\ 6x_1-5x'_2+3x_3+s_3 = 150\\ x_1,x'_2,x_3,x_4\geq 0\\ s_1,s_2,s_3\geq 0\end{cases}$$

And the problem is transformed in its augmented form and ready to be used in the SIMPLEX method!
