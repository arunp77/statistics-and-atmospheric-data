# Chapter - 4 : Correlation and Regression in Atmospheric Variables

### 1. Why Relationships Matter

Atmospheric systems are **interconnected**. Temperature affects humidity, humidity affects cloud formation, and clouds influence radiation and precipitation.
To understand or predict these processes, we need to **quantify relationships** between variables.

Statistics provides two key tools:

* **Correlation** — measures the *strength* and *direction* of association.
* **Regression** — builds a *predictive model* for one variable based on others.

These concepts are central to:

* Climate trend detection (e.g., CO₂ vs Temperature)
* Model validation (satellite vs ground data)
* Process studies (ozone vs NO₂, AOD vs humidity)
* Forecasting (rainfall vs SST anomalies)

---

### 2. Correlation: Measuring Association

#### 2.1 Pearson Correlation (Linear)

$$
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
$$

* Measures **linear** association between $X$ and $Y$.
* Range = −1 (perfect negative) → +1 (perfect positive).
* ( r ≈ 0 ) → no linear relationship.

**Example:**
Daily temperature and ozone concentrations may show ( r ≈ 0.7 ): warm days often have higher ozone.

**Limitations:** Sensitive to outliers, assumes linearity and normality.

#### 2.2 Spearman Rank Correlation (Monotonic)

* Based on ranks rather than raw values.
* Captures **monotonic** but non-linear relationships.
* Robust to non-normal and skewed data.

**Example:**
Cloud fraction vs. solar radiation — relationship is monotonic but not linear.

#### 2.3 Kendall’s Tau

* Measures concordance between ranked pairs.
* Good for small samples and ordinal data.

---

### 3. Visualizing Correlations

Plots are indispensable for diagnosing relationships.

| Plot type         | Purpose                              | Typical use                  |
| ----------------- | ------------------------------------ | ---------------------------- |
| **Scatter plot**  | Visualize linear/nonlinear trends    | Temp vs O₃                   |
| **Heatmap**       | Matrix of correlation coefficients   | Multi-variable diagnostics   |
| **Pair plot**     | Pairwise scatter plots for many vars | Exploratory analysis         |
| **Time-lag plot** | Correlation across lags              | SST anomaly vs precipitation |

```python
import seaborn as sns, pandas as pd
sns.heatmap(df.corr(), cmap="coolwarm", annot=True)
```

---

### 4. Regression: Quantifying Functional Relationships

While correlation measures association, **regression** *models* how one variable depends on another.

#### 4.1 Simple Linear Regression

$$
y = \beta_0 + \beta_1 x + \epsilon
$$

* $\beta_0$ = intercept, $ \beta_1$ = slope.
* $R^2$ measures proportion of variance in $Y$ explained by $X$.
* Test slope significance with $p-$value.

**Example:**
Modeling ozone concentration as a linear function of solar radiation.

Interpretation:

* $\beta_1 > 0 $: ozone rises with radiation.
* $ R^2 = 0.64 $: 64 % of ozone variability explained.

#### 4.2 Multiple Linear Regression

$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \epsilon
$$

Useful when several predictors influence one variable.

Example:
$$
\text{O₃} = \beta_0 + \beta_1 (\text{T}) + \beta_2 (\text{NO₂}) + \beta_3 (\text{Wind}) + \epsilon
$$

Interpret the sign and magnitude of each coefficient physically.

---

### 5. Model Diagnostics

Before trusting a regression, always test its assumptions:

| Check                      | Why it matters                                | Tools                           |
| -------------------------- | --------------------------------------------- | ------------------------------- |
| **Linearity**              | Relationship between X and Y should be linear | Scatterplot, residual vs fit    |
| **Homoscedasticity**       | Constant variance of residuals                | Residual plot                   |
| **Normality of residuals** | Valid p-values                                | Q–Q plot                        |
| **Independence**           | No autocorrelation in time series             | Durbin–Watson test              |
| **Multicollinearity**      | Predictors not strongly correlated            | VIF (Variance Inflation Factor) |

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
```

---

### 6. Beyond Linearity

Atmospheric processes are often **non-linear**:

* Radiation scales exponentially with temperature (Stefan–Boltzmann).
* Chemical reactions depend non-linearly on precursors.

Alternatives:

| Model                                          | Notes                                              |
| ---------------------------------------------- | -------------------------------------------------- |
| **Polynomial regression**                      | Adds curvature (e.g., quadratic ozone vs T).       |
| **Generalized Linear Models (GLM)**            | Allows non-normal distributions.                   |
| **Log/log-transform**                          | Converts multiplicative relationships to additive. |
| **Non-parametric regression (LOESS, splines)** | Smooths non-linear trends.                         |

---

### 7. Lagged and Cross-Correlation

Atmospheric variables often influence each other **with time delay**.

**Cross-correlation function (CCF):**

$$
\rho_{xy}(k) = \frac{E[(x_t - \bar{x})(y_{t+k} - \bar{y})]}{\sigma_x \sigma_y}
$$

Identifies time lags between two series.

**Example:**
SST anomaly leading monsoon rainfall by 2 months → predictive signal.

---

### 8. Spatial Correlation

Spatial data (satellite grids, station networks) exhibit **spatial autocorrelation**.

* Nearby points more similar than distant ones.
* Violates independence assumption.
* Quantified using **Moran’s I**, **semivariograms**, or **spatial correlation functions**.

**Implication:**
Statistical significance must account for *effective degrees of freedom* — otherwise, correlations appear artificially high.

---

### 9. Partial and Multiple Correlation

To isolate effects:

$$
r_{xy.z} = \frac{r_{xy} - r_{xz} r_{yz}}{\sqrt{(1-r_{xz}^2)(1-r_{yz}^2)}}
$$

**Example:**
Remove temperature influence when analyzing O₃–NO₂ correlation.
Essential in atmospheric chemistry and climatology, where variables are interdependent.

---

### 10. Nonlinear and Machine Learning Extensions

Regression ideas extend naturally to more flexible methods:

* **Decision Trees / Random Forests:** non-linear, interpretable variable importance.
* **Neural Networks:** complex relationships, good for forecasting.
* **Support Vector Regression:** robust to outliers.

But the philosophy remains the same — identify **statistical dependence**, quantify **predictive power**, and ensure **physical plausibility**.

---

### 11. Example: Modeling Ground-Level Ozone

Goal: Estimate O₃ (ppb) using temperature, solar radiation, and wind speed.

1. Collect daily data (n = 365).
2. Compute correlation matrix → choose predictors with |r| > 0.3.
3. Fit multiple linear regression.
4. Check residuals for autocorrelation and non-linearity.
5. Report:

   * Coefficients ± standard errors
   * $R^2$ and RMSE
   * Physical interpretation (e.g., +2.1 ppb O₃ per °C)

This example blends statistical modeling with process understanding — what drives ozone formation.

---

### 12. Summary

* Correlation quantifies association; regression models dependence.
* Check assumptions — independence, linearity, residual behavior.
* Use transformations or non-linear models where appropriate.
* Interpret coefficients **in physical context**, not just numerically.
* Temporal and spatial correlations require special care.

---

### 13. Suggested Reading

* Wilks, D. S. (2019). *Statistical Methods in the Atmospheric Sciences.*
* von Storch & Zwiers (1999). *Statistical Analysis in Climate Research.*
* Emery & Thomson (2017). *Data Analysis Methods in Physical Oceanography.*
* Salby, M. L. (1996). *Fundamentals of Atmospheric Physics* — Ch. 7 (Data Relationships).


