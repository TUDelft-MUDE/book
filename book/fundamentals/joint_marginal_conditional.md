# Joint, Marginal, and Conditional Distributions

Understanding the relationships between random variables is fundamental in probability and statistics. This chapter provides a quick yet comprehensive review of **joint**, **marginal**, and **conditional** distributions, focusing on continuous variables.

---

## Joint Distribution

The **joint probability distribution** describes the likelihood of two (or more) random variables occurring simultaneously.

**Definition:**  
Let $X$ and $Y$ be continuous random variables with joint probability density function (PDF) $ p_{XY}(x, y) $. Then:

$$
p(a < X < b, \, c < Y < d) = \int_c^d \int_a^b p_{XY}(x, y) \, dx \, dy
$$

**Properties:**
- $ p_{XY}(x, y) \geq 0 $
- $ \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} p_{XY}(x, y) \, dx \, dy = 1 $

---

## Marginal Distributions

The **marginal distribution** of one variable is obtained by integrating out the other.

**Formulas:**
- Marginal PDF of $ X $:  

  $$
  p_X(x) = \int_{-\infty}^{\infty} p_{XY}(x, y) \, dy
  $$

- Marginal PDF of $ Y $:  
  
  $$
  p_Y(y) = \int_{-\infty}^{\infty} p_{XY}(x, y) \, dx
  $$

These describe the distributions of $ X $ and $ Y $ on their own.

---

## Conditional Distribution

The **conditional distribution** quantifies the probability of one variable given the other.

**Formula:**  
If $ p_Y(y) > 0 $:

$$
p_{X|Y}(x | y) = \frac{p_{XY}(x, y)}{p_Y(y)}
$$

Similarly:

$$
p_{Y|X}(y | x) = \frac{p_{XY}(x, y)}{p_X(x)}
$$

**Interpretation:**  
This reflects how knowing one variable (e.g., $ Y $) affects our knowledge about the other (e.g., $ X $).

---

## Independence

Two variables $ X $ and $ Y $ are **independent** if:

$$
p_{XY}(x, y) = p_X(x) p_Y(y)
$$


When independent, knowing $ Y $ provides no information about $ X $, and vice versa.

---

