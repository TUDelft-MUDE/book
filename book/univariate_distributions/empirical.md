# Empirical Distributions

As you can imagine, it is also possible to define a PDF and a CDF based on observations. In this section we will walk you through the process of constructing an empirical PDF and CDF.

## Step 1: Analyzing the data

As an example, let us consider a dataset of wind speeds in Delft. The figure below shows wind speed estimates in Delft at 10m height over the past year[^ref]. To the right of the time series is a **histogram** of the wind speeds. Observe how some wind speeds are more common than others.

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
:aspectratio: 2 / 1

Wind speed estimates at 10m height in Delft over the past year. Hover over the graph to highlight individual data points. This element, and all subsequent elements on this page, access the latest available wind speed data from an online resource. If you come back later, these plots may look different. [^ref]
````

## Step 2: Computing the empirical PDF

A histogram can fulfill a similar purpose to a PDF, but instead of continuous probability densities it displays the **frequency** of events in a certain discrete value range. We have discussed in the previous section how the probability to obtain a sample in a value between $x_1$ and $x_2$ can be obtained from the CDF as
$F(x_2)-F(x_1)$. When working with a finite set of samples, we can compute the discrete interval probability $P(x_1 < x \leq x_2)$ from the histogram by dividing the counts in each bin by the total number of data points. This process is illustrated with the following pseudo-code [^density].


    read observations

    #Assume the bin size
    bin_size = 2

    #Calculate the number of bins and the bin edges given the bin size
    min_value = minimum value of observations
    max_value = maximum value of observations 
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

The element below illustrates the resulting histogram: 

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_empirical_wind_speed_pdf.html
:name: empirical_wind_speed_pdf
:aspectratio: 1 / 1

Empirical PDF derived from wind speed estimates at 10m height in Delft over the past year. Hover over the bars to highlight the interval probabilities. [^ref]
````                                

## Step 3: Computing the empirical CDF

As we have discussed in the previous sections, the CDF defines the non-exceedance probabilities for certain values of the random variable $x$, in this case: wind speed. In the empirical setting, this means that we need to assign to each observation a non-exceedance probability. In this instance, we are neglecting the time dimension, and sort the hourly wind speed measurements in ascending order, which assigns to each data point its corresponding rank.

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_empirical_wind_speed_sorting.html
:name: empirical_wind_speed_sorting
:aspectratio: 2 / 1

Wind speed estimates at 10m height in Delft over the past year. Click the button on the right to sort the data set. The red vertical lines demarkate the latest wind speed estimate in Delft. [^ref]
````

If we assume that our data set represent **independent and identically distributed** (i.i.d.) samples from the underlying distribution, we can derive the empirical non-exceedance probabilities by sorting the data and computing the non-exceedance probabilities from their rank.

To do so, we just need to sort the observations and compute the non-exceedance probabilities using the ranks. This is illustrated below with pseudo-code.

    read observations

    length = number of observations

    x = sort observations in ascending order
    rank = range of integer values from 1 to length

    probability of not exceeding = (range of integer values from 1 to length) / length + 1

    plot x versus probability of not exceeding 

Using the above algorithm, the following figure is obtained. Note that empirical CDFs are usually plotted using a step plot to highlight their empirical nature. From this plot, we can read the non-exceedance probability of the latest wind speed estimate in Delft (since this plot is updated dynamically, you may see a different number when you next load this page). 

% START-CREDIT
% source: maxramgraber
````{margin}
```{attributiongrey} Attribution
:class: attribution
This interactive figure is created by Max Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
````
% END-CREDIT

````{iframe-figure} ../_static/elements/element_empirical_wind_speed_cdf.html
:name: empirical_wind_speed_cdf
:aspectratio: 1 / 1

Empirical CDF derived from wind speed estimates at 10m height in Delft over the past year. Hover over the graph to highlight individual data points. Note that the wind speed is now plotted on the x-axis. The red vertical lines demarkate the latest wind speed estimate in Delft. [^ref]
````

[^density]: Happily, in most coding languages, the algorithm to compute the pdf is already implemented and we just need to plot a histogram selecting the option to show us the densities.

[^ref]: <a href="https://open-meteo.com/">Weather data by Open-Meteo.com</a>. The API data shown here are offered under Attribution 4.0 International (CC BY 4.0). If the graph only shows data from January to December 2024, the server is currently unavailable and a backup dataset has been loaded. 

% START-CREDIT
% source: distributions
```{attributiongrey} Attribution
:class: attribution
This chapter was written by Patricia Mares Nasarre, Robert Lanzafame, and Maximilian Ramgraber. {ref}`Find out more here <distributions_credit>`.
```
% END-CREDIT