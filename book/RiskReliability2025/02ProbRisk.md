# Probabilistic Risk Analysis

To answer these questions typically a triplet is used $〈s_i,p_i,x_i 〉$. Where $s_i$ is a scenario description, $p_i$ is the probability of the scenario and $x_i$ is the consequence of the scenario. Risk can be defined as a set of triplets  $R={〈s_i,p_i,x_i 〉}$, $i=1,…,N$. Because the possible scenarios in any risk analysis are infinite, and in practice the risk analyst cannot contemplate all these, an N+1 scenario that accounts for all “other” possibilities is often used.  
The triplets $〈s_i,p_i,x_i 〉$ are often presented in a tabular form 

<div align="center">

| Scenario | Probability  | Consequence |
|-------|-------|-------|
| $S_1$ | $p_1$ | $x_1$ |
| $S_2$ | $p_2$ | $x_2$ |
| ⋮     |   ⋮    |  ⋮    |
| $S_N$ | $p_N$ | $x_N$ |

</div> 

## Risk Curves 

To present a visual idea of risk, we first arrange the scenarios in order of severity. That is such that $x_1 \leq x_2 \leq x_3 \leq ⋯ \leq x_N$. By adding a column to the table above we may compute the cumulative probabilities adding from the bottom 

<div align="center">

| Scenario | Probability  | Consequence | Cumulative <br>Probabililty|
|-------|-------|-------|-------|
| $S_1$ | $p_1$ | $x_1$ | $P_1 = P2+p_1$ |
| $S_2$ | $p_2$ | $x_2$ |$P_2 = P3+p_2$ |
| ⋮     |   ⋮    |  ⋮    |  ⋮    |  
| $S_{N-1}$ | $p_{N-1}$ | $x_N$ | $P_1 = PN+p_{N-1}$ |
| $S_N$ | $p_N$ | $x_N$ |  $P_N = p_N$ |

</div> 

A plot of the consequences $x_i$ against the cumulative probabilities $P_i$ looks like Figure 1 although a common representation is in a log-log scale for both axis in which case the (smoothed risk) curve looks like in Figure 2.

