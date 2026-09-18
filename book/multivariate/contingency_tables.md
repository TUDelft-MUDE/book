# Contingency tables

A **contingency table** summarizes observations of one or more discrete random variables. Each cell contains the number of observations corresponding to a particular combination of outcomes. By dividing these counts by the total number of observations, we can turn the table into a probability distribution.

Contingency tables are especially useful because the same table can be used to study three closely related quantities:

- **marginal distributions**, which describe one random variable on its own;
- **joint distributions**, which describe two random variables simultaneously;
- **conditional distributions**, which describe one random variable after fixing the value of another.

In the interactive examples below, we will use hair color and eye color as discrete random variables. The examples use the same data throughout so that you can see how the different probability distributions are related.

**Attribution**: The data used in the interactive elements is taken from [Table 3 of Snee, 1974, *Graphical Display of Two-way Contingency Tables*](https://www.jstor.org/stable/2683520); it shows hair and eye colour of students that took an introductory statistics course at the University of Delaware.

## Marginal distributions

Suppose a discrete random variable $X$ can take one of the categories $x_1,\ldots,x_k$. Its probability distribution assigns a probability to each possible outcome,

$$
p_X(x_i) = P(X=x_i).
$$

For a discrete random variable, these probabilities must satisfy

$$
p_X(x_i) \geq 0 \quad \text{(First Axiom of probability)}
$$

for every possible value $x_i$, and

$$
\sum_i p_X(x_i)=1.  \quad \text{(Second Axiom of probability)}
$$

If our data contain $N$ observations, and the outcome $x_i$ occurs $n_i$ times, we can estimate its probability directly from the relative frequency,

$$
p_X(x_i)=\frac{n_i}{N}.
$$

The figure below shows the distribution of hair color in the example dataset. The same information is represented in three ways: as category counts, as bars, and as fractions of the total in a pie chart. Move your mouse over a category, or click/tap it, to highlight the corresponding parts of the different representations.

```{iframe-figure} ../_static/elements/element_contingency_table_univariate_marginal.html
:name: contingency_table_univariate_marginal

Interactively visualize a univariate discrete probability distribution. Hover over, click, or tap a hair-color category to highlight the same outcome across the different representations.
```

When a single variable is extracted from a larger table containing several variables, this distribution is called a **marginal distribution**. The term *marginal* comes from the common practice of writing the corresponding totals in the *margins* of a contingency table.

## Joint distributions

We now consider two discrete random variables simultaneously. Let $X$ denote eye color and $Y$ denote hair color. The probability that both variables take particular values is a **joint probability**,

$$
p_{X,Y}(x_i,y_j)
=
P(X=x_i,\;Y=y_j).
$$

If $n_{ij}$ observations fall in the cell corresponding to $X=x_i$ and $Y=y_j$ (e.g., a person has *black* hair and *green* eyes), then

$$
p_{X,Y}(x_i,y_j)
=
\frac{n_{ij}}{N}.
$$

The collection of all joint probabilities forms the **joint probability distribution**. Just as for a univariate distribution, all probabilities are non-negative and the probabilities over the complete table must sum to one:

$$
\sum_i\sum_j p_{X,Y}(x_i,y_j)=1.
$$

The interactive contingency table below shows the joint distribution of eye color and hair color. Hover over, click, or tap any cell. The selected cell corresponds to one joint event, while the bars along the edge of the table show the marginal distributions of eye color and hair color.

```{iframe-figure} ../_static/elements/element_contingency_table_joint.html
:name: contingency_table_joint

Interactively visualize a joint probability and the corresponding marginal probabilities. Select a cell to compare the cell count with the row total, column total, and grand total.
```

The marginal distributions introduced above can be recovered directly from the joint distribution. To obtain the marginal probability of one eye color, we sum the joint probabilities over all possible hair colors:

$$
p_X(x_i)
=
\sum_j p_{X,Y}(x_i,y_j).
$$

Similarly, the marginal distribution of hair color is obtained by summing over all possible eye colors:

$$
p_Y(y_j)
=
\sum_i p_{X,Y}(x_i,y_j).
$$

In terms of counts, this is exactly what the row and column totals of a contingency table represent. For example,

$$
p_X(x_i)
=
\frac{\sum_j n_{ij}}{N},
\qquad
p_Y(y_j)
=
\frac{\sum_i n_{ij}}{N}.
$$

This is why the marginal distributions from the previous section reappear naturally along the edges of the joint contingency table.

## Conditional distributions

A joint distribution describes how two variables occur together. Often, however, we want to ask a different question: **how is one variable distributed when the value of the other variable is already known?**

This leads to a **conditional probability**. For example, the probability of observing hair color $Y=y_j$ given eye color $X=x_i$ is

$$
p_{Y|X}(y_j|x_i)
=
P(Y=y_j\mid X=x_i).
$$

The conditional probability is obtained by dividing the corresponding joint probability by the probability of the event we condition on:

$$
p_{Y|X}(y_j|x_i)
=
\frac{p_{X,Y}(x_i,y_j)}{p_X(x_i)}.
$$

Using counts from the contingency table, the same calculation becomes

$$
p_{Y|X}(y_j|x_i)
=
\frac{n_{ij}}{\sum_j n_{ij}}.
$$

The important change compared with a joint probability is the **denominator**. For a joint probability we divide by the total number of observations, $N$. For a conditional probability we restrict our attention to the observations satisfying the condition, so the denominator becomes the relevant row or column total.

The interactive figure below makes this restriction explicit. Use the lock symbols to choose the eye color or hair color on which you want to condition. The locked row or column becomes the new sample space. Within that subset, hover over, click, or tap a cell to compute the corresponding conditional probability.

```{iframe-figure} ../_static/elements/element_contingency_table_conditional.html
:name: contingency_table_conditional

Interactively visualize conditional probabilities. Lock a row or column to define the conditioning event, then select a cell to see the corresponding conditional-probability calculation.
```

Conditioning can be performed in either direction. If we instead want the probability of eye color $X=x_i$ given hair color $Y=y_j$, then

$$
p_{X|Y}(x_i|y_j)
=
\frac{p_{X,Y}(x_i,y_j)}{p_Y(y_j)}
=
\frac{n_{ij}}{\sum_i n_{ij}}.
$$

For a fixed conditioning event, the resulting conditional probabilities again form a probability distribution. Therefore,

$$
\sum_j p_{Y|X}(y_j|x_i)=1
$$

for a fixed value of $x_i$, and similarly,

$$
\sum_i p_{X|Y}(x_i|y_j)=1
$$

for a fixed value of $y_j$.

The joint, marginal, and conditional distributions are consequently not separate objects. They are three different ways of reading the same contingency table:

- a **cell** gives a joint probability;
- a **row or column total** gives a marginal probability;
- a **cell divided by its row or column total** gives a conditional probability.

% START-CREDIT

% source: contingency_tables

```{attributiongrey} Attribution
:class: attribution

This chapter was written by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```

% END-CREDIT
