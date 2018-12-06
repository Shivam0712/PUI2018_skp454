
# PUI2018 HW 11

## ASSIGNMENTS:

### Assignment 1. Work with Time Series Data And Build Model to Classify Card Type. 
1. Analyze Time Series Patterns:
    1. Event Detection
    2. Trend Detection
2. Make Model to Identify Card type:
    1. Build Random Forest Classifier with 4 built Features.
    2. Build Random Forest Classifier with 194 time series Features.
    3. Produce Confusion Matrix, Classification Report and Feature Importance.
  
### Assignment 2. Improve your plot from HW8 based on the feedback you recieved from your classmates (let me know if you did not recieve feedback and I will comment on your original plot)

1. Updated the plot as per suggestions recieved from peers. The updated plot and caption is added below.
2. The [notebook](https://github.com/Shivam0712/PUI2018_skp454/blob/master/HW11_skp454/HW8_Assignment1_skp454-Copy1.ipynb) used to prepare this plot contains the MD text for how suggestion from peers were incorporated in the plot.  

![](https://github.com/Shivam0712/PUI2018_skp454/blob/master/HW11_skp454/MTA%20Entries.png)
#### Fig: Time series data of passengers' entries into MTA Subway
1. The figure shows an attempt to model daywise MTA Subway entries as sum of past 1 Year and past 7 day moving average.  
2. In the top left figure we see the original data of number of entries over time with past 1 year moving average.
3. In top right figure we remove the past 1 year moving average. Past 1 week moving average is calculated on the residual.
4. After removing the past 1 year and 1 week moving average, in bottom left we see the final residual left.
5. In bottom right figure we superimpose our modelled data which is obtained by adding past 1 year and 1 week moving average, we see the model data is able to explain much of the variation present in the actual data.






