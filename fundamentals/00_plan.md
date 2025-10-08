# Statistics

# Pacing and module map (standard 12-week plan)

* Week 0: Course intro, tools, and reproducibility
* Week 1: Probability basics and distributions
* Week 2: Descriptive statistics and exploratory data analysis
* Week 3: Measurement uncertainty, precision, and accuracy
* Week 4: Error propagation and confidence intervals
* Week 5: Hypothesis testing (t-test, chi-square, F-test)
* Week 6: Experimental design and one-way ANOVA
* Week 7: Two-way ANOVA, blocking, and factorial designs
* Week 8: Variance components and interactions
* Week 9: Regression (linear) and correlation
* Week 10: Nonlinear regression and parameter precision
* Week 11: Autocorrelation, time series basics, nonparametric tests
* Week 12: Review, project presentations, exam

You can collapse/expand modules to fit a shorter or longer term.

---

# Weekly lesson template (copy for each module)

**Module X — <Title>**

* **Learning objectives** (3–5 short bullets)
* **Prerequisites / prework** (readings, videos, short scripts)
* **Core concepts to cover** (bulleted list)
* **Step-by-step in-class plan**

  1. Quick recap of prior week (5–10 minutes)
  2. Conceptual lecture (20–40 minutes) — use 6–10 slides highlighting intuition and equations
  3. Live demo (20–30 minutes) — run the notebook and show visuals
  4. Short guided lab / paired exercise (20–30 minutes)
  5. Quick formative quiz or poll (5–10 minutes)
* **Notebook contents** (list cells: imports, data load, EDA, model, diagnostics, save outputs)
* **Assignment** (clear deliverable, data, and submission format)
* **Assessment & rubric** (how the assignment will be graded)
* **Estimated time** (lecture + lab + assignment workload)
* **Suggested datasets & tools** (Python libs, example datasets)
* **Further reading / references**

Use this template to create a single markdown file per week under `schedule/` for quick printing.

---

# Example: Module 1 (Probability basics and distributions)

* **Learning objectives**

  * Understand random variables, PMF/PDF, expectation and variance
  * Identify common distributions used in environmental science
  * Compute probabilities and apply Bayes theorem to a simple sensor problem

* **Prerequisites**: basic algebra; install `numpy`, `scipy`, `matplotlib`, `pandas`

* **Step-by-step plan**

  1. Start with everyday example: probability of rain and conditional probability.
  2. Introduce discrete vs continuous variables and the key distribution family members.
  3. Derive mean and variance for simple distributions and show sampling from them.
  4. Live demo: simulate rainfall and compute probabilities with NumPy and SciPy.
  5. Lab exercise: given synthetic sensor outputs, compute posterior probability using Bayes formula.

* **Notebook cells**: imports, random draws, pmf/pdf plotting, sampling variability demo, Bayes compute example, short exercise block.

* **Assignment (short)**: simulate sensor behavior for two pollutant sources and estimate posterior classification accuracy. Submit notebook and short writeup.

* **Estimated time**: lecture 50 minutes, lab 30 minutes, assignment 3–4 hours.

---

# Module-by-module quick checklist

For each module prepare these and tick them off before class:

* [ ] Slides (10–25 slides)
* [ ] Notebook (demo + exercises)
* [ ] Dataset prepared and small enough to version in repo
* [ ] One graded assignment or project step
* [ ] Short quiz (5 questions) for formative assessment
* [ ] Instructor solution and unit tests for automatic checks (optional)

---

# Assignments and assessments

* **Types**: weekly labs (30%), two midterm assignments (30%), final project or exam (30%), participation/quizzes (10%). Adapt as needed.
* **Deliverables**: Jupyter notebook (clear outputs), short PDF report (2–4 pages), code files if needed.
* **Rubric template** (example): correctness 50%, clarity & reproducibility 20%, explanation & interpretation 20%, code style 10%.

---

# Example assignment skeleton (use as a template)

**Title**: Analyzing measurement uncertainty in temperature sensors

**Background**: Brief context (2–3 sentences).
**Data**: `data/temperature_sensors.csv` (describe columns).
**Tasks**:

1. Compute summary statistics per sensor.
2. Estimate uncertainty for the mean using bootstrap and analytic formula.
3. Compare two sensors using an appropriate hypothesis test and interpret the result.
4. Submit: notebook + short PDF with conclusions.

**Grading**: include the rubric above.

---

# Teaching tips and reproducibility

* Always include a `requirements.txt` or `environment.yml` with exact package versions.
* Keep raw data separate from processed data.
* Use small synthetic datasets in class demos; link to larger raw datasets for projects.
* Encourage students to write a short reproducibility checklist in each submission (how to run notebook, random seeds).

---

# Final notes and next steps

If you want, I can:

* Expand any single module into a full week plan with complete lecture notes and a ready-to-run Jupyter notebook.
* Produce a slide template and assignment rubric as actual files to add to the repo.

Tell me which module to expand first and I will create the slide and notebook checklist for it.
