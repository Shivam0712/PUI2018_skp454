### Task: Review Plot of a fellow classmate

#### Plot Reviewed:

<img src="https://github.com/ShellyYoon/PUI2018_yy2908/blob/master/HW8_yy2908/2016.png">
<img src="https://github.com/ShellyYoon/PUI2018_yy2908/blob/master/HW8_yy2908/2017.png">
<img src="https://github.com/ShellyYoon/PUI2018_yy2908/blob/master/HW8_yy2908/compare.png">
<img src="https://github.com/ShellyYoon/PUI2018_yy2908/blob/master/HW8_yy2908/changes.png">

There are 4 plots to be reviewed.

1. In the plots, 311 noise data constrained to NYC from the platform NYC Open Data is used. The data in 2016 is compared to that of 2017, to measure the change.

2. The plots are not clear to understand as they miss labels and scales for axes and, the plot titles.

3. In plot 1 2 and 3, the purpose for using a line for zipcode is unknown.

4. The choice of using line chart for this data seems to be incorrect as their is no continous series like time on the x-axis.

5. In plot 4, the title 'Changes in log 2016 vs log 2017' is ambigious and not interpretable.

Suggestion to improve the plot:

As it appears from the code, we are trying to fulfill following objectives by the use of plots.

1. Map the number of noise complaints by zipcodes in years 2016 and 2017.
2. Map the difference in number of noise complaints between years 2016 and 2017.
3. Make a scatter plot of number of noise complaints in years 2016 and 2017, where each dot will represent a zipcode.

To better fulfill these objectives what can be done is:

1. For objective 1, use shapefile of zipcodes to make 2 choropleths with non-divergent color scheme.
These 2 choropleths should represent the log of number of noise complaints in years 2016 and 2017.
Alongwith these choropleths, make 2 histograms showing the distribution of number of complaints for different zipcodes in year 2016 and year 2017.

2. For objective 2, use shapefile of zipcode to make a choropleth with a divergent color scheme.
This choropleth should represent the difference in noise complaints between years 2016 and 2017 in different zipcodes.
Alongwith the choropleth, also provide a histogram to show the distribution of this difference.

3. For objective 3, the current plot4 is correct.
Please add labels to x and y axis so, that it is clear which axis represent which year.
Also, use a proper title so that meaning of the plot is clear.

For all these plots:
1. Please add labels to x and y axis.
2. Please add an appropriate title.
3. Please add a caption defining what is been shown in the plot and why.
