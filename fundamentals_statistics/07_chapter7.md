# Experimental design and Various kinds of tests

Comparison test
1. t-test	
2. ANOVA	
3. Mood’s median	
4. Wilcoxon signed-rank
5. Wilcoxon rank-sum (Mann-Whitney U)	
6. Kruskal-Wallis H	

Correlation test
1. Pearson’s r	
2. Spearman’s r	
3. Chi square test of independence

Regression test
1. Simple linear regression	
2. Multiple linear regression	
3. Logistic regression	
4. Nominal regression	
5. Ordinal regression


---

## 1. Independent t-test

The t-test is a statistical test used to determine if there is a significant difference between the means of two groups. There are two main types of t-tests: 
1. the independent samples t-test and 
2. the paired samples t-test.

Independent Samples t-Test:
The independent samples t-test is used to compare the means of two independent groups. The null hypothesis is that the two groups have equal means, while the alternative hypothesis is that they have different means.

The formula for the independent samples t-test is:

$$
t = \frac{\bar{X}_1 - \bar{X}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
$$

Where:
- $\bar{x}_1$ and $\bar{x}_2$ are the means of the two groups
- $s_p$ is the pooled standard deviation
- $n_1$ and $n_2$ are the sample sizes of the two groups

Here pooled standard deviation is defined as:

$$
s_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}
$$

The independent samples t-test assumes that the variances of the two groups are equal. If they are not, a modified version of the t-test called Welch's t-test can be used.

### Paired Samples t-Test:
The paired samples t-test is used to compare the means of two related groups, such as before and after measurements of the same group. The null hypothesis is that the mean difference between the two groups is zero, while the alternative hypothesis is that the mean difference is different from zero.

The formula for the paired samples t-test is:

$$
t = \frac{\bar{d}}{s_d / \sqrt{n}}
$$

where
- $\bar{d}$ = mean of differences, 
- $s_d$ = standard deviation of differences, 
- $n$ = sample size.

The paired samples t-test assumes that the differences between the two groups are normally distributed.

#### Interpretation:
After calculating the t-value and degrees of freedom, the p-value can be obtained from the t-distribution table. If the p-value is less than the significance level, then the null hypothesis is rejected, indicating that there is a significant difference between the means of the two groups. If the p-value is greater than the significance level, then the null hypothesis cannot be rejected, indicating that there is not a significant difference between the means of the two groups.


---

## 2. ANOVA (Analysis of Variance) test

ANOVA (Analysis of Variance) is a statistical test used to determine whether there are significant differences between the means of three or more groups. It tests the null hypothesis that all group means are equal, against the alternative hypothesis that at least one group mean is different from the others.

The ANOVA test is based on the F-statistic, which is calculated by dividing the variance between the groups by the variance within the groups. The F-statistic follows an F-distribution with degrees of freedom based on the number of groups and the number of observations.

More details on ANOVA is in chapter 8.



## 4. Mann–Whitney U test

**Purpose:** Compare **medians** of two independent groups (nonparametric).
**Formula:**

$$
U = n_1 n_2 + \frac{n_1 (n_1 + 1)}{2} - R_1
$$

where $R_1$ is the sum of ranks for group 1.
Used when data are **ordinal or non-normal**.

---

## 5. Kruskal–Wallis test

**Purpose:** Compare **three or more independent groups** (nonparametric ANOVA).
**Formula:**

$$
H = \frac{12}{N(N+1)} \sum \frac{R_i^2}{n_i} - 3(N+1)
$$

where $R_i$ = rank sum of group $i$, $n_i$ = sample size, $N$ = total sample size.
Follows chi-square distribution with $k-1$ degrees of freedom.

---

## 6. Chi-square test of independence

**Purpose:** Test **association between two categorical variables**.
**Formula:**

$$
\chi^2 = \sum \frac{(O - E)^2}{E}
$$

where $O$ = observed frequency, $E$ = expected frequency.
Larger χ² → stronger evidence against independence.

---

## 7. Fisher’s Exact Test

**Purpose:** Exact test for association between **two categorical variables** when sample sizes are small.
**No formula approximation:** Uses combinatorial probability to compute the exact p-value from contingency tables.

---

## 8. Pearson Correlation (r)

**Purpose:** Measure **linear relationship** between two continuous variables.
**Formula:**

$$
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
$$

Range: -1 (perfect negative) → +1 (perfect positive).

---

## 9. Spearman Rank Correlation (ρ)

**Purpose:** Measure **monotonic relationship** using **ranks**.
**Formula:**

$$
\rho = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}
$$

where $d_i$ = rank differences.

---

## 10. Linear Regression

**Purpose:** Model relationship between **dependent variable (Y)** and **independent variable(s) (X)**.
**Model:**

$$
Y = \beta_0 + \beta_1 X + \varepsilon
$$

where β₀ = intercept, β₁ = slope, and ε = random error.
Objective: Minimize

$$
\sum (Y_i - \hat{Y_i})^2
$$

(least squares).

---

## 11. Logistic Regression

**Purpose:** Model probability of a **binary outcome**.
**Model:**

$$
\ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 X
$$

where $p$ = probability of success (Y=1).
Uses **maximum likelihood estimation**.

---

## 12. Chi-square Goodness-of-Fit Test

**Purpose:** Test if observed frequencies match expected theoretical distribution.
**Formula:**

$$
\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
$$

where $E_i$ are expected counts based on hypothesis.

---

## 13. Levene’s Test / Bartlett’s Test

**Purpose:** Test **equality of variances** across groups.

* **Levene’s:** Robust to non-normal data.
* **Bartlett’s:** More sensitive, assumes normality.

**Levene’s Formula (simplified):**

$$
W = \frac{(N - k)}{(k - 1)} \frac{\sum n_i (Z_{i\cdot} - Z_{\cdot\cdot})^2}{\sum \sum (Z_{ij} - Z_{i\cdot})^2}
$$

where $Z_{ij} = |Y_{ij} - \text{median}(Y_i)|$.

---

> ✅ **In short:** Each test answers a specific question —
> “Are groups different?”, “Are variables related?”, or “Can one predict another?”
> Always match your **data type**, **distribution**, and **research question** to the correct test.

