# Limit State Function


In reliability analysis we are typically concerned with the probability that a component or system does not perform its purpose adequately. When this happens we typically speak of *failure events*. Failure events in turn are described through mathematical relations in order to be properly described. A function that describes failure events is called a *limit state function*.

Let $E_f = \{\, \textbf{x} \in \textbf{X} : g(\textbf{x}) \leq 0 \}$ denote the failure set. Then $g$ is the limit state function. As usual, $\textbf{x}$ are samples or realizations of the random vector $\textbf{X}$. The probability of interest is thus, $P_f = P(E_f) = P\left(g(x) \leq 0\right)$ or $P_f = \int_{E_f} f_\textbf{X}(\textbf{x})\,\mathrm{d}\textbf{x}$.

There are several ways to compute $P_f$. In some basic cases one may use simple properties of the random variables of interest. In particular, for normal distributions and a linear limit state function, the calculation of the failure probability is very straightforward. 

## Linear Limit State Function and Normal Distributions

Consider the random vector $\textbf{X}=(X_1,\ldots,X_n)$ where all $X_i$ follow a normal distribution. Consider a linear limit state function given by:

$$
    g(\textbf{x}) = a_0+\sum_{i=1}^n a_ix_i
$$

One can show that sums of Normally distributed random variables are also normal with expected value and variance given by:

$$
    \mu_g = a_0+\sum_{i=1}^n a_i\mu_i
$$

$$
    \sigma^2_g = \sum_{i=1}^n a_i^2 \sigma_i^2 +2\sum_{i < j} a_ia_j \mathrm{Cov}(X_i,X_j)
$$

or in terms of correlation coefficients, using the definition of Pearson's correlation coefficient:

$$
    \sigma^2_g = \sum_{i=1}^n a_i^2 \sigma_i^2 +2\sum_{i < j} a_ia_j \rho_{i,j}\sigma_i \sigma_j
$$

In this case the probability of failure $P_{E_f} = P\left(g(\textbf{x})\leq0\right)$ may be computed by standardizing the Normal distribution corresponding to $g$. That is:  

$$
    P_{E_f} = P\left(g(\textbf{x})\leq0\right)=\Phi\left(\frac{0-\mu_g}{\sigma_g}\right) = \Phi(-\beta) 
$$

where $\beta=\frac{\mu_g}{\sigma_g}$ is sometimes called the *reliability index*. 

## Example

Consider a steel rod. The rod will fail if the stress applied in the cross sectional area ($a=10$mm$^2$) exceeds the yield strength (the resistance). The yield strength $r$ and the annual stress are uncertain. For simplicity they are assumed to follow independent normal distributions $R$ for resistance and $S$ for solicitation (or load).  The parameters of the normal distributions are $\mu_R = 350 \, \rm{MPa}$, $\sigma_R=35 \, \rm{MPa}$, $\mu_S = 1500 \, \rm{N}$ and $\sigma_S=300 \, \rm{N}$. The limit state function is:

$$
    g(r,s) = ar-s  
$$

to compute the failure region take $ g(r,s) = 0 \Rightarrow ar = s$. Compute the mean and standard deviation of the normal distribution corresponding to $g$.

The mean is given by: $\mu_g = 10 (350) - 1500 = 2000 \, \rm{N}$

For the standard deviation notice first that the variables are uncorrelated, hence only the terms with the variances remain: $\sigma_g=\sqrt{10^2(35^2)+300^2} \, \rm{N}  \approx460.98 \, \rm{N}$

The relibility index $\beta=\frac{2000}{460.98}\approx4.34$

Hence the probability of failure $P_{E_f}=\Phi(-4.34)\approx7.12\times10^{-6}$ in a cross sectional area.  The graphical representation is presented in the Figure below.

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/failure_region_RS.jpg

---

---
Graphical representation of the linear limit state and normal variables for the calculation of the  reliability of a steel rod.
```


Figure below shows the variables transformed to standard normal space. Notice that $\beta$ is an orthogonal vector to the limit state in the standard normal space. The point in $g$ with the smallest distance to the origin in standard normal space is sometimes called the *design point*. 

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/failure_region_Zspace.jpg

---

---
Graphical representation of the linear limit state and normal variables transformed to standard normal space with orthogonal vector and design point for the calculation of the  reliability of a steel rod.
```

Figure below shows the calculation of the failure probability through Monte Carlo simulation. In this case $\hat{P}_{E_f} = \frac{16}{2\times10^6}=8\times10^{-6}$

```{figure} https://github.com/TUDelft-MUDE/source-files/raw/main/file/MC_original_space_RS.jpg

---

---
Graphical representation of the Monte Carlo simulation performed for the calculation of the  reliability of a steel rod.
```


% START-CREDIT
% source: risk_reliablity_credit
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Patricia Mares Nasarre, Max Ramgraber and Oswaldo Morales Napoles. {ref}`Find out more here <risk_reliability_credit>`.
```
% END-CREDIT
