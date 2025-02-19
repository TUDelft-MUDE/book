(risk)=
# Risk Analysis

Throughout this book we have focused on a variety of deterministic and probabilistic topics, which probably appeared to be completely unrelated. However, in engineering practice we often need to combine deterministic and probabilistic approaches to design and assess the projects we work on and Risk Analysis concepts are an important way to facilitate this. In particular, concepts in this chapter are focused not so much on evaluating the behavior of a particular system, but rather _evaluating the risk associated with various outcomes_ and, most importantly, providing _a framework with which decisions can be made to improve it._

**Risk and Reliability in Practice**

Throughout this chapter of the book we will repeatedly draw on the field of flood management to illustrate risk and reliability concepts as this field requires expertise from all perspectives in civil and environmental engineering and geosciences, from climate and hydrologic processes to evacuation and recovery. In addition, this field has driven the development and use of risk and reliability techniques in the Netherlands since the flooding disaster of 1953, not to mention the experience gained during the previous millenium, albeit in a less rigorous mathematical fashion. And finally, new safety standards for primary flood defences in the Netherlands have been in place since 2017 that are formulated as a tolerable failure probability of dike[^dike] segments. As such, dike reinforcements are legally required to be designed according to these new standards, which requires one to show that the failure probability is less than an allowable maximum value.

Despite the focus on flood management, many applications exist in other fields, for example the discussion about the gas extraction in the North of the Netherlands which leads to increased earthquakes, building damage and potential injury to humans. A thorough analysis of the probability of earthquake occurrence, structural safety of various infrastructure (houses, levee, hospitals, pipelines), benefits associated with extracting gas and the resulting level of risk is required to make decisions about how to manage this industry. As with the flood management application, advanced knowledge of probabilistic techniques is needed. 


```{admonition} MUDE exam information
:class: tip

Concepts in this section to focus on for the Q2 MUDE exam are:
- **Risk Definition** and the **Risk Curve** (Section 8.1)
- Evaluation of risk using various **Safety Standards** (the last page of Section 8.2)
- In particular, it is essential that you can construct a risk curve and interpret its meaning, as well as assess it using the limit line approach

A few exercises are provided at the end of this chapter, but do not exhaustively illustrate the type of questions that you can expect on the exam. See exam questions from previous years, as well as in-class activities, for additional examples.

```

```{admonition} MUDE not-on-the-exam information
:class: tip

There are several pages included in this chapter that provides useful pre-requisite ot background information and _you are expected to read and understand them;_ however, these pages do _not_ need to be studied intensively for the exam. This includes:

- Steps of a Risk Analysis (second page in Section 8.1)
- Decision analysis, cost benefit analysis and economic optimization (first 3 pages in Section 8.2)
- The Paint System example (Section 8.3)

```

[^dike]: A dike is a structure, typically made of soil, that protects a specific region from flooding by physically holding back water. Usually associated with rivers, such structures are also widely used on the coast, especially in low elevation areas such as the Netherlands. The Dutch word for levee is *dijk,* but English word *dike* is used in this book. Outside of the Netherlands the words *embankment* and *levee* are used.