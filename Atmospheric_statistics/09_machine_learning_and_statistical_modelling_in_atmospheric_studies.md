# Chapter - 9: Machine Learning and Statistical Modeling in Atmospheric Studies

Atmospheric science produces large, complex datasets—from satellite imagery and ground-based monitoring networks to aircraft campaigns. **Machine learning (ML)** and **statistical modeling** help extract patterns, make predictions, and understand complex relationships between atmospheric variables.

---

## 1. Introduction

Key objectives of ML/statistical modeling in atmospheric research:

* Predict atmospheric variables (e.g., ozone, PM2.5, VOCs)
* Identify relationships among variables
* Detect patterns, trends, or anomalies
* Support decision-making in air quality management or climate studies

**Types of models**:

1. **Statistical models**: Linear regression, generalized linear models, ARIMA (time-series), etc.
2. **Machine learning models**: Decision Trees, Random Forests, Gradient Boosting, K-Nearest Neighbors, Support Vector Machines, Neural Networks.

---

## 2. Preparing Atmospheric Data for ML

Before applying ML:

1. **Handle missing data**: Imputation or removal.
2. **Feature scaling**: Standardization or normalization for algorithms sensitive to magnitude (e.g., SVM, KNN).
3. **Train-test split**: Separate dataset to evaluate model performance.

Example in Python:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Simulate atmospheric dataset
np.random.seed(42)
n_samples = 200
temperature = np.random.normal(25, 3, n_samples)
humidity = np.random.uniform(40, 80, n_samples)
no2 = np.random.normal(30, 5, n_samples)
ozone = 0.4*temperature - 0.3*humidity + 0.5*no2 + np.random.normal(0, 2, n_samples)

df = pd.DataFrame({'Temperature': temperature, 'Humidity': humidity, 'NO2': no2, 'Ozone': ozone})

# Features and target
X = df[['Temperature','Humidity','NO2']]
y = df['Ozone']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## 3. Linear Regression

A simple, interpretable model for continuous atmospheric variables:

$$
y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p + \epsilon
$$

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
y_pred = lr.predict(X_test_scaled)

print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R²:", r2_score(y_test, y_pred))
```

**Applications**: Predict ozone or PM2.5 based on temperature, humidity, and precursor gases.

---

## 4. Decision Trees and Random Forests

Non-linear models that can capture complex interactions:

* **Decision Trees**: Split data based on feature thresholds.
* **Random Forests**: Ensemble of multiple trees for better generalization.

```python
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train_scaled, y_train)
y_rf_pred = rf.predict(X_test_scaled)

print("Random Forest RMSE:", np.sqrt(mean_squared_error(y_test, y_rf_pred)))
print("R²:", r2_score(y_test, y_rf_pred))
```

**Advantages**: Handle non-linearities, interactions, and noisy data; require minimal feature engineering.

---

## 5. Support Vector Machines (SVM) for Regression

SVM can perform **non-linear regression** using kernels:

```python
from sklearn.svm import SVR

svr = SVR(kernel='rbf')
svr.fit(X_train_scaled, y_train)
y_svr_pred = svr.predict(X_test_scaled)

print("SVM RMSE:", np.sqrt(mean_squared_error(y_test, y_svr_pred)))
print("R²:", r2_score(y_test, y_svr_pred))
```

**Applications**: Predicting atmospheric concentrations where relationships are non-linear.

---

## 6. Model Evaluation Metrics

1. **RMSE (Root Mean Squared Error)**: Sensitive to large errors.
2. **MAE (Mean Absolute Error)**: Robust to outliers.
3. **R² (Coefficient of Determination)**: Fraction of variance explained by the model.
4. **Cross-validation**: Ensures generalization by testing multiple train-test splits.

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(rf, X_train_scaled, y_train, cv=5, scoring='r2')
print("Random Forest cross-validated R²:", scores)
print("Mean R²:", scores.mean())
```

---

## 7. Feature Importance

Random Forests provide **feature importance**, useful for understanding which atmospheric variables influence predictions most:

```python
import matplotlib.pyplot as plt

importance = rf.feature_importances_
features = X.columns

plt.bar(features, importance)
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.title('Random Forest Feature Importance')
plt.show()
```

---

## 8. Time-Series Modeling (Optional)

For temporal atmospheric datasets:

* **ARIMA** or **SARIMA**: Forecasting based on past observations.
* **LSTM neural networks**: Advanced deep learning for long-term sequences.

---

## 9. Summary

* ML and statistical models are essential tools for **predicting, understanding, and analyzing atmospheric data**.
* **Linear models** are interpretable; **tree-based models** capture non-linearities.
* **SVM, Random Forests, and ensemble methods** improve predictive accuracy.
* **Feature importance** helps identify key drivers of atmospheric variables.
* Proper **train-test splitting, scaling, and cross-validation** ensure robust and reliable models.

**Learning outcomes**:

1. Prepare atmospheric datasets for ML/statistical analysis.
2. Apply linear and non-linear regression models to predict atmospheric variables.
3. Evaluate model performance using appropriate metrics.
4. Interpret feature importance to identify dominant atmospheric drivers.
5. Extend modeling to time-series predictions for dynamic atmospheric phenomena.

---

[Hands on practice notebook](09_machine_learning_and_statistical_modelling_in_atmospheric_studies.ipynb)
[Hands on practice notebook for interactive analysis](09_machine_learning_and_statistical_interactive.ipynb)
[To analyze chapter 8 and 9 together interactively](08_09_combined_interactive_atmoshpheric_analysis.ipynb)
