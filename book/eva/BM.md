
# Block Maxima

Block maxima consists of defining a time block, for instance a year, and selecting the maximum observation within that time block. Thus, the number of sampled extremes would be equal to the number of blocks. 

Let's apply it to our time series. We are going to use a block = 1 year, so we will obtain 20 extreme observations for the subsequent phases of our analysis. In the figure below, you can see how the application of this method looks.

```{figure} https://files.mude.citg.tudelft.nl/BlockMaxima.png

---

---
Application of Block Maxima to $H_s$ time series with a time block of 1 year (Yearly Maxima).
```

## Advantages and considerations for use

Typically, in the Civil Engineering field, time blocks of 1 year are used, since natural phenomena with annual seasonality are usually studied (e.g., wave storms or floods). This also simplifies the quantification of yearly exceedance probabilities, as you will see in subsequent sections.

When introducing the concept of $RT$, we saw that one of the basic assumptions of EVA was that extremes follow a Bernoulli process and, thus, are independent and identically distributed (*iid* conditions). This implies that when sampling our extremes, we need to ensure that they are independent. At this point is where Block Maxima has a great advantage: if the time block is long enough, we can guarantee that the sampled observations are independent. For instance, if we use Yearly Maxima (one observation each year), we can be sure that the extreme observation of the year $y$ is independent from the extreme observations in years $y-1$ and $y+1$. Also, it is very easy to implement.

```{admonition} Block Maxima
:class: tip

Advantages:
- Easy to guarantee that sampled extremes are *iid*.
- Simple implementation and coding.

Disadvantages:
- Only one observation per block, so we may be neglecting extreme observations located within the same time block.
- Not appropriate for short time series.
```

## Let's code it

In order to exemplify how to actually implement Block Maxima,pseudo code is presented.

### Pseudo code

    read observations

    for each year i:
        obs_max[i] = maximum observations in year i
    end

