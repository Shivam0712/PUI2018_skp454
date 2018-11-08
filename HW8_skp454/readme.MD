### HW8

#### Assignment 1: Make a plot

The objective of this assignment is to make a well described reproducible plot:

![image](https://github.com/Shivam0712/PUI2018_skp454/blob/master/HW8_skp454/SubwayTimeSeries.png)

##### Fig1: Time series data of passengers' entries into MTA Subway

1. In the top left figure we see the original data of number of entries over time. This data has many repetative cycles in it alongwith some trend.

2. In top right figure we remove the yearly trend and the pattern stabilizes a bit. The weekly trend is fit over this data by taking average of last 7 days.

3. After removing the yearly and wekly trend, in bottom left figure we see the pattern completely stabilizes and represents the pattern of a white noise.

4. In bottom right figure when we superimpose our modelled data which is obtained by adding yearly and weekly trend for each day, we see the model data is able to explain much of the variation present in the actual data.

![image](https://github.com/Shivam0712/PUI2018_skp454/blob/master/HW8_skp454/Autocorr.png)

##### Fig2: Autocorrelation in Time Series data of Subway Entries

1. In the top figure we can see, in the original data for datewise entries, autocorrelation exist for both short and long periods of lag.

2. In the middle figure we can see, after removing the yealy trend, in the residual data, although the autocorrelation increased for short period of lags, the correlation for long period of lags were eliminated.

3. In the bottom figure we can see, after removing the yearly and weekly trend from the original data, the residual left is not autocorrelated to each other thus, the residual can be treated as white noise or stationary data.


#### Assignment2:

Write an article about our test on citibike data.
Url: https://www.authorea.com/336173/J8aO96wGiWBUwNuUuht9ig
