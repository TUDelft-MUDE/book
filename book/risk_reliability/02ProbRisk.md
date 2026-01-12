# Probabilistic Risk Analysis

We established that a risk analysis answers three questions: (i) What can happen? (ii) How likely is it that that will happen, and (iii) If it does happen what are the consequences? To answer these questions typically a triplet is used $〈s_i,p_i,x_i 〉$. Where $s_i$ is a scenario description, $p_i$ is the probability of the scenario and $x_i$ is the consequence of the scenario. Risk can be defined as a set of triplets  $R={〈s_i,p_i,x_i 〉}$, $i=1,…,N$. Because the possible scenarios in any risk analysis are infinite, and in practice the risk analyst cannot contemplate all these, an N+1 scenario that accounts for all “other” possibilities is often used.  
The triplets $〈s_i,p_i,x_i 〉$ are often presented in a tabular form  as

<div align="center">

| Scenario | Probability  | Consequence |
|-------|-------|-------|
| $S_1$ | $p_1$ | $x_1$ |
| $S_2$ | $p_2$ | $x_2$ |
| ⋮     |   ⋮    |  ⋮    |
| $S_N$ | $p_N$ | $x_N$ |

</div> 

For example, imagine that you are analyzing the risk of a bridge connecting two sides of a river. We can define five events:
1. Failure of the bridge due to the support beams;
2. Failure due to scouring around the bridge foundation;
3. Stop of the traffic due to a car accident;
4. Stop of the traffic due to damages in the pavement;
5. Normal operation of the bridge. 

Once the scenarios are defined, we can define the triplets

<div align="center">

| Scenario | Probability  | Consequence |
|-------|-------|-------|
| 1 | $0.04$ | $2 \cdot 10^6$ |
| 2 | $0.03$ | $3\cdot 10^5$ |
| 3 | $0.10$ | $5\cdot 10^4$ |
| 4 | $0.08$ | $7\cdot 10^5$ |
| 5 | $1-0.04-0.03-0.10-0.08 = 0.75$ | $0$ |

</div> 

where the consequences here are assessed in terms of economic consequences (€).

## Risk Curves 

To present a visual idea of risk, we first arrange the scenarios in order of severity. That is such that $x_1 \leq x_2 \leq x_3 \leq ⋯ \leq x_N$. By adding a column to the table above we may compute the cumulative probabilities adding from the bottom.

<div align="center">

| Scenario | Probability  | Consequence | Cumulative <br>Probabililty|
|-------|-------|-------|-------|
| $S_1$ | $p_1$ | $x_1$ | $P_1 = P2+p_1$ |
| $S_2$ | $p_2$ | $x_2$ |$P_2 = P3+p_2$ |
| ⋮     |   ⋮    |  ⋮    |  ⋮    |  
| $S_{N-1}$ | $p_{N-1}$ | $x_N$ | $P_1 = PN+p_{N-1}$ |
| $S_N$ | $p_N$ | $x_N$ |  $P_N = p_N$ |

</div> 

A plot of the consequences $x_i$ against the cumulative probabilities $P_i$ looks like shown in the Figure below.

```{figure} https://files.mude.citg.tudelft.nl/risk_curve.png

---

---
Example of risk curve.
```


A common representation is in a log-log scale for both axis in which case the (smoothed risk) curve looks like in the Figure below.

```{figure} https://files.mude.citg.tudelft.nl/risk_curve_log.png

---

---
Example of risk curve in log-log scale.
```

Going back to the previous example of the bridge, we can order the triplets in decreasing order of severity as

<div align="center">

| Scenario | Probability  | Consequence |Cumulative <br>Probabililty|
|-------|-------|-------|-------|
| 5 | $1-0.04-0.03-0.10-0.08 = 0.75$ | $0$ | $1.00$ |
| 3 | $0.10$ | $5\cdot 10^4$ | $0.25$ |
| 2 | $0.03$ | $3\cdot 10^5$ | $0.15$ |
| 4 | $0.08$ | $7\cdot 10^5$ | $0.12$ |
| 1 | $0.04$ | $2 \cdot 10^6$ | $0.04$ |


</div> 

Finally, we can represent the risk curve as

```{figure} https://files.mude.citg.tudelft.nl/example_risk_curve.png

---

---
Risk curve for the bridge example.
```

And in log-log scale as


```{figure} https://files.mude.citg.tudelft.nl/example_log_curve.png

---

---
Risk curve in log-log scale for the bridge example.
```


% START-CREDIT
% source: risk_reliablity_credit
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Patricia Mares Nasarre, Max Ramgraber and Oswaldo Morales Napoles. {ref}`Find out more here <risk_reliability_credit>`.
```
% END-CREDIT
