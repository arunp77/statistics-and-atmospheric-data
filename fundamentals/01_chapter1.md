# Module 0 — Introduction, Tools, and Reproducibility

## 🎯 Learning Objectives

* Understand what Environmental Statistics is and how it supports environmental science and policy.
* Learn the core computational tools for this course (Python, Jupyter, Git, etc.).
* Set up a reproducible analysis environment.
* Get comfortable with version control, documentation, and data management best practices.
* Practice running and documenting a simple analysis workflow.

---

## 1. What is Environmental Statistics?

Environmental Statistics applies statistical theory and data analysis to environmental data — such as air and water quality, climate variables, ecological counts, or satellite observations. It focuses on understanding **uncertainty**, **variability**, and **patterns** in environmental systems.

**Core questions addressed:**

* How certain are we about pollution levels in a city?
* How do rainfall, temperature, and vegetation interact?
* What is the confidence level in climate trend estimates?

**Key applications:**

* Climate change studies (trend analysis, anomaly detection)
* Water and air quality monitoring
* Environmental impact assessment
* Remote sensing data validation

---

## 2. Tools Overview

### 2.1 Python Stack

The course uses **Python** for data analysis and visualization. You’ll need:

* **Python 3.10+**
* **JupyterLab / Jupyter Notebook** (for interactive work)
* **Core libraries:**

  * `numpy` – numerical computing
  * `pandas` – data frames and time series
  * `matplotlib` / `seaborn` – plotting
  * `scipy.stats` – statistical analysis
  * `statsmodels` – regression, ANOVA, etc.
  * `xarray` / `netCDF4` – for gridded and environmental data

**Optional for advanced work:**

* `pingouin` (modern statistical tests)
* `geopandas`, `cartopy` (spatial data)

### 2.2 Environment Management

Use one of the following methods:

**Option 1: Conda (recommended)**

```bash
conda create -n es670 python=3.10 numpy pandas matplotlib seaborn scipy statsmodels jupyterlab
conda activate es670
```

**Option 2: Poetry (for reproducible dependency tracking)**

```bash
poetry init
poetry add numpy pandas matplotlib seaborn scipy statsmodels jupyterlab
```

### 2.3 Version Control with Git

**Key commands:**

```bash
git init
git add .
git commit -m "initial commit"
git remote add origin <repo_url>
git push -u origin main
```

Always include a `.gitignore` file to avoid committing large datasets or system files.

---

## 3. Reproducibility Foundations

Environmental research requires transparent and reproducible results. The main components are:

### 3.1 Reproducible Code

* Keep all analysis in Jupyter notebooks or Python scripts.
* Use consistent random seeds (`np.random.seed(42)`).
* Store configurations (e.g., file paths, constants) in a separate config file.

### 3.2 Reproducible Data

* Use versioned datasets with metadata.
* Keep raw data read-only; store processed versions separately.
* Document all preprocessing steps.

**Example folder layout:**

```
data/
├─ raw/
│  ├─ air_quality_2023.csv
├─ processed/
│  ├─ air_quality_clean.csv
scripts/
notebooks/
outputs/
```

### 3.3 Documentation

* Each notebook should have a short header: objective, data source, and output summary.
* Use markdown cells generously to explain rationale and interpretation.

**Example header snippet:**

```markdown
# Objective
Estimate mean PM2.5 concentration for 2024 and test if it exceeds WHO limits.

# Data
Source: EEA OpenAQ dataset (daily PM2.5, 2023–2024).

# Output
Summary statistics, CI plots, hypothesis test results.
```

### 3.4 Environment Capture

To ensure exact reproducibility, export the environment file:

```bash
conda env export > environment.yml
```

Or with Poetry:

```bash
poetry export -f requirements.txt --output requirements.txt
```

Include these files in your repository.

---

## 4. First Hands-on Task — Reproducible Mini Project

**Goal:** Create a small end-to-end workflow.

**Steps:**

1. Create a folder `es670_intro/` with subfolders `data/`, `notebooks/`, `results/`.
2. Download a small dataset, e.g., daily temperature for one station.
3. In a Jupyter notebook:

   * Load data with `pandas`.
   * Compute basic statistics (mean, median, std).
   * Plot daily temperature.
4. Save outputs (`figures/temp_trend.png`).
5. Document every step in markdown.
6. Commit everything to GitHub.

**Deliverable:**

* `notebooks/intro_temperature_analysis.ipynb`
* `requirements.txt`
* Screenshot of Git commit history.

---

## 5. Checklist for Students

✅ Python installed and working
✅ Jupyter Notebook opens successfully
✅ Git installed and basic commands tested
✅ Repo created and first commit made
✅ Environment file exported
✅ First simple analysis completed and reproducible

---

## 6. Suggested Reading

* *Good Enough Practices in Scientific Computing* — Wilson et al., PLOS Comp Bio, 2017.
* *Python Data Science Handbook* — Jake VanderPlas.
* *Reproducible Research with R and Python* — VanderWalt & Perktold.
* *Helsel & Hirsch (2002)* — *Statistical Methods in Water Resources* (for environmental case studies).

---

## 7. Instructor Notes

* Demonstrate live environment setup (Conda or Poetry) in class.
* Show how version control catches mistakes (rollback example).
* Discuss data ethics, transparency, and open science briefly.
* Encourage each student to create a personal repo (`es670_yourname`) for all weekly notebooks.

---

**Outcome:** By the end of this module, every student should be fully equipped to carry out reproducible analyses, version control their work, and understand the context of environmental statistics.
