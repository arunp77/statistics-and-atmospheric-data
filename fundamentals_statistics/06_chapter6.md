# Inferential Statistics

Inferential statistics, on the other hand, is the branch of statistics that deals with drawing conclusions or making predictions about a larger population based on a sample of data. It involves using probability theory to estimate population parameters (e.g., mean, proportion) from sample statistics (e.g., sample mean, sample proportion) and testing hypotheses about the relationship between variables. Inferential statistics aims to make generalizations about the population based on the information obtained from the sample.`

### Main uses of the Inferential statistics

Inferential statistics is used to make generalizations and predictions about populations based on sample data. Some of the main uses of inferential statistics are:

1. **Estimation:** Inferential statistics can be used to estimate population parameters (such as the mean or proportion) based on sample data.
2. **Hypothesis testing:** Inferential statistics can be used to test hypotheses about population parameters using sample data.
3. **Prediction:** Inferential statistics can be used to make predictions about future observations or outcomes based on past data.
4. **Generalization:** Inferential statistics can be used to generalize findings from a sample to the larger population.
5. **Decision-making:** Inferential statistics can be used to support decision-making in various fields, such as business, medicine, and social sciences.

Overall, inferential statistics allows researchers to draw conclusions about populations based on sample data, which can be used to make informed decisions and predictions.

### Descriptive versus inferential statistics

| Descriptive Statistics	| Inferential Statistics |
|---------------------------|------------------------|
| Describes sample data	| Makes inferences about population based on sample data |
| Provides summary measures such as mean, median, mode, standard deviation, etc.	| Uses sample statistics to estimate population parameters |
| Helps in data exploration and visualization	| Tests hypotheses about population parameters |
| Useful in describing and summarizing data	| Helps in making predictions about future observations or outcomes |
| Examples: frequency distributions, measures of central tendency, measures of dispersion, etc.	| Examples: t-tests, ANOVA, regression analysis, etc. |

### Types of estimates
There are two important types of estimates you can make about the population: 

1. **Point estimates:** A point estimate is a single value estimate of a parameter. For instance, a sample mean is a point estimate of a population mean.
2. **Interval estimates:** An interval estimate gives you a range of values where the parameter is expected to lie. A confidence interval is the most common type of interval estimate.

Both types of estimates are important for gathering a clear idea of where a parameter is likely to lie.

---

## Hypothesis testing

- Hypothesis testing is a formal process of statistical analysis using inferential statistics. The goal of hypothesis testing is to compare populations or assess relationships between variables using samples. 

- Hypotheses, or predictions, are tested using statistical tests. Statistical tests also estimate sampling errors so that valid inferences can be made.

- Statistical tests can be:

    - **Parametric**: parametric tests are considered more statistically powerful because they are more likely to detect an effect if one exists. Parametric tests make assumptions that include the following:
        - the population that the sample comes from follows a normal distribution of scores
        - the sample size is large enough to represent the population
        - the variances, a measure of variability, of each group being compared are similar
        - Example: t-test, ANOVA, Regression analysis, Pearson correlation coefficient.
        - **t-test:** Used to compare the means of two groups when the data are normally distributed and the variances of the two groups are equal.
        - **ANOVA:** Used to compare the means of three or more groups when the data are normally distributed and the variances of the groups are equal.
        - **Regression analysis:** Used to model the relationship between two or more variables when the data are normally distributed and the assumptions of the model are met.
        - **Pearson correlation coefficient:** Used to measure the strength and direction of the linear relationship between two continuous variables when the data are normally distributed.


    - **Non-parametric**: When your data violates any of these assumptions, non-parametric tests are more suitable. Non-parametric tests are called “distribution-free tests” because they don’t assume anything about the distribution of the population data.
        - Example: Wilcoxon signed-rank test, Mann-Whitney U test, Kruskal-Wallis test, Spearman correlation coefficient
        * **Wilcoxon signed-rank test:** Used to compare the medians of two related samples when the data are not normally distributed.
        * **Mann-Whitney U test:** Used to compare the medians of two independent groups when the data are not normally distributed.
        * **Kruskal-Wallis test:** Used to compare the medians of three or more groups when the data are not normally distributed.
        * **Spearman correlation coefficient:** Used to measure the strength and direction of the monotonic relationship between two continuous variables when the data are not normally distributed.

## Various kind of hypothesis testing
Statistical tests come in three forms: 
1. **comparison test:** Comparison tests assess whether there are differences in means, medians or rankings of scores of two or more groups. To decide which test suits your aim, consider whether your data meets the conditions necessary for parametric tests, the number of samples, and the levels of measurement of your variables.
    
| Comparison test	| Parametric?	| What’s being compared?	| Samples |
|-------------------|---------------|---------------------------|---------|
| t-test	| Yes	| Means	| 2 samples |
| ANOVA	| Yes	| Means	| 3+ samples |
| Mood’s median	| No	| Medians	| 2+ samples |
| Wilcoxon signed-rank	| No	| Distributions	| 2 samples |
| Wilcoxon rank-sum (Mann-Whitney U)	| No	| Sums of rankings	| 2 samples |
| Kruskal-Wallis H	| No	| Mean rankings	| 3+ samples |

2. **correlation test:** Correlation tests determine the extent to which two variables are associated. Although Pearson’s r is the most statistically powerful test, Spearman’s r is appropriate for interval and ratio variables when the data doesn’t follow a normal distribution. The chi square test of independence is the only test that can be used with nominal variables.

| Correlation test	| Parametric?	| Variables |
|-------------------|---------------|-----------|
| Pearson’s r	| Yes	| Interval/ratio variables |
| Spearman’s r	| No	| Ordinal/interval/ratio variables |
| Chi square test of independence	| No	| Nominal/ordinal variables |

3. **regression test:** Regression tests demonstrate whether changes in predictor variables cause changes in an outcome variable. You can decide which regression test to use based on the number and types of variables you have as predictors and outcomes. Most of the commonly used regression tests are parametric. If your data is not normally distributed, you can perform data transformations.Data transformations help you make your data normally distributed using mathematical operations, like taking the square root of each value.

| Regression test	| Predictor	| Outcome |
|-------------------|-----------|---------|
| Simple linear regression	| 1 interval/ratio variable	| 1 interval/ratio variable |
| Multiple linear regression	| 2+ interval/ratio variable(s)	| 1 interval/ratio variable |
| Logistic regression	| 1+ any variable(s)	| 1 binary variable |
| Nominal regression	| 1+ any variable(s)	| 1 nominal variable |
| Ordinal regression	| 1+ any variable(s)	| 1 ordinal variable |


### Step-by-Step Guide to Hypothesis Testing

> **note:** Please note that a detailed description on various kind of test statistics are given in chapter 8.

1. **Formulate Hypotheses**

   * **Null (H₀):** No effect or difference.
   * **Alternative (Hₐ):** There is an effect or difference.
     *Example:* H₀: Drug = Placebo, Hₐ: Drug ≠ Placebo.

    <a href="#null-and-alternative-hypothesis" style="display:inline-block;padding:5px 10px;background-color:#337ab7;color:#fff;text-decoration:none;border-radius:5px;font-size:14px;">Go to detailed section</a>

2. **Choose Significance Level (α)**

   * Commonly α = 0.05, the probability of rejecting H₀ when it’s true.

   <a href="#significance-level" style="display:inline-block;padding:5px 10px;background-color:#337ab7;color:#fff;text-decoration:none;border-radius:5px;font-size:14px;">Go to detailed section</a>

3. **Select a Statistical Test**

   * Depends on data type and research question.
   * Examples: t-test (2 groups), ANOVA (3+ groups), z-test (large sample or known σ).

    <a href="#selecting-a-appropriate-statistical-test" style="display:inline-block;padding:5px 10px;background-color:#337ab7;color:#fff;text-decoration:none;border-radius:5px;font-size:14px;">Go to detailed section</a>

4. **Calculate Test Statistic**

   * **t-test:** $t = \frac{\bar{x} - \mu}{s/\sqrt{n}}$
   * **z-test:** $z = \frac{\bar{x} - \mu}{\sigma/\sqrt{n}}$
   * Measures how far the sample is from H₀ in standard error units.

5. **Compute p-value**

   * Probability of observing data as extreme as the sample, assuming H₀ is true.
   * **p < α:** Reject H₀ (significant).
   * **p ≥ α:** Fail to reject H₀ (not significant).

6. **Interpret Results**

   * **Significant:** Evidence against H₀.
   * **Not significant:** Insufficient evidence to reject H₀.

---

#### Example
To illustrate this process, let's consider an example: 

Suppose we want to test whether there is a difference in the average height of men and women. We collect a sample of 100 men and 100 women, and measure their heights. We want to test the null hypothesis that there is no difference in height between men and women, against the alternative hypothesis that there is a difference.

- *Null hypothesis*: $H_0$: $\mu_1 = \mu_2$ (there is no difference in height between men and women). 

- *Alternative hypothesis:* $H_a$: $\mu_1 \neq \mu_2$ (there is a difference in height between men and women)

- *Significance level*: $\alpha = 0.05$

- *Statistical test*: We can use a two-sample t-test to compare the means of the two groups.

- *Test statistic*: The test statistic for a two-sample t-test is calculated as:

    t = (x̄1 - x̄2) / (s / sqrt(n1 + n2))

    where x̄1 and x̄2 are the sample means, s is the pooled standard deviation, and n1 and n2 are the sample sizes. In our example, let's assume that the sample mean height for men is 175 cm and the sample mean height for women is 162 cm. The pooled standard deviation (s) is calculated as:

    $s = \sqrt{\frac{(n1 - 1) * s1^2 + (n2 - 1) * s2^2}{(n1 + n2 - 2)}}$.

    where s1 and s2 are the sample standard deviations for the men and women, respectively. Let's assume that s1 = 6 cm and s2 = 5 cm. Then:

    s = 5.524 cm

    Plugging in the values, we get:

    $t = \frac{175 - 162}{{5.524 /\sqrt{100 + 100}}} = 12.215$

- *P-value*: The p-value is the probability of getting a t-statistic as extreme as 12.215, assuming that there is no difference in height between men and women. The p-value can be calculated using a t-distribution with 198 degrees of freedom (the sum of the sample sizes minus 2). Using a t-table or a statistical software, we find that the p-value is much less than 0.05 (in fact, it is practically 0), indicating strong evidence against the null hypothesis.

- *Interpretation*: Since the p-value is less than the significance level, we reject the null hypothesis and conclude that there is a statistically significant difference in height between men and women.

This example illustrates how hypothesis testing can be used to draw conclusions about differences between groups based on sample data. The choice of statistical test, calculation of the test statistic, and interpretation of the results can vary depending on the specific research question and data being analyzed.


---

## [Null and Alternative hypothesis](#null-and-alternative-hypothesis)

Formulating the null and alternative hypotheses is a **critical first step in hypothesis testing**.

## 1. Null Hypothesis (H₀)

* Statement that there is **no significant difference or relationship** between variables.
* Assumed true until evidence suggests otherwise.

## 2. Alternative Hypothesis (Hₐ or H₁)

* Statement that there **is a significant difference or relationship**.
* Represents the research hypothesis or what the researcher aims to prove.

## Key Points

* **Mutually Exclusive:** Only one can be true.
* **Collectively Exhaustive:** Together they cover all possibilities.
* Can be **one-tailed** (predicts direction) or **two-tailed** (no direction predicted).

## Examples

1. **Drug Effect on Blood Pressure**

   * H₀: The new drug has no effect on blood pressure.
   * Hₐ: The new drug has a significant effect on blood pressure.

2. **Job Satisfaction by Gender**

   * H₀: No difference in job satisfaction between men and women.
   * Hₐ: A significant difference exists in job satisfaction between men and women.

> ✅ Summary: Properly formulating H₀ and Hₐ defines the **research question** and the **direction of analysis**. It ensures clarity in statistical testing.

---

## [Significance level ($\alpha$)](#significance-level)

The **significance level**, denoted by **α**, represents the **probability of rejecting the null hypothesis (H₀) when it is actually true** — also known as the **risk of making a Type I error** (false positive).

---

## 🔹 What It Means

* **Type I Error:** Rejecting H₀ when it’s true.
* **α Value:** The threshold for deciding whether to reject H₀.
* **Common Choice:** α = 0.05 → 5% risk of Type I error.

---

## 🔹 Choosing α

The choice of α depends on:

1. **Consequences of Type I Error:**

   * If the cost of a false positive is high → use smaller α (e.g., 0.01).
2. **Strength of Evidence Needed:**

   * Stricter studies require smaller α to ensure stronger proof.
3. **Sample Size & Effect Size:**

   * Small samples or weak effects → lower α to reduce error risk.
   * Large samples or strong effects → slightly higher α acceptable.

---

## 🔹 Summary

* α controls how strict your test is.
* Smaller α → less chance of false positives but more chance of **Type II errors** (false negatives).
* Typically set at **0.05**, but may vary (e.g., 0.01 or 0.10) based on the context.

> ✅ **In short:**
> The significance level (α) defines how much risk you’re willing to accept when deciding to reject the null hypothesis.

---

## [Selecting a appropriate statistical test](#selecting-a-appropriate-statistical-test)

Choosing the **appropriate statistical test** is critical to ensure valid and reliable results. The test depends on your **data type**, **sample characteristics**, and **research question**.

---

## 🔹 Key Factors to Consider

1. **Type of Data**

   * **Continuous data:** Use tests like *t-test* or *ANOVA*.
   * **Categorical data:** Use *Chi-square* or *Fisher’s exact test*.
   * **Ordinal data:** Use nonparametric tests like *Mann–Whitney U* or *Kruskal–Wallis*.

2. **Sample Size**

   * **Small samples:** Prefer *nonparametric tests* (fewer assumptions).
   * **Large samples:** Use *parametric tests* (more powerful).

3. **Number of Groups**

   * **Two groups:** *t-test* (independent or paired).
   * **Three or more groups:** *ANOVA* or *Kruskal–Wallis*.

4. **Test Assumptions**

   * Normality → t-test, ANOVA.
   * Equal variances → ANOVA.
   * Violations → use nonparametric alternatives.

5. **Research Question Type**

   * **Comparing groups:** t-test, ANOVA.
   * **Relationships:** Correlation or regression.
   * **Associations (categorical):** Chi-square test.

---

## 🔹 Summary

Selecting the right test depends on:

> Data type ➜ Sample size ➜ Number of groups ➜ Assumptions ➜ Research question

Choosing appropriately ensures **valid conclusions** and **statistical accuracy**.

> ✅ **In short:** Pick the test that matches your data structure and research goal — the wrong test can invalidate your results.

---

## 🧠 Statistical Test Selection Guide

| **Objective**                       | **Data Type**                   | **Groups / Variables**          | **Common Test(s)**              | **Notes / Assumptions**                    |
| ----------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------------------ |
| **Compare means (parametric)**      | Continuous                      | 2 independent groups            | **Independent t-test**          | Data normal, equal variances               |
|                                     | Continuous                      | 2 related groups (before–after) | **Paired t-test**               | Normal difference scores                   |
|                                     | Continuous                      | 3+ groups                       | **ANOVA (One-way)**             | Normal, equal variances                    |
| **Compare medians (nonparametric)** | Ordinal / Non-normal continuous | 2 independent groups            | **Mann–Whitney U test**         | No normality assumption                    |
|                                     | Ordinal / Non-normal continuous | 3+ groups                       | **Kruskal–Wallis test**         | Nonparametric ANOVA alternative            |
| **Compare proportions**             | Categorical                     | 2+ categories                   | **Chi-square test**             | Expected freq ≥ 5                          |
|                                     | Categorical                     | Small sample                    | **Fisher’s Exact Test**         | For small expected counts                  |
| **Test relationships**              | Continuous                      | 2 variables                     | **Pearson correlation (r)**     | Linear, normal variables                   |
|                                     | Continuous / Ordinal            | 2 variables                     | **Spearman correlation (ρ)**    | Nonlinear or ranked data                   |
| **Predict a variable**              | Continuous (Y)                  | 1+ predictors                   | **Linear regression**           | Linearity, independence, homoscedasticity  |
|                                     | Categorical (Y)                 | 1+ predictors                   | **Logistic regression**         | Binary or multinomial outcome              |
| **Test goodness of fit**            | Categorical                     | 1 variable                      | **Chi-square goodness-of-fit**  | Compares observed vs. expected frequencies |
| **Check variance equality**         | Continuous                      | 2+ groups                       | **Levene’s or Bartlett’s test** | Tests homogeneity of variances             |

---

> ✅ **Quick Tip:**
>
> * Use **parametric tests** when data are normally distributed and assumptions are met.
> * Use **nonparametric tests** when data violate assumptions (skewed, ordinal, or small samples).
