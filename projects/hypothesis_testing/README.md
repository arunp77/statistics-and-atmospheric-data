# Comprehensive Hypothesis Testing in Python

## Overview

This project presents an end-to-end statistical hypothesis testing framework using Python. It covers exploratory data analysis, one-sample and two-sample tests, ANOVA, effect sizes, confidence intervals, non-parametric methods, and regression-based inference. Using a realistic synthetic dataset, the project emphasizes statistical assumptions, mathematical foundations, visual diagnostics, and practical interpretation beyond p-values. The work is designed as both a learning reference and a teaching-quality resource.

Rather than focusing on isolated tests, the project shows **how hypothesis testing fits into the full data analysis workflow**:

* exploratory data analysis
* assumption checking
* statistical testing
* effect size estimation
* confidence intervals
* interpretation and conclusions

---

## Objectives

The main goals of this project are to:

* Understand hypothesis testing from first principles
* Connect mathematical theory with Python implementations
* Learn when and why to use different statistical tests
* Go beyond p-values using effect sizes and confidence intervals
* Build a reusable reference for future statistical analyses

---

## Dataset Description

The project uses a **synthetic but realistic dataset** representing student performance and learning behavior.

### Features

| Variable          | Description                 |
| ----------------- | --------------------------- |
| `score`           | Final exam score (0–100)    |
| `study_hours`     | Average daily study time    |
| `attendance_rate` | Class attendance percentage |
| `previous_gpa`    | GPA before the course       |
| `gender`          | Student gender (M/F)        |
| `teaching_method` | Teaching method (A, B, C)   |
| `school_type`     | Public or private school    |
| `passed`          | Binary indicator of passing |

The dataset is intentionally designed to:

* contain real-world noise
* support multiple hypothesis tests
* include known effects for validation

---

## Project Structure

```
hypothesis-testing-python/
│
├── README.md
├── data/
│   └── student_performance.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_one_sample_tests.ipynb
│   ├── 03_two_sample_and_anova.ipynb
│   ├── 04_effect_size_and_ci.ipynb
│   ├── 05_non_parametric_tests.ipynb
│   └── 06_regression_hypothesis_testing.ipynb
│
├── src/
│   ├── data_generation.py
│   ├── effect_size.py
│   └── utils.py
│
└── requirements.txt
```

---

## Topics Covered

### 1. Exploratory Data Analysis (EDA)

* Summary statistics
* Distribution analysis
* Group-wise visualization
* Outlier detection
* Assumption awareness

### 2. One-Sample Hypothesis Testing

* One-sample t-test
* Manual computation of test statistics
* Sampling distributions
* Interpretation of results

### 3. Two-Sample Hypothesis Testing

* Independent t-tests
* Welch’s t-test
* Variance testing
* Mean difference confidence intervals

### 4. ANOVA

* One-way ANOVA
* F-statistic interpretation
* Post-hoc testing (Tukey HSD)
* Variance decomposition

### 5. Effect Size and Confidence Intervals

* Cohen’s d (one-sample and two-sample)
* Eta squared (ANOVA)
* Confidence intervals for means and differences
* Practical vs statistical significance

### 6. Non-Parametric Tests

* Mann–Whitney U test
* Kruskal–Wallis test
* When parametric assumptions fail

### 7. Regression as Hypothesis Testing

* Linear regression
* Coefficient-level hypothesis tests
* Confidence intervals for parameters
* Model interpretation

---

## Key Concepts Emphasized

* Null vs alternative hypotheses
* Type I and Type II errors
* Statistical vs practical significance
* Assumptions and diagnostics
* Effect size reporting
* Interpretation over mechanical testing

---

## Tools and Libraries

* Python 3.x
* NumPy
* Pandas
* SciPy
* Statsmodels
* Matplotlib
* Seaborn

---

## How to Run

1. Clone the repository
2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Open Jupyter Notebook
4. Start with:

   ```
   notebooks/01_eda.ipynb
   ```

Each notebook builds logically on the previous one.

---

## Intended Audience

This project is useful for:

* Data science and analytics students
* Researchers transitioning to Python-based statistics
* Engineers wanting deeper statistical understanding
* Interview or teaching preparation
* Personal reference for hypothesis testing

