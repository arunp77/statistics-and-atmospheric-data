# Chapter - 3 : Statistical Distributions in Atmospheric Data

### 1. Why Distributions Matter

When we talk about “average temperature” or “mean rainfall,” we implicitly assume we know what kind of **distribution** the data follow.
But in atmospheric science, the **shape** of the data’s probability distribution often carries more insight than the average itself.

For example:

* A rainfall dataset where most days are dry, but a few days have extreme storms — highly **skewed**, not Gaussian.
* Daily temperatures that oscillate around a mean — roughly **normal**, but with **seasonal modulation**.
* Aerosol concentrations — often **log-normal**, spanning several orders of magnitude.

Understanding these distributions helps you:

* Choose the right **statistical tests** (parametric vs. non-parametric)
* Accurately **model uncertainty**
* Detect **extreme events**
* Fit **probability models** to predict rare outcomes (e.g., 1-in-100-year floods)

---

### 2. The Concept of Probability Distributions

A **probability distribution** describes how likely different values of a variable are.

For continuous atmospheric variables, we define a **probability density function (PDF)**:

$$
\int_{-\infty}^{\infty} f(x) , dx = 1
$$

Where:

* $f(x)$ is the probability density
* The area under the curve between two points gives the probability of finding a value in that range

Atmospheric examples:

* $f(T) $: temperature distribution
* $ f(P)$: precipitation amount per day
* $f(AOD) $: aerosol optical depth

---

### 3. The Normal (Gaussian) Distribution

The **Normal Distribution** is central to classical statistics:

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right]
$$

**Key properties:**

* Symmetric around the mean $\mu$ 
* Characterized entirely by mean and standard deviation
* The “68–95–99.7 rule”:
  68% of data within 1σ, 95% within 2σ, 99.7% within 3σ

In atmospheric research, many **temperature**, **pressure**, and **wind speed anomalies** approximate normality — especially when averaged over time or space (by the Central Limit Theorem).

However, not everything is Gaussian — and assuming it blindly can lead to serious misinterpretation.

---

### 4. Non-Gaussian Distributions in the Atmosphere

Atmospheric data are often **non-linear**, **bounded**, or **multiplicative**, leading to **non-Gaussian** distributions.

| Distribution           | Common Atmospheric Example               | Shape Features                             |
| ---------------------- | ---------------------------------------- | ------------------------------------------ |
| **Log-normal**         | Aerosol number, trace gas concentrations | Skewed right; many small values, few large |
| **Gamma**              | Precipitation amount                     | Positive, right-skewed                     |
| **Exponential**        | Time between rain events                 | Decaying tail                              |
| **Weibull**            | Wind speed                               | Flexible shape, fits many climatologies    |
| **Beta**               | Cloud fraction, humidity (bounded 0–1)   | Bounded and flexible                       |
| **Power-law (Pareto)** | Extreme rainfall, lightning intensity    | Heavy-tailed, rare but impactful extremes  |

---

### 5. Skewness and Kurtosis

To quantify how a distribution deviates from normality, we use two higher-order moments:

| Metric       | Definition                              | Interpretation                                                 |
| ------------ | --------------------------------------- | -------------------------------------------------------------- |
| **Skewness** | $( \frac{E[(x - \mu)^3]}{\sigma^3} )$     | Positive → right tail (e.g., rainfall); Negative → left tail   |
| **Kurtosis** | $( \frac{E[(x - \mu)^4]}{\sigma^4} - 3 ) | >0 $ = heavy tails (leptokurtic); <0 = light tails (platykurtic) |

**Example:**

* Daily precipitation in a tropical site → high positive skewness
* Temperature anomalies → near zero skewness

Plotting PDFs or histograms is the first visual clue to such behavior.

---

### 6. The Log-Normal Example: Aerosols and Trace Gases

Atmospheric composition often varies over **orders of magnitude** — multiplicative processes (emission, growth, scavenging) yield **log-normal** distributions.

If $X$ is log-normally distributed, then $\ln(X) $ is normal.

**Properties:**

* Median < Mean < Mode
* Best analyzed on logarithmic scales
* Fits well for:

  * Aerosol optical depth (AOD)
  * Volatile Organic Compounds (VOCs)
  * Particle number concentration
  * Rain droplet diameters

**Practical Tip:**
Always visualize both *linear* and *log* histograms before fitting.

---

### 7. The Gamma and Exponential Distributions: Rainfall and Waiting Times

**Gamma distribution:**

$$
f(x; k, \theta) = \frac{1}{\Gamma(k)\theta^k} x^{k-1} e^{-x/\theta}
$$

* $k $ = shape parameter
* $\theta $ = scale parameter
* Commonly used for **rainfall intensities**, **precipitation accumulation**, **cloud water content**

When $k = 1 $, the gamma becomes **exponential**, useful for **time-between-events**, like dry spells or lightning intervals.

These distributions help define **return periods** for extreme weather.

---

### 8. The Weibull Distribution: Wind Speed Modeling

Wind speed is inherently non-negative and asymmetrical — best modeled by **Weibull**:

$$
f(x; k, c) = \frac{k}{c}\left(\frac{x}{c}\right)^{k-1} e^{-(x/c)^k}
$$

Where:

* $k$= shape parameter
* $c$ = scale parameter

Applications:

* Wind resource assessment
* Turbine energy potential estimation
* Extreme gust probability

A typical surface wind dataset fits $k \approx 2 $, $ c \approx 7 $ m/s.

---

### 9. Extreme Value Distributions

Atmospheric extremes — floods, heatwaves, cyclones — require **Extreme Value Theory (EVT)**.

Two main approaches:

* **Block Maxima (GEV distribution):**
  Take maxima per year (temperature, rainfall)
* **Peaks Over Threshold (GPD distribution):**
  Analyze exceedances beyond a high threshold

These methods estimate **return levels** — “the 100-year flood” — essential for risk management and climate adaptation.

---

### 10. Mixture and Multimodal Distributions

Atmospheric datasets often come from **multiple regimes**:

* Clear-sky vs. cloudy conditions
* Winter vs. summer seasons
* Marine vs. continental air masses

The combined PDF may appear **multimodal** — e.g., two peaks in temperature distribution.
Statistically, these can be modeled by **mixture models**:

$$
f(x) = \sum_i w_i f_i(x)
$$

where each $f_i(x)$ is a component (e.g., Gaussian for each regime).

**Application:**
Classifying air masses or aerosol types.

---

### 11. Testing for Normality

Before applying a parametric method (e.g., t-test, regression), check the data distribution.

Common tests:

* **Shapiro–Wilk test**
* **Kolmogorov–Smirnov test**
* **Anderson–Darling test**
* **Q–Q plots**

If the test rejects normality:

* Apply a **transformation** (e.g., log, sqrt)
* Or use **non-parametric** alternatives (e.g., Mann–Whitney test, Spearman correlation)

---

### 12. Fitting and Evaluating Distributions

1. **Visual check** — Histogram, PDF overlay, Q–Q plot
2. **Parameter estimation** — Maximum likelihood (MLE) or method of moments
3. **Goodness-of-fit tests** — Chi-square, KS test, AIC/BIC
4. **Interpretation** — Does the model make *physical* sense?

Example (Python-style workflow):

```python
from scipy.stats import gamma, norm, weibull_min
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("rainfall.txt")

params = gamma.fit(data)
x = np.linspace(0, max(data), 100)
plt.hist(data, bins=30, density=True, alpha=0.5, label="Observed")
plt.plot(x, gamma.pdf(x, *params), "r-", label="Gamma fit")
plt.legend()
```

---

### 13. Summary

* Atmospheric data often deviate from the normal distribution.
* Recognizing distribution shapes is crucial for correct model choice.
* Many physical processes (emissions, precipitation) yield skewed or heavy-tailed data.
* Statistical tools exist to describe, fit, and test these distributions.
* Always let *physics* guide your interpretation — statistics are descriptive, not prescriptive.

---

### 14. Suggested Reading

* Wilks, D. S. (2019). *Statistical Methods in the Atmospheric Sciences*.
* Katz, R. W. & Parlange, M. B. (1998). *Overdispersion Phenomena in Atmospheric Science Data*.
* Gilleland, E., Katz, R. W., & Worsley, K. J. (2009). *Extreme Value Theory for Meteorological Applications*.
* Panofsky, H. A. & Brier, G. W. (1968). *Some Applications of Statistics to Meteorology*.

