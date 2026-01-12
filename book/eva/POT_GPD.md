
# Peak Over Threshold & GPD

A second approach to Extreme Value Analysis is Peak Over Threshold (POT): a threshold value is chosen and all observations in the time series that exceed the threshold are selected. In this chapter we will see that this method is theoretically linked to the Generalized Pareto distribution (GPD).

Compared to BM, the POT method is useful when time series are short and there may not be enough data to fit a distribution to the annual maxima: a 10 year record may have a lot of hourly observations, but will only produce 10 data points if you want to find a distribution for the annual maxima! We will also see that the selection of a threshold (and declustering time) adds considerably to the subjectivitity and judgement required when choosing a distribution to represent, and extrapolate, your data.

Our objective in this book is to introduce key concepts and theorems to give a thorough understanding of POT assumptions and analysis. Keep in mind that in engineering practice and research, there are many variations and alternatives to the methods presented here.


% START-CREDIT
% source: extreme_value_analysis
```{attributiongrey} Attribution
:class: attribution
This chapter is written by Patricia Mares Nasarre. {ref}`Find out more here <extreme_value_analysis_credit>`.
```
% END-CREDIT
