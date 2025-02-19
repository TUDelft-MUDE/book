(rr_intro)=
# An Introduction to Risk and Reliability

_This chapter provides a brief introduction to risk and reliability, a topic that will be revisited in later chapters of this book._

Almost all activities in life are characterized by some level of risk, such as riding a bike or driving a car, boarding an airplane, or living below sea level behind a flood protection system. Particularly within the field of civil engineering and geosciences, risk and safety are key concepts that should be taken into account explicitly in design and management. Failures of systems providing flood protection, water distribution, transportation networks, air quality control, energy production, buildings and other infrastructure are expected to occur rarely, but can lead to large consequences. On the other hand, these systems also provide many benefits to humankind on a daily basis. 

*Risk* is often defined simply as the combination of probability and consequences; it is a measure of how bad something can be (the consequence) combined with the chance that it can happen. In mathematical form: 

$$\text{Risk}_\text{bad thing}=\text{Consequence}_\text{bad thing}\cdot\text{Probability}_\text{bad thing}$$

```{note}
:class: dropdown
Why are the variables above written using words? Because many different terms and symbols are used in different fields of science and engineering which refer to about the same mathematical concepts. For example, 'failure probability,' $p_f$, is often used when designing structural components. However, this term may be misleading when applied to the probability that the concentration of a solute in groundwater exceeds a certain value, or the discharge of a river falling below a regulatory threshold for fish migration.
```

As engineers we are typically concerned with making sure bad things don't happen, or, stated more precisely for our purposes: *reducing the **probability** of a bad thing happening to an **acceptable** level.* To determine if this probability results in a situation that is *safe enough,* an acceptable level of risk needs to be defined. The eventual decision about acceptable risk is predominantly a political one, but engineers can have an important role in the discussion and decision-making. They can provide information on failure probabilities and consequences (economic consequences, life loss, etc.) of a given system and highlight trade-offs between investments in safer systems and risk reduction. Risk plays an important role in many current societal discussions. Examples include recent discussions related to Covid-19 vaccination programs and mitigation measures like facemasks, where there was a lot of uncertainty in the effect of virus spread. Another example is the discussion over nuclear power versus fossil fuels: both activities bring various benefits (energy generation) but also introduce additional risks to the population and environment. A systematic analysis of risks of (proposed) projects can help to inform the broader societal discussions.

Inevitably, the consideration of risk should result in a specific value of probability that can be used in the design or evaluation of something; in other words, a specific criteria for $\text{Probability}_\text{bad thing}$. For standard applications and systems that are frequently used, the risk analysis has been done. For instance, building codes are available that define acceptable safety levels in such a way that the failure probability of a structure is sufficiently small. A specific example is Eurocode, which provides guidance for the design of structures using so-called target values for the failure probability different safety classes. Thus, critical buildings like hospitals are designed to be stronger than a hardware store. However, for other applications, e.g. special structures or new applications like the reliability of renewable energy-generating components, no standard codes or guidelines are available for design and a more explicit analysis of the reliability and risk of the system is required. An example from the past is the design of the Eastern Scheldt barrier. The acceptable probabilities of failure of the structure and non-closure of the gates were determined based on the acceptable risk of flooding of Zeeland. These probability values formed the basis for the so-called probabilistic design of the barrier in the 1970’s.

```{note}
:class: dropdown
Although much of this book focuses on calculating failure probability, or $\text{Probability}_\text{bad thing}$, we call this a reliability analysis, where *reliability* is simply  

$$\text{Reliability}=1-\text{Probability}_\text{bad thing}$$

So in fact, as engineers we are optimistic, otherwise this chapter would be called Risk and *Un*reliability.
```

% ## Risk and Reliability in Practice

% Throughout this book we will repeatedly draw on the field of flood management to illustrate risk and reliability concepts as this field requires expertise from all perspectives in civil and environmental engineering and geosciences, from climate and hydrologic processes to evacuation and recovery. In addition, this field has driven the development and use of risk and reliability techniques in the Netherlands since the flooding disaster of 1953, not to mention the experience gained during the previous millenium, albeit in a less rigorous mathematical fashion. And finally, new safety standards for primary flood defences in the Netherlands have been in place since 2017 that are formulated as a tolerable failure probability of dike[^dike] segments. As such, dike reinforcements are legally required to be designed according to these new standards, which requires one to show that the failure probability is less than an allowable maximum value.

% Despite the focus on flood management, many applications exist in other fields, for example the discussion about the gas extraction in the North of the Netherlands which leads to increased earthquakes, building damage and potential injury to humans. A thorough analysis of the probability of earthquake occurrence, structural safety of various infrastructure (houses, levee, hospitals, pipelines), benefits associated with extracting gas and the resulting level of risk is required to make decisions about how to manage this industry. As with the flood management application, advanced knowledge of probabilistic techniques is needed. 

**It All Comes Back to Probability**

In short, risk and reliability concepts cannot be defined or applied without *probability.* It is necessary in order to quantify uncertainty and take it into account when making decisions, regardless of whether our specific task is to investigate, assess, design or create policy for a particular engineering problem. Probability theory is a powerful tool because it provides a way to quantify many aspects of uncertainty, for example:
- precision of measurements
- variability in data
- accuracy and precision of data-driven or physics-based models
- stochastic processes
- unknown conditions due to lack of data 
- inability to predict the outcome of future events with sufficient accuracy or precision
- and many more

It is crucial that engineers are able to understand and apply the concepts of risk and reliability, as well as probability theory.

**Probabilistic Design**

Stated as simply as possible, the term *probabilistic design* implies the use of probability to design something. Although this may sound complex, it is actually not much different than a deterministic approach, where values used to design something are not assumed to be random. For example, the load on a beam, or the maximum discharge expected in a river. In a typical design process, the problem and functional requirements are first defined, the system or component is evaluated and then refined {cite:p}`voorendt2017`. It is ideally an iterative process, where tradeoffs between competing requirements must be considered in order to arrive at an optimal configuration. During much of your university education you have probably learned a variety of techniques to evaluate interesting problems in your field of study; however, only towards the end of a bachelor or master program do you begin to *design* things and take into count information beyond what is written in a simple exam problem to make decisions. The design process is often challenging because there is no single right answer, and it turns out that incorporating probability in the design process can help.

Consider some arbitrary object--let's call it a thingamajig--which we must design and eventually build. We would like to apply the *factor of safety* approach, which compares load[^solicitation], $S$, to resistance, $R$, such that $FS=R/S$. As long as we make sure that $S$ is less than $R$, or $FS>1$, our thingamajig will never fail. We could also use the *safety margin* approach, where $M=R-S$, which also quantifies the point between safe and unsafe, although here we make sure $M>0$. These so-called *limit states* make the design process quite simple and is a great engineering approach for many situations, for example, if:
1. the values of $R$ and $S$ are precisely known, or the range of values is negligibly small
2. $R$ and $S$ never change (at least not over short time or length scales)
3. $R$ and $S$ are easy to measure in all locations of interest
4. the model used to design the thingamajig is nearly perfect
5. the consequence of a failure is negligible

In situations like this you can make your design decision and rest assured that there won't be any lawyers knocking on your door in the near future because the thingamajig broke.

For many situations, however, a deterministic analysis is not wise because we cannot guarantee that our thingamajig will always survive. When $R$ and/or $S$ can take on a range of possible values, all of a sudden there is a chance that our thingamajig is *not* reliable: there is a distinct probability it may *fail.* Part of this book is concerned with the quantification of what is often called the *failure probability,* $p_f$, for which there are many different techniques. These techniques all rely on  probability theory because it allows us to quantitatively account for the following in our engineering process:  

1. imprecise measurements
2. model error
3. randomness in some of our important design variables
4. risk-based design criteria and safety standards

These are just a few examples, where items 3 and 4 are the focus of the following chapters, and items 1 and 2 have already been considered elsewhere in MUDE.

%Sometimes we have criteria, sometimes we do not.

<!-- ## Chapter Overview -->

%Terms and definitions first??
%Aleatoric and epistemic.
%Sometimes we don't have a structure. Then we can consider just the *hazard*.

A probabilistic design is illustrated in the following sections, first with the simple cases of one random variable. Then an example with two random variables is used, which can be referred to as a *bivariate* case. This is more insightful than the univariate case because it allows us to consider the quantitative and qualitative influence of dependence, as well as the functional relationship between two variables and their joint probability density (e.g., union, intersection or limit-states).

<!-- The evaluation and design of a river flood protection system is used to introduce key aspects of risk and reliability, as well as the design process. A distinction is made between using probability to assess engineering components and systems (reliability analysis) and to derive design criteria (risk evaluation), which are introduced formally in later chapters after the general risk analysis framework is discussed. -->

<!-- ```{admonition} MUDE exam information
:class: tip
In this chapter exam tips are given on the page of each section.
``` -->

%Table of contents:

%```{tableofcontents}
%```

[^solicitation]: $S$ stands for solicitation. While this letter and word are much more pedantic-sounding than simply using load, or $L$, it is widely used in the structural engineering field, where component reliability methods were pioneered. Here we take a broader approach on the subject. Classical texts are {cite:t}`adk2022`, {cite:t}`moss2020` and {cite:t}`ditlevsen1996`.
%[^pattern]: The word *paradigm* is not used because it suggests completeness. The examples here, are meant to be used as illustrations for key concepts, and extended to other situations and higher dimensions, so *pattern* seems more appropriate.