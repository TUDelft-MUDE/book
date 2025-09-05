(uncertainty_classification)=
# Uncertainty Classification

All of us have an idea of what is uncertainty, but we may use different names for it: unpredictability, randomness, ambiguity, variability... Thus, we can say that something is uncertain if we don't know for sure (*not a big surprise, right?*).

In the context of modelling and enginering, it can be useful to classify the sources of uncertainty since it allows us to identify, quantify and, if possible, reduce it. In general, we can distinguish three main types of uncertainty: aleatoric, epistemic and error.

## Aleatoric

The word *aleatoric* derives from the Latin *alea*, which means the rolling of dice. Therefore, when we talk about the aleatoric uncertainty, we refer to the one which is an intrinsic phenomenon and is typically associated with variations that occur in nature. For instance, if we want to predict river discharge next year for Amazon River, it is not possible to use models and data to reduce the uncertainties, since they occur in the future and a range of values is possible.



## Epistemic 

The word epistemic derives from the Greek *episteme*, which means knowledge. Therefore, an epistemic uncertainty is the one caused by the lack of knowledge. For instance, if I have only measured the width of a river 5 times over a length of a few km, I can only guess at the true width in between those measurement points. Since there are no other sources of information, there is not much I can say about those widths, therefore they are uncertain. If I invest time and resources making more measurements of the river width, the uncertainty will decrease. Thus, epistemic uncertainty is sometimes a matter of time and resources; at some point it is better to use a probability distribution to take the uncertainty into account rather than to collect more information to reduce it.

## Error

Error stands for any identifiable deficiency in any stage of modelling and simulation that is not due to lack of knowledge. For instance, the gauge will have some error when measuring the discharge. Sometimes this is also called model error, and sometimes it is also grouped together with epistemic uncertainty.

## A note about modelling uncertainty

In MUDE we will typically use probability distributions to model uncertainty because it is a relatively simple and straightforward approach. In fact, we focus mostly on continuous parametric distributions. Since we often use the same distributions to model all sources of uncertainty, the ability to classify it into different categories can be useful for interpreting the results of our stochastic models.

Note that there is no universal uncertainty classification. You can read more about this topic in [^ref1] or [^ref2].

[^ref1]: Der Kiureghian and Ditlevsen (2009). Aleatory or epistemic? Does it matter? *Structural safety* 31, 2, 105-112. [doi.org:10.1016/j.strusafe.2008.06.020](https://doi.org/10.1016/j.strusafe.2008.06.020)

[^ref2]: Van Gelder (2000). Statistical methods for the risk-based design of civil structures. PhD thesis. TUDelft. http://resolver.tudelft.nl/uuid:6a62d6fa-cbcc-4c38-af8a-027c3d191a9d


% START-CREDIT
% source: modelling_concepts
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Alessandro Cabboi, Patricia Mares Nasarre and Robert Lanzafame. {ref}`Find out more here <modelling_concepts_credit>`.
```
% END-CREDIT
