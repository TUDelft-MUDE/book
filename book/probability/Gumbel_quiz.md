
# Gumbel distribution: let's practice

Groundwater quality of a shallow aquifer has been tracked for a year to determine if it is duable to use it or if it is getting polluted. To this end, the daily maximum concentration of chloride in miligrams per liter has been measured. These concentration has been described using a Gumbel distribution with parameters $\mu=60$ and $\beta=10$.

Chlorides between 1mg/L an 100mg/L are normal in freshwater. Use the Gumbel distribution to compute the probability of being in that interval.

```{admonition} Answer
:class: tip, dropdown

The probability of being below 100mg/L is:

$$
   P[X \leq 100] = F(100) = e^{-e^{-\frac{100-60}{10}}} \approx 0.98 
$$

The same way, the probability of being below 1mg/L is:

$$
   P[X > 1] = F(1) = e^{-e^{-\frac{1-60}{10}}} \approx 0
$$

Thus, the probability of being in the interval (0,100) is

$$
    P[1 \leq X \leq 100] = 0.98 - 0 = 0.98
$$

The figure below illustrates the area to integrate in the PDF (blue area in the left pannel) and the probabilities computed in the CDF (right pannel).

```{figure} /probability/figures/gumbel_concentration.png

---

```


And what is the probability of exceeding the upper limit of 100mg/L?

```{admonition} Answer
:class: tip, dropdown

Making use of the probability axioms:

The probability of being below 100mg/L is:

$$
   P[X>100]=1-P[X \leq 100] = 1-F(100) = 1- 0.98 = 0.02
$$

This probability is very small, so the engineers can conclude that the water in the aquifer seems to present the characteristics of fresh water regarding the concentration of Chlorides.

```
