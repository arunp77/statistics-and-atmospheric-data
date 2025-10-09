# Chapter - 6 : Spatial Statistics and Geostatistics in Atmospheric Data

Atmospheric phenomena—like ozone concentrations, VOCs, or temperature—vary not only in time but also across **space**. Understanding spatial variability is essential for analyzing patterns, predicting values at unmeasured locations, and designing observational networks.

---

## 1. Introduction to Spatial Data

**Spatial data** represents variables measured over geographic locations. In atmospheric science, spatial data may come from:

* Ground-based stations (air quality monitoring networks)
* Aircraft campaigns (VOC measurements at different latitudes/longitudes)
* Satellite observations (global ozone, NO₂, temperature maps)

**Types of spatial data**:

1. **Point data**: Measurements at specific coordinates (e.g., ozone sensors at cities).
2. **Gridded data**: Regularly spaced measurements (e.g., satellite images, climate reanalysis).
3. **Irregular data**: Non-uniform spatial sampling (common in aircraft campaigns or field surveys).

**Key questions in spatial analysis**:

* Are there regions with systematically higher or lower values?
* How do measurements at nearby locations relate?
* Can we predict the variable at locations with no measurements?

---

## 2. Spatial Descriptive Statistics

### 2.1 Measures of Central Tendency and Dispersion

Similar to standard statistics, but applied **spatially**:

* **Mean**: Average over all locations
* **Variance**: Measure of spatial variability
* **Skewness/Kurtosis**: Identify asymmetry or heavy tails in spatial distributions

Example using Python:

```python
import numpy as np

values = np.array([10.5, 12.3, 11.2, 13.1])  # e.g., ozone at 4 locations
mean_val = np.mean(values)
std_val = np.std(values)
print(f"Mean: {mean_val}, Std Dev: {std_val}")
```

---

### 2.2 Spatial Autocorrelation

Nearby locations are often more similar than distant ones. **Spatial autocorrelation** quantifies this:

* **Moran's I**: Global measure of spatial correlation

$$
I = \frac{N}{W} \frac{\sum_i \sum_j w_{ij} (x_i - \bar{x})(x_j - \bar{x})}{\sum_i (x_i - \bar{x})^2}
$$

Where:

* $x_i$ = variable at location $i$

* $w_{ij}$ = spatial weight between locations $i$ and $j$

* $N$ = number of locations, $W$ = sum of all $w_{ij}$

* **Interpretation**:

  * $I > 0$ → positive spatial autocorrelation (clusters of similar values)
  * $I < 0$ → negative autocorrelation (neighbors dissimilar)
  * $I \approx 0$ → random spatial pattern

* **Python example** using `pysal`:

```python
import libpysal
from esda.moran import Moran

# coordinates and values
coords = [(0,0), (0,1), (1,0), (1,1)]
values = [10, 12, 11, 13]

w = libpysal.weights.DistanceBand(coords, threshold=1.5)
moran = Moran(values, w)
print(f"Moran's I: {moran.I}, p-value: {moran.p_sim}")
```

---

## 3. Variograms and Geostatistics

**Geostatistics** deals with **modeling spatial dependence** and predicting values at unmeasured locations.

### 3.1 Variogram

A **variogram** measures how data similarity decreases with distance:

$$
\gamma(h) = \frac{1}{2N(h)} \sum_{i,j | d_{ij} = h} \big( x_i - x_j \big)^2
$$

Where:

* $h$ = lag distance
* $x_i, x_j$ = values at locations $i, j$ separated by $h$

**Interpretation**:

* **Nugget**: Variability at very small scales (measurement noise)
* **Sill**: Variance plateau at large distances
* **Range**: Distance at which autocorrelation becomes negligible

**Python example** using `scikit-gstat`:

```python
from skgstat import Variogram
import numpy as np

coords = np.array([[0,0],[0,1],[1,0],[1,1]])
values = np.array([10,12,11,13])
V = Variogram(coords, values)
V.plot()
```

---

### 3.2 Kriging: Spatial Interpolation

**Kriging** is a powerful geostatistical method to estimate variable values at unmeasured locations:

1. Fit a variogram model to the data
2. Predict values using weighted linear combination of observed points

**Types**:

* **Ordinary Kriging**: Assumes unknown but constant mean
* **Universal Kriging**: Accounts for trends in mean
* **Indicator Kriging**: Used for categorical or thresholded data

Example workflow:

```python
from pykrige.ok import OrdinaryKriging
import numpy as np

x = np.array([0,0,1,1])
y = np.array([0,1,0,1])
z = np.array([10,12,11,13])

OK = OrdinaryKriging(x, y, z, variogram_model='linear')
gridx = np.linspace(0,1,10)
gridy = np.linspace(0,1,10)
z_pred, ss = OK.execute('grid', gridx, gridy)
```

**Applications in atmospheric science**:

* Estimate pollutant concentrations at unmonitored locations
* Fill gaps in aircraft campaign datasets
* Produce high-resolution pollutant maps for health studies

---

## 4. Spatial Pattern Detection

* **Hotspot Analysis**: Identify areas of unusually high or low values
* **Cluster detection**: e.g., high VOC plumes from industrial regions
* Tools: `Moran’s I`, `Getis-Ord Gi*` statistics

---

## 5. Practical Example: VOC Mixing Ratios over a Region

Suppose an aircraft measured **isoprene mixing ratios** at scattered locations:

1. Compute **spatial mean** and **standard deviation**
2. Check **autocorrelation** using Moran’s I
3. Fit **variogram** and determine nugget, sill, and range
4. Perform **ordinary kriging** to predict values on a fine lat-lon grid
5. Visualize as a **heatmap** or **contour plot**

This workflow teaches students to combine **exploratory spatial analysis**, **statistical modeling**, and **prediction**.

---

## 6. Summary

* Atmospheric data have spatial structure; analyzing it requires **spatial statistics**.
* **Descriptive spatial statistics** and **autocorrelation** reveal patterns.
* **Variograms** quantify spatial dependence.
* **Kriging** allows prediction at unobserved locations.
* This knowledge is foundational for creating **maps**, **interpolated datasets**, and **spatial models** in atmospheric research.

Please checkout the jupyter notebook: [jupyter notebook](06_spatial_statistics_and_geostatistics.ipynb)