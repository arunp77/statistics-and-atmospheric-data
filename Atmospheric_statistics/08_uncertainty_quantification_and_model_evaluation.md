# Chapter - 8 : Uncertainty Quantification and Model Evaluation in Atmospheric Data

Atmospheric data and models are inherently uncertain due to **measurement errors, sampling limitations, model approximations, and natural variability**. Properly quantifying uncertainty and evaluating models is crucial for reliable interpretation, prediction, and decision-making in atmospheric research.

---

## 1. Introduction

**Key questions in uncertainty and model evaluation**:

* How confident are we in measured or modeled values?
* How well does a model reproduce observed data?
* Which sources of error dominate, and how can we reduce them?

Atmospheric datasets often require:

* **Propagation of measurement uncertainty** through analyses.
* **Assessment of predictive models** using error metrics and validation techniques.

---

## 2. Types of Uncertainty

1. **Aleatoric uncertainty (random)**:

   * Inherent variability in the atmosphere or measurement noise.
   * Example: short-term fluctuations in VOC measurements from an aircraft sensor.

2. **Epistemic uncertainty (systematic)**:

   * Due to incomplete knowledge, model assumptions, or calibration errors.
   * Example: uncertainty in emission factors or reaction rates in chemical transport models.

---

## 3. Quantifying Measurement Uncertainty

* **Standard deviation / variance**: Basic measure of spread.
* **Confidence intervals**: Range around mean where the true value likely lies.

Example (Python):

```python
import numpy as np

# Simulated ozone measurements
ozone = np.array([50.2, 49.8, 51.1, 50.5, 50.0])
mean_val = np.mean(ozone)
std_val = np.std(ozone, ddof=1)  # sample standard deviation
conf_interval = 1.96 * std_val / np.sqrt(len(ozone))  # 95% CI

print(f"Mean: {mean_val:.2f} ± {conf_interval:.2f} ppb (95% CI)")
```

---

## 4. Propagation of Uncertainty

When combining variables in formulas or models:

* **Error propagation formula (linear approximation)**:

$$
\sigma_f^2 = \sum_i \left( \frac{\partial f}{\partial x_i} \sigma_{x_i} \right)^2
$$

Where $\sigma_f$ is the uncertainty in $f(x_1,x_2,...,x_n)$ and $\sigma_{x_i}$ is the uncertainty in variable $x_i$.

* Example: Combining temperature and pressure measurements to calculate density.

---

## 5. Model Evaluation Metrics

After building a predictive model for atmospheric variables, it is essential to evaluate its performance.

### 5.1 Common Metrics

1. **Mean Absolute Error (MAE)**:

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|
$$

2. **Root Mean Squared Error (RMSE)**:

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}
$$

3. **Coefficient of Determination (R²)**:

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

**Python example**:

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Observed and predicted ozone values
y_obs = np.array([50.2, 49.8, 51.1, 50.5, 50.0])
y_pred = np.array([50.0, 50.2, 50.8, 50.3, 49.9])

mae = mean_absolute_error(y_obs, y_pred)
rmse = np.sqrt(mean_squared_error(y_obs, y_pred))
r2 = r2_score(y_obs, y_pred)

print(f"MAE: {mae:.3f}, RMSE: {rmse:.3f}, R²: {r2:.3f}")
```

---

### 5.2 Cross-Validation

* Split data into **training** and **testing** sets to avoid overfitting.
* **k-fold cross-validation** ensures robust evaluation by rotating training/testing partitions.

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

X = np.random.rand(100, 3)
y = X @ np.array([1.5, -2.0, 0.5]) + np.random.normal(0, 0.5, 100)

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print("Cross-validated R²:", scores)
```

---

## 6. Uncertainty in Model Predictions

* **Prediction intervals**: Range within which future observations are likely to fall.
* **Monte Carlo simulations**: Randomly perturb inputs based on uncertainty and propagate through the model.

```python
# Example: simple Monte Carlo for a linear model
n_sim = 1000
predictions = []
for _ in range(n_sim):
    X_perturbed = X + np.random.normal(0, 0.1, X.shape)
    model.fit(X_perturbed, y)
    predictions.append(model.predict(X_perturbed[0].reshape(1,-1))[0])

predictions = np.array(predictions)
mean_pred = predictions.mean()
ci_lower = np.percentile(predictions, 2.5)
ci_upper = np.percentile(predictions, 97.5)
print(f"Prediction: {mean_pred:.3f} [{ci_lower:.3f}, {ci_upper:.3f}] 95% CI")
```

---

## 7. Visualizing Uncertainty

* Use **error bars** for measurements.
* Use **shaded areas** for prediction intervals in time-series or spatial maps.

Example:

```python
time = np.arange(5)
plt.errorbar(time, y_obs, yerr=0.3, fmt='o', label='Observed ± uncertainty')
plt.plot(time, y_pred, 'r-', label='Predicted')
plt.fill_between(time, y_pred-0.5, y_pred+0.5, color='red', alpha=0.2, label='Prediction interval')
plt.xlabel('Time')
plt.ylabel('O3 [ppb]')
plt.legend()
plt.show()
```

---

## 8. Summary

* **Uncertainty** arises from measurement errors and model limitations.
* **Quantification** helps in interpreting confidence in data and model predictions.
* **Model evaluation metrics** (MAE, RMSE, R²) measure predictive performance.
* **Cross-validation and Monte Carlo simulations** improve reliability and estimate prediction intervals.
* Proper uncertainty quantification ensures **scientifically robust conclusions** in atmospheric research.

---

[Hands on practice notebook](08_uncertainty_quantification_and_model_evaluation.ipynb)