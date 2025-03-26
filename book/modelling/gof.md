# Goodness of Fit

In the previous sections we have introduced the concept of model and the need of selecting an appropriate model *ad hoc* for our problem. Also, you have been introduced to the concepts of verification, validation and calibration. In the validation process, we compared the results of our model with known reference values to assess the performance of the model. **But how good is the performance?** If there are different verified and validated models I can use, **which one is better?**

We can make use of **goodness of fit (GOF) techniques** to support our answers to those questions. GOF techniques are objective and (mainly) quantitative metrics which provide insight into the performance of models. It is important to note that GOF techniques are not a ground truth, but an objective way of comparing models. Different techniques may lead to different results and it is the engineer who has to balance those outputs and select the best model. Thus, it is recommended to use more than one GOF technique in the decision-making process. In the subsequent sections, some commonly used GOF techniques are presented.

In order to illustrate these techniques, the following example will be used. Waves suffer several physical processes when travelling from offshore to the coast (namely, refraction, diffraction, shoaling, reflection and breaking). We typically have wave measurements offshore and need to propagate them using a propagation model to the coast to assess the loads on, for instance, a water intake or a structure. In this example, we have measurements of waves both offshore and near the shore obtained through physical model tests (small-scale tests). We are going to assess how accurate the performance of the propagation model is for two wave features: the significant wave height ($H_{m0}$) and the mean wave period ($T_m$) [^reference]. GOF techniques will be applied to quantify this performance.

## How does it look?

The first step when addressing a problem is to visualize it. Thus, the first GOF technique recommended here (note that it is not a metric) is visual inspection. It is common practice to plot the reference values against the predictions given by our model, as shown below. The perfect fit would correspond to all the points aligned with the 45-degrees line.

%```{figure} ./figs/Visual_inspection.png
%
%---
%
%---
%Comparison between measured and predicted: (a) siginificant wave height, $H_{m0}$, and (b) mean wave period, $T_m$.
%```
%
% source unknown

![](https://files.mude.citg.tudelft.nl/replacement.svg)

Just using the above plot, we can see that our model tends to underpredict $T_m$. Also, we can see that the performance to estimate $H_{m0}$ is better than for $T_m$, since the points are way closer to the 45-degrees line. But **how much better?** 

## Square differences

In many fields, it is common practice to use GOF metrics based on the squared errors between the measurements and the predictions ($SE$). 

$$
SE_i=(y_i - \hat  y_i)^2
$$

where $y_i$ are the observations and $\hat  y_i$ are the predictions. 

Note that it does not matter the sign of the error ($y_i > \hat  y_i$ or $y_i < \hat  y_i$), $SE$ will always be positive. This is computationally very convenient in optimization processes, such as when calibrating the coefficients of a model minimizing the $SE$. Convergence is faster when the objective function ($SE$) does not change from one sign to another between iterations but only changes in absolute value (you will learn more about this later in the course).

Within this family of metrics, we will focus here on two: the Root Mean Square Error ($RMSE$) and the coefficient of determination ($R^2$).

### Root Mean Square Error ($RMSE$)

The Root Mean Square Error ($RMSE$) is defined as 

$$
RMSE=\sqrt{\frac{\sum_{i=1}^{N} (y_i - \hat  y_i)^2}{N}}=\sqrt{MSE}
$$

where $N$ is the number of observations and $MSE$ is the mean squared error computed as

$$
MSE = \frac{\sum_{i=1}^{N} (y_i - \hat  y_i)^2}{N} = \frac{\sum_{i=1}^{N} (SE_i)^2}{N}
$$ 

$RMSE$ is a very intuitive metric since it represents the mean error between the observations and the predictions. Therefore, the lower the $RMSE$, the better. Moreover, it has the same units as the studied variable, so we can put into the context of our design process the obtained $RMSE$ and assess whether it is acceptable. For instance, in our example, $RMSE$ will be in centimeters and seconds for $H_{m0}$ and $T_m$, respectively. Computing this metric in our example, we obtain $RMSE(H_{m0})=0.65cm$ and $RMSE(T_{m})=0.016s$. If we see the magnitude of $RMSE$ with respect to the magnitude of the variables ($H_{m0}\in[5, 20]cm$ and $H=T_{m}\in[0.8, 1.8]s$), the error seems reasonable. 

But **which variable is better predicted by the model?** We would need an standardized GOF metric to this end.

### Coefficient of determination ($R^2$)

The coefficient of determination ($R^2$) is an standardized version of the $RMSE$, which the $MSE$ dimensionless using the variance of the observations as

$$
R^2=1-\frac{MSE}{Var(y)}=1-\frac{\sum_{i=1}^{N} (y_i - \hat  y_i)^2}{\sum_{i=1}^{N} (y_i - \overline  y)^2}
$$

where $\overline  y_i$ is the average of the observations.

Therefore, $0 \leq R^2 \leq 1$ represents the percentage of variance explained by the model and the higher, the better the performance of the model. The main advantage is that the value of the metric does not depend on the units of the variable easing the comparison process. 

Moreover, if the natural variability of the process is known, the $R^2$ can be interpreted into that context. For instance, if the natural variability of a phenomenon is around 5%, $R^2 \approx 95\%$ would represent a very accurate model. If the studied phenomenon is way more uncertain with variabilities up to 30%, $R^2 \approx 70\%$ would be a satisfactory model. 

If we compute this metric in our example, we obtain $R^2(H_{m0})=0.94$ and $R^2(T_{m})=0.68$. Using the $RMSE$, it was complicated to choose which variable was better modelled. With $R^2$, we can conclude that $H_{m0}$ is better modelled than $T_{m}$. Moreover, considering that the natural variability of waves is low, the performance for $H_{m0}$ is satisfactory while the performance or $T_{m}$ is reasonable.

## Bias

So far, the GOF metrics introduced were focused on quantifying the scatter of the predictions around the perfect fit. Another interesting aspect to quantify in our model is its bias. The bias is the systematic tendency of our model to under- or over-prediction. This is, how skewed the predictions of our model are and towards which side.

Between the existing bias metrics, we are going to introduce the relative bias ($rbias$).

### Relative bias ($rbias$)

The relative bias ($rbias$) is a standardized dimensionless measure of bias which can be computed as

$$
rbias = \frac{1}{N}\sum_{i=1}^{N}\frac{\hat y_i-y_i}{|y_i|}
$$

$rbias$ quantifies the mean ratio between the error and the absolute value of the variable. Therefore, $-1 \leq rbias \leq 1$ and the closer to 0, the better. If $rbias<0$, the predictions provided by the model are in average lower than the reference values, and viceversa. Therefore, $rbias$ gives us information about how much my model deviates from the reference values (magnitude of $rbias$) and the tendency of the model to under- or over-predict the studied variable (sign of $rbias$).

If we compute this metric for our example, we obtain $rbias(H_{m0})=0.05$ and $rbias(T_{m})=-0.09$. These results tell us that the model tends to slightly overpredict $H_{m0}$ and underpredict $T_{m}$.


[^reference]: Data extracted from Mares-Nasarre et al. (2022). Hydraulic stability of cube-armored mound breakwaters in depth-limited breaking wave conditions, *Ocean Engineering* 259, 111845.  https://doi.org/10.1016/j.oceaneng.2022.111845