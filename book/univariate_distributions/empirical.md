# Empirical Distributions

As you can imagine, it is also possible to define a PDF and a CDF based on observations. In this section we will walk you through the process of constructing an empirical PDF and CDF.

## Step 1: Analyzing the data

As an example, let us consider a dataset of wind speeds close to Schiphol Airport. The figure below shows the wind speeds measured over 1 year. We can see that there are wind speeds between 0 m/s and about 18 m/s, and that there are some weak seasonal trends.


```{figure} https://files.mude.citg.tudelft.nl/data_overview.png
---
scale: 100%
name: data_wind

---
Time series of wind speed close to Schiphol Airport.
```

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_empirical_wind_speed.html
:name: empirical_wind_speed

Live read wind speeds at 10m height in Delft over the past year. Hover over the graph to highlight individual data points. If the graph only shows data from January to December 2024, the server is currently unreachable and a backup dataset has been loaded. <a href="https://open-meteo.com/">Weather data by Open-Meteo.com</a>. [^ref]
````

## Step 2: Computing the empirical CDF

As we have discussed in the previous sections, the CDF defines the non-exceedance probabilities for certain values of the random variable $x$, in this case: wind speed. In the empirical setting, this means that we need to assign to each observation a non-exceedance probability. To do so, we just need to sort the observations and compute the non-exceedance probabilities using the ranks. This is illustrated below with pseudo-code.

    read observations

    x = sort observations in ascending order

    length = the number of observations
    probability of not exceeding = (range of integer values from 1 \
                                    to length) / length + 1

    plot x versus probability of not exceeding 

Using the above algorithm, the following figure is obtained. Note that empirical CDFs are usually plotted using a step plot.

```{figure} https://files.mude.citg.tudelft.nl/ecdf_wind.png
---
scale: 75%
name: ecdf

---
Empirical cumulative distribution function of the wind speed data.
```

## Step 3: Computing the empirical PDF

It can be useful to also visualize the empirical PDF. As mentioned above, the PDF is the derivative of the CDF, leading to the following equation.

$$
f(x) = F'(x) = \lim_{\Delta x \to 0} \frac{F(x+\Delta x)-F(x)}{\Delta x}
$$

Thus, we can compute the empirical PDF assuming a bin size. To do so, we need to count the number of observations in each bin and calculate the relative frequency of each bin by dividing that count with the total number of observations. The density will be then those relative frequencies divided by the bin size. This process is illustrated with the following pseudo-code [^density].


    read observations

    #Assume the bin size
    bin_size = 2

    #Calculate the number of bins and the bin edges given the bin size
    min_value = minimum value of observations
    max_value = maximum value observations 
    n_bins = (max_value - min_value) / bin_size 
    bin_edges = range of n_bins + 1 values between the truncated value \
                of min_value and the ceiling value of max_value

    #Count the number of observations in each bin
    count = empty list
    for each bin:
        append the number of observations between the bin_edges to count

    #Compute relative frequencies
    freq = count / number of observations

    #Compute densities
    densities = freq / bin_size

    #plot epdf
    barplot densities

Using the above algorithm, the following figure is obtained. We can see that most of the density is concentrated between 2 and 9 m/s.

```{figure} https://files.mude.citg.tudelft.nl/epdf_wind.png
---
scale: 75%
name: epdf

---
Empirical probability density function of the wind speed data.
```

[^density]: Happily, in most coding languages, the algorithm to compute the pdf is already implemented and we just need to plot a histogram selecting the option to show us the densities.

[^ref]: The API data shown here are offered under Attribution 4.0 International (CC BY 4.0). Zippenfenig, P. (2023). Open-Meteo.com Weather API [Computer software]. Zenodo. https://doi.org/10.5281/ZENODO.7970649.

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre and Robert Lanzafame. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT