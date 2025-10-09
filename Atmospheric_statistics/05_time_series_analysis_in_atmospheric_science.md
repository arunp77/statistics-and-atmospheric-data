#  Chapter 5: Regression and Correlation Analysis in Atmospheric Science

Atmospheric data often come as continuous measurements over time, such as temperature, gas concentrations, wind speed, or satellite-observed parameters. Understanding temporal behavior is crucial to study trends, seasonal cycles, and anomalies in atmospheric processes.

## 1. Introduction to Time-Series Data

A **time-series** is a sequence of data points recorded at successive time intervals. Atmospheric data can have different temporal resolutions:

* **High-frequency data**: Seconds to minutes (e.g., aircraft instruments measuring VOCs, ozone, or temperature).
* **Daily/Monthly data**: Ground-based or satellite observations.
* **Long-term climate datasets**: Yearly or decadal averages.

**Key characteristics** of atmospheric time-series:

* **Trend**: Long-term increase or decrease in the dataset (e.g., rising CO₂ levels).
* **Seasonality**: Repeating patterns at fixed intervals (e.g., higher ozone in summer).
* **Noise/Randomness**: Short-term fluctuations caused by measurement variability or natural processes.
* **Outliers**: Sudden spikes or drops due to events (e.g., volcanic eruptions, instrument errors).

---

## 2. Data Preprocessing for Time-Series

Before analysis, time-series data often need preprocessing:

1. **Handling missing values**:

   * **Interpolation** (linear, spline) for continuous data.
   * **Forward/backward fill** for sensor gaps.

2. **Resampling and aggregation**:

   * Convert high-frequency data to daily/hourly averages if required.
   * Example in Python using Pandas:

```python
import pandas as pd

# Suppose df has datetime index and column 'O3'
df_daily = df['O3'].resample('D').mean()  # Daily mean
```

3. **Smoothing** (optional for visualization):

   * Moving average filters or low-pass filters to reduce short-term noise.

---

## 3. Visualizing Time-Series Data

Visualization is the first step in understanding trends and patterns.

* **Line plot**: Standard tool for continuous temporal data.
* **Seasonal plots**: Compare data across years/months.
* **Rolling statistics**: Plot rolling mean/median to highlight trends.

Example:

```python
import matplotlib.pyplot as plt

df['O3'].plot(label='Hourly O3')
df['O3'].rolling(window=24).mean().plot(label='24-hr rolling mean')
plt.xlabel('Time')
plt.ylabel('O3 Mixing Ratio [ppb]')
plt.title('Ozone Time-Series')
plt.legend()
plt.show()
```

---

## 4. Trend Analysis

### 4.1 Linear Trend

A simple first step is to fit a linear trend using regression:

$$
y(t) = \beta_0 + \beta_1 t + \epsilon
$$

Where:

* $y(t)$: atmospheric variable at time $t$
* $\beta_0$: intercept
* $\beta_1$: slope (rate of change per unit time)
* $\epsilon$: residual error

**Example in Python**:

```python
import numpy as np
from scipy.stats import linregress

t = np.arange(len(df_daily))
slope, intercept, r_value, p_value, std_err = linregress(t, df_daily.values)
print(f"Slope: {slope:.4f} per day")
```

**Interpretation**:

* Positive slope → increasing trend
* Negative slope → decreasing trend
* $p$-value < 0.05 → statistically significant trend

---

### 4.2 Seasonal-Trend Decomposition

Atmospheric data often combine **trend**, **seasonality**, and **noise**. The `statsmodels` library allows decomposition:

```python
from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(df_daily, model='additive')
result.trend.plot(title='Trend')
result.seasonal.plot(title='Seasonality')
result.resid.plot(title='Residuals')
```

* **Additive model**: $y(t) = \text{Trend} + \text{Seasonal} + \text{Residual}$
* **Multiplicative model**: $y(t) = \text{Trend} \times \text{Seasonal} \times \text{Residual}$ (useful if seasonal amplitude grows with trend)

---

## 5. Autocorrelation and Time Dependence

Many atmospheric processes exhibit temporal correlation.

* **Autocorrelation Function (ACF)**: Measures correlation of a variable with itself at different lags.
* **Partial Autocorrelation Function (PACF)**: Shows correlation at a lag excluding the effects of shorter lags.

```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(df_daily)
plot_pacf(df_daily)
```

**Usefulness**:

* Identify **memory** in the system (e.g., persistence of ozone after emission events).
* Inform time-series modeling (AR, MA, ARIMA).

---

## 6. Trend Significance Tests

To test whether a detected trend is significant:

* **Mann-Kendall Test**: Non-parametric test commonly used for environmental time-series.
* **Theil-Sen Estimator**: Robust slope estimator less sensitive to outliers.

```python
import pymannkendall as mk

trend_test = mk.original_test(df_daily)
print(trend_test)
```

**Output Interpretation**:

* `trend`: increasing/decreasing/no trend
* `p`: significance level
* `slope`: estimated rate of change

---

**Key learning outcomes**:

* Understand the difference between trend and seasonality.
* Apply statistical methods to detect trends.
* Interpret autocorrelation and residual behavior.
* Communicate findings clearly using plots and metrics.

---

## 8. Summary

* Time-series analysis is essential in atmospheric research.
* Proper preprocessing (missing values, resampling) is crucial.
* Visualizations reveal trends, seasonal cycles, and anomalies.
* Trend detection uses linear regression, decomposition, and significance tests.
* Autocorrelation informs persistence and memory in atmospheric systems.

This chapter provides a foundation for **more advanced topics**, such as forecasting atmospheric variables, anomaly detection, and predictive modeling using ARIMA or machine learning approaches.

