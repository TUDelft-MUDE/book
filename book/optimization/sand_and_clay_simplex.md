# SIMPLEX method

The story is told in a video. The video below has a one-to-one correspondence with this book:

```{eval-rst}
.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/S_8MsOXu60I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```


```{admonition} MUDE Exam Information
:class: tip, dropdown
For the exam, you are expected to have a clear understanding behind the Simplex method and how to do it. you will not need to do the calculations by hand in the exam or on Friday’s assignment.
```

The SIMPLEX method has been created to automate the solving of the augmented form of a linear programming problem with continuous variables. Consider the following optimization problem:

$$\text{Max }L=57x_1+60x_2$$

such that:

$$\begin{cases}8x_1+4x_2\leq 40\\ 4x_1+5x_2\leq 40\\ 50x_1+13x_2\leq 200\\ x_1,x_2\geq 0\end{cases}$$

First, you need the problem in its augmented form, i.e., with the constraints given by:

$$\begin{cases}8x_1+4x_2+s_1=40\\ 4x_1+5x_2+s_2=40\\ 50x_1+13x_2+s_3=200\\ x_1,x_2,s_1,s_2,s_3\geq 0\end{cases}$$

The feasible solution space of the problem is defined by all the constraints. We have 3 equations and 5 variables and, therefore, the solution space is not just one point. There are infinite points but just a finite number of feasible basic solutions (vertices).

A basic solution to this problem will have three variables different from zero (named basic variables), one for each constraint (ignore the domain constraints for this), and two that must be non-zero (non-basic). You will see how these match the vertices of the feasible region polygon.

From the three equations, one obvious apparent basic solution is $s_1=40$, $s_2=40$, $s_3=200$, with $x_1=0$ and $x_2=0$. A basic variable can be recognized in its contraint because it has a positive unitary coefficient in its constraint (+1) and it does not appear (has 0 coefficient) in the other constraints.

![sand_clay_1](./figs/sand_clay_1.png)

In order to search for the best solution, we should move from one system of equations to another that is equivalent to the first (it has the same solution space) but in which **another apparent basic solution comes up**.

There are two types of operations to transform the system of equations into another equivalent one:

* Multiply any equation by a positive or negative number
* Add to an equation another one which has been multiplied by any number

Graphically:

![sand_clay_2](./figs/sand_clay_2.png)

The problem is that even though this is a vertex, it is not a feasible solution - note that $s_1$ is negative!

How many basic solutions are there? We have **5 variables**, that divide into three basic variables ($x_1$, $x_2$, and $s_1$) and two non-basic ($s_2$ and $s_3$). The number of basic variables is always equal to the total number of equations (not including the domain constraints - $x_1>0$ - or the objective function). Therefore, the number of feasible and unfeasible basic solutions is given by:

$$C_n^m=\frac{n!}{m!(n-m)!}$$

where $n$ represents the number of variables and $m$ the total number of constraints. The feasible basic solutions are, therefore, given by:

![sand_clay_3](./figs/sand_clay_3.png)

We need a systematic method (algorithm) that applies changes to the system of equations going from feasible basic solution to feasible basic solutions without leaving the feasible space. This is the so-called **SIMPLEX method** (created by Dantzig in the 1950s).

---

## Augmented form

We start with the augmented form, given (as seen before) by:

$$\text{Max }L-57x_1-60x_2-0s_1-0s_2-0s_3=0$$

subject to the following constraints:

$$\begin{cases}8x_1+4x_2+s_1=40\\ 4x_1+5x_2+s_2=40\\ 50x_1+13x_2+s_3=200\\ x_1,x_2,s_1,s_2,s_3\geq 0\end{cases}$$

```{note}

The objective function must be put in the form of an equation with all the variables on the left-hand side and the independent coefficient on the right.

```

## Setting up the first table

| Basic Variables | $L$ | $x_1$ |$x_2$ | $s_1$ | $s_2$ | $s_3$ | $b$ |
| :--- | ---- |---| ---| ---| ---| ---| ---: |
| $L$ | $1$ | $-57$ | $-60$ | $0$ | $0$ | $0$ | $0$ |
| | || || | |  |
| $s_1$ | $0$ | $8$ | $4$ | $1$ | $0$ | $0$ | $40$ |
| $s_2$ | $0$ | $4$ | $5$ | $0$ | $1$ | $0$ | $40$ |
| $s_3$ | $0$ | $50$ | $13$ | $0$ | $0$ | $1$ | $200$ |

Our current solution right now sets the basic variables $[s_1,s_2,s_3]=[40,40,200]$, and the non-basic variables $[x_1,x_2]=[0,0]$. The value of the objective function in this case is $L=0$.

## Optimality condition of the SIMPLEX method

The **optimality condition** assures that it is not possible to find a better solution.

In a maximization problem, the current basic feasible solution is optimal if all the coefficients of the objective functions are positive. On the other hand, in a minimization problem, the current solution is optimal if all the coefficients of the objective function are negative.

| Basic Variables | $L$ | $x_1$ |$x_2$ | $s_1$ | $s_2$ | $s_3$ | $b$ |
| :--- | ---- |---| ---| ---| ---| ---| ---: |
| $L$ | $1$ | $-57$ (negative) | $-60$ (negative) | $0$ | $0$ | $0$ | $0$ |
| | || || | |  |
| $s_1$ | $0$ | $8$ | $4$ | $1$ | $0$ | $0$ | $40$ |
| $s_2$ | $0$ | $4$ | $5$ | $0$ | $1$ | $0$ | $40$ |
| $s_3$ | $0$ | $50$ | $13$ | $0$ | $0$ | $1$ | $200$ |

So it's not optimal

**How to go to the next table of the SIMPLEX method?**

* In a maximization problem, the variable to enter the basis (to become basic) is the one that has the most negative coefficient in the objective funcion
* In a minimization problem, the variable to enter the basis (to become basic) is the one that has the most positive coefficient in the objective function

Therefore, in our problem it will be $x_2$.

**And how to choose the variable to leave the basis?**

The variable to leave the basis is the one whose quotient between the independent coefficient of the constraint (meaning the same line) under the variable that will enter the basis is the lowest positive number including zero (this does not depend on being a maximization or minimization problem at all).

```{note}

Two special cases exist often:

* if the coefficient of the entering basic variable is zero: enter *no limit* in the minimum ratio test column. That is not a candidate.
* if the coefficient of the entering basic variable is negative: enter *no limit* in the minimum ratio test column. This is not a candidate.

```

| Basic Variables | $L$ | $x_1$ |$x_2$ (variable to enter) | $s_1$ | $s_2$ | $s_3$ | $b$ || $\Delta$|
| :--- | ---- |---| ---| ---| ---| ---|---|---| ---: |
| $L$ | $1$ | $-57$ | $-60$ (most negative coefficient) | $0$ | $0$ | $0$ | $0$ |||
| | || || | |  |||
| $s_1$ | $0$ | $8$ | $4$ | $1$ | $0$ | $0$ | $40$ ||$10$|
| $s_2$ (variable to leave) | $0$ | $4$ | $5$ (pivot) | $0$ | $1$ | $0$ | $40$ ||$8$ (lowest positive number)|
| $s_3$ | $0$ | $50$ | $13$ | $0$ | $0$ | $1$ | $200$ ||$15.4$|


Changing the system, our table will start looking like:

| Basic Variables | $L$ | $x_1$ |$x_2$ | $s_1$ | $s_2$ | $s_3$ | $b$ |
| :--- | ---- |---| ---| ---| ---| ---| ---: |
| $L$ | $1$ | $-9$ | $0$ | $0$ | $12$ | $0$ | $480$ |
| | | | | | | | |
| $s_1$ | $0$ | $4.8$ | $0$ | $1$ | $-0.8$ | $0$ | $8$ |
| $x_2$ | $0$ | $0.8$ | $1$ (pivot) | $0$ | $0.2$ | $0$ | $8$ |
| $s_3$ | $0$ | $39.6$ | $0$ | $0$ | $-2.6$ | $1$ | $96$ |

And our current solution has $[s_1,x_2,s_3]=[8,8,96]$ as basic variables and $[x_1,s_2]=[0,0]$ as non-basic variables. With this scenario, the objective function is now $L=480$. Graphically speaking:

![sand_clay_8](./figs/sand_clay_8.png)

**But is it already the optimal solution?**

The next step will be to check if the solution obtained is the optimal solution and move to the next basic solution if it is not:

| Basic Variables | $L$ | $x_1$ |$x_2$ | $s_1$ | $s_2$ | $s_3$ | $b$ |
| :--- | ---- |---| ---| ---| ---| ---| ---: |
| $L$ | $1$ | $-9$ (negative) | $0$ | $0$ | $12$ | $0$ | $480$ |
| | | | | | | | |
| $s_1$ | $0$ | $4.8$ | $0$ | $1$ | $-0.8$ | $0$ | $8$ |
| $x_2$ | $0$ | $0.8$ | $1$ | $0$ | $0.2$ | $0$ | $8$ |
| $s_3$ | $0$ | $39.6$ | $0$ | $0$ | $-2.6$ | $1$ | $96$ |

So it's not optimal

Repeating the same procedure again to identify the variables to enter and to leave:

| Basic Variables | $L$ | $x_1$ (variable to enter) |$x_2$ | $s_1$ | $s_2$ | $s_3$ | $b$ || $\Delta$|
| :--- | ---- |---| ---| ---| ---| ---|---|---| ---: |
| $L$ | $1$ | $-9$ (most negative coefficient) | $0$ | $0$ | $12$ | $0$ | $480$ |||
| | | | | | | | |||
| $s_1$ (variable to leave) | $0$ | $4.8$ (pivot) | $0$ | $1$ | $-0.8$ | $0$ | $8$ ||1.67 (lowest positive number)|
| $x_2$ | $0$ | $0.8$ | $1$ | $0$ | $0.2$ | $0$ | $8$ ||10|
| $s_3$ | $0$ | $39.6$ | $0$ | $0$ | $-2.6$ | $1$ | $96$ ||2.42|

So $x_1$ is the variable to enter and $s_1$ the variable to leave.

Transforming the table again, we will obtain:

| Basic Variables | $L$ | $x_1$ |$x_2$ | $s_1$ | $s_2$ | $s_3$ | $b$ |
| :--- | ---- |---| ---| ---| ---| ---| ---: |
| $L$ | $1$ | $0$ | $0$ | $1.87$ | $10.5$ | $0$ | $495$ |
| | | | | | | | |
| $x_1$ | $0$ | $1$ (pivot) | $0$ | $0.21$ | $-0.17$ | $0$ | $1.67$ |
| $x_2$ | $0$ | $0$ | $1$ | $-0.17$ | $0.33$ | $0$ | $6.67$ |
| $s_3$ | $0$ | $0$ | $0$ | $-8.25$ | $4$ | $1$ | $30$ |

The current solution is now given by $L=495$, which results from having $[x_1,x_2,s_3]=[1.67,6.67,30]$ as basic variables and $[s_1,s_2]=[0,0]$ as non-basic variables. Graphically speaking:

![sand_clay_12](./figs/sand_clay_12.png)

Now we just need to check if the solution we have just obtained is optimal and, in this case, it is!

| Basic Variables | $L$ | $x_1$ |$x_2$ | $s_1$ | $s_2$ | $s_3$ | $b$ |
| :--- | ---- |---| ---| ---| ---| ---| ---: |
| $L$ | $1$ | $0$ (positive) | $0$ (positive) | $1.87$ (positive)| $10.5$ (positive) | $0$ (positive) | $495$ |
| | | | | | | | |
| $x_1$ | $0$ | $1$ | $0$ | $0.21$ | $-0.17$ | $0$ | $1.67$ |
| $x_2$ | $0$ | $0$ | $1$ | $-0.17$ | $0.33$ | $0$ | $6.67$ |
| $s_3$ | $0$ | $0$ | $0$ | $-8.25$ | $4$ | $1$ | $30$ |

So, this is the optimal solution

:::{card} Quiz questions
<iframe src="https://tudelft.h5p.com/content/1292123849460777397/embed" aria-label="2_3_3_1_simplex_method" width="1088" height="637" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>
:::

## Summary

The SIMPLEX workflow is shown in the scheme below:

![sand_clay_14](./figs/sand_clay_14.png)