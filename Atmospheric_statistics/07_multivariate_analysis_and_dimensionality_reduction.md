# Chapter - 7 : Multivariate Analysis and Dimensionality Reduction in Atmospheric Data

Atmospheric datasets are often **high-dimensional**, containing multiple variables such as ozone, NO₂, VOCs, temperature, humidity, and wind speed. Analyzing these datasets requires **multivariate statistical techniques** to understand relationships, reduce dimensionality, and reveal hidden patterns.

---

## 1. Introduction

**Multivariate analysis** examines relationships among multiple variables simultaneously. It helps to:

* Identify correlated atmospheric variables.
* Detect underlying patterns (e.g., pollution sources or meteorological influences).
* Reduce dimensionality while preserving important information.

**Common scenarios in atmospheric research**:

* Studying correlations among trace gases and meteorological parameters.
* Identifying major factors controlling air quality.
* Reducing high-dimensional satellite or aircraft data to key components for modeling.

---

## 2. Correlation Analysis

Before advanced methods, we often start with **pairwise correlation**:

* **Pearson correlation**: Measures linear relationships.
* **Spearman correlation**: Measures monotonic relationships, robust to outliers.

Example in Python:

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Simulate a dataset
np.random.seed(0)
n_samples = 100
temperature = np.random.normal(25, 2, n_samples)
ozone = 0.5*temperature + np.random.normal(0, 1, n_samples)
no2 = np.random.normal(30, 5, n_samples)
voc = 0.8*no2 + np.random.normal(0,2, n_samples)

df = pd.DataFrame({'Temperature': temperature, 'O3': ozone, 'NO2': no2, 'VOC': voc})

# Correlation matrix
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Atmospheric Variables')
plt.show()
```

**Interpretation**:

* Strong positive correlation indicates related processes (e.g., temperature and ozone).
* Negative correlation may indicate competing factors or inverse relationships.

---

## 3. Principal Component Analysis (PCA)

High-dimensional atmospheric data can be **compressed** into a smaller number of variables while retaining most information.

### 3.1 PCA Concept

* PCA finds **new orthogonal axes (principal components)** along which the variance of the data is maximized.
* Each principal component is a **linear combination** of original variables:

$$
\text{PC}*1 = w*{11} X_1 + w_{12} X_2 + ... + w_{1p} X_p
$$

* The first few components often capture the majority of variability.

### 3.2 PCA Steps in Python

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)

# Plot PCA
plt.figure(figsize=(7,6))
plt.scatter(X_pca[:,0], X_pca[:,1])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA of Atmospheric Variables')
plt.show()
```

**Interpretation**:

* The **explained variance ratio** tells how much variability each component captures.
* Loadings indicate which variables contribute most to each principal component.

---

## 4. Factor Analysis (Optional)

**Factor analysis** assumes that observed variables are influenced by **latent factors**. It is useful for:

* Identifying hidden processes (e.g., pollution sources).
* Reducing noise while modeling relationships.

```python
from sklearn.decomposition import FactorAnalysis

fa = FactorAnalysis(n_components=2)
X_fa = fa.fit_transform(X_scaled)
```

---

## 5. Clustering and Multivariate Patterns

Multivariate analysis can reveal groups or patterns in the data:

* **K-Means clustering**: Groups similar observations based on multiple variables.
* **Hierarchical clustering**: Reveals nested clusters.

Example:

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, random_state=0)
clusters = kmeans.fit_predict(X_scaled)

plt.scatter(X_pca[:,0], X_pca[:,1], c=clusters, cmap='viridis')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Clustered Atmospheric Observations')
plt.show()
```

**Applications in atmospheric research**:

* Identifying regions with similar pollution levels.
* Grouping similar weather patterns or VOC plumes.

---

## 6. Multivariate Regression

Sometimes, we want to **predict one variable** based on others:

$$
y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_p X_p + \epsilon
$$

Example: Predicting ozone levels using temperature, NO₂, and VOC concentrations.

```python
from sklearn.linear_model import LinearRegression

X = df[['Temperature','NO2','VOC']]
y = df['O3']

model = LinearRegression()
model.fit(X, y)

print("Regression coefficients:", model.coef_)
print("Intercept:", model.intercept_)
```

---

## 7. Summary

* Multivariate analysis helps understand relationships among multiple atmospheric variables.
* **Correlation matrices** identify dependencies and potential redundancies.
* **PCA** reduces dimensionality, allowing visualization and simplification of high-dimensional datasets.
* **Factor analysis** and **clustering** uncover hidden structures or groupings.
* **Multivariate regression** enables predictive modeling of key variables.

**Learning outcomes** for students:

1. Identify relationships among atmospheric variables.
2. Reduce high-dimensional datasets to interpretable components.
3. Detect patterns, clusters, and key drivers of atmospheric phenomena.
4. Build multivariate models for prediction and analysis.

---

[Please check the related jupyter notebook for analysis]()
