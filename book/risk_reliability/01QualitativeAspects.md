
# Qualitative aspects

Risk and reliability are concepts that are often used together, and sometimes they are even interchanged and confused with each other. However, they are distinct concepts, to the point that the mathematical tools used to describe them are developing along increasingly separate lines. Both concepts use the more general concept of probability since both concepts deal with uncertainty and probability, as we have discussed, gives us the mathematical framework required to describe it. 

To define risk and introduce some of the tools available for risk analysis, we follow Kaplan and Garrick (1981)[^1]. The definition of reliability follows Barlow and Proschan (1996)[^2]. 

We start by observing that _hazard_ is a source of danger. In Engineering and Geosciences, we typically deal with natural hazards such as storms, hurricanes or earthquakes.

_Risk_ is the possibility of loss or injury (presumably because of an adverse situation happening) and the degree of probability of such loss. Thus, it is common to find as quantitative definition of risk the following

$$
R_{A} = p_A \times C_A
$$

where $R_A$ is the risk of the event A, $p_A$ is the probability of the event A happening, and $C_A$ are the consequences derived from the event A happening. Event A could be, for instance, the ocurrence of an accident in a bridge that leads to stopping the traffic.

_Reliability_ is the probability of a device or system performing its intended function under given conditions for a specified period of time. For instance, given a bridge that connects two sides of the river, its function is to serve as connection between the two margins of the river. The reliability of the bridge would be the probability of being fully operative, allowing traffic to cross from margin to margin.

Notice some important distinctions between reliability and risk: 

1.   when speaking about reliability **the focus is performance** and the consequence is lack of adequate performance or failure while risk focuses on the consequences of certain hazardous events.
2.  reliability is often used in engineering, more recently in investigating the reliability of models (although all models are wrong). **Risk is a broader concept** often encountered in safety, economics, insurance and engineering.
3.  the **time aspect is an explicit part of the definition** of reliability. In reliability theory one often speaks of time to failure or survival time. When speaking of risk, time can be chosen as part of the analysis. 


Because of its broader scope, we will deal mostly with risk analysis. A risk analysis answers three questions: (i) What can happen? (ii) How likely is it that that will happen, and (iii) If it does happen what are the consequences? 

[^1]: Kaplan, S., and Garrick, B. J. (1981). On the Quantitative Definition of Risk. Risk Analysis 1, 1, 11-27. https://doi.org/10.1111/j.1539-6924.1981.tb01350.x

[^2]: Barlow, R.E., and Proschan F. (1996). Mathematical Theory of Reliability. Society for Industrial and Applied Mathematics (SIAM). https://doi.org/10.1137/1.9781611971194 
