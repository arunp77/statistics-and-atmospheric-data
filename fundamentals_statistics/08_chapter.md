# 🧠 ANOVA (Analysis of Variance)

## 🔹 Overview

**Analysis of Variance (ANOVA)** is a statistical method used to **compare the means of three or more groups** to determine if at least one group mean differs significantly from the others.

It extends the **t-test** (which compares two means) to **multiple groups** while controlling the **Type I error rate**.

---

## 🔹 Intuitive Idea

Instead of comparing means pairwise (like multiple t-tests), ANOVA compares **variability between groups** to **variability within groups**.

* If the **between-group variability** is **much larger** than the **within-group variability**, it suggests that the group means are **not all equal**.

---

## 🔹 Hypotheses

$$
H_0: \mu_1 = \mu_2 = \mu_3 = \dots = \mu_k \quad \text{(all group means are equal)}
$$

$$
H_a: \text{At least one group mean is different}
$$

---

## 🔹 The ANOVA Concept

ANOVA divides the **total variation** in the data into two components:

| Source of Variation       | Description                          | Measured by    |
| ------------------------- | ------------------------------------ | -------------- |
| **Between Groups**        | Differences due to group means       | $SS_{between}$ |
| **Within Groups (Error)** | Random differences within each group | $SS_{within}$  |

---

## 🔹 The F-statistic

The **F-statistic** measures the ratio of between-group variance to within-group variance:

$$
F = \frac{MS_{between}}{MS_{within}}
$$

where:

$$
MS_{between} = \frac{SS_{between}}{df_{between}} \quad \text{and} \quad MS_{within} = \frac{SS_{within}}{df_{within}}
$$

* $SS$: Sum of squares
* $df$: Degrees of freedom
* $MS$: Mean square (average sum of squares)

If $F$ is large, it indicates that group means differ more than expected by random chance.

---

## 🔹 One-Way ANOVA

### **Purpose:**

Compare the means of **three or more groups** based on **one independent variable** (factor).

### **Example:**

You test whether **three fertilizers** produce different average plant growth.

| Group        | Mean Growth (cm) |
| ------------ | ---------------- |
| Fertilizer A | 12               |
| Fertilizer B | 15               |
| Fertilizer C | 18               |

### **Model:**

$$
Y_{ij} = \mu + \tau_i + \varepsilon_{ij}
$$

where:

* $Y_{ij}$: observation $j$ in group $i$
* $\mu$: overall mean
* $\tau_i$: effect of group $i$
* $\varepsilon_{ij}$: random error term (assumed normally distributed)

### **Assumptions:**

1. Independence of observations
2. Normal distribution within each group
3. Homogeneity of variances (equal variances across groups)

---

### **Decision Rule:**

* Compute F-statistic
* Compare with critical F-value from F-distribution at significance level (e.g., α = 0.05)
* If $F > F_{critical}$, reject $H_0$

### **Post-hoc Tests (if H₀ is rejected):**

If you find a significant difference, use post-hoc tests (e.g., **Tukey’s HSD**, **Bonferroni**) to identify **which groups differ**.

---

## 🔹 Two-Way ANOVA

### **Purpose:**

Compare means across groups when you have **two independent variables (factors)**.
It also allows testing for **interaction effects** between factors.

### **Example:**

You test how **fertilizer type (A, B, C)** and **sunlight exposure (Low, High)** affect plant growth.

### **Model:**

$$
Y_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \varepsilon_{ijk}
$$

where:

* $\mu$: overall mean
* $\alpha_i$: effect of Factor A (e.g., fertilizer)
* $\beta_j$: effect of Factor B (e.g., sunlight)
* $(\alpha\beta)_{ij}$: interaction effect between A and B
* $\varepsilon_{ijk}$: random error term

---

### **Hypotheses:**

1. For **Factor A**:
   $H_0: \alpha_1 = \alpha_2 = ... = 0$
2. For **Factor B**:
   $H_0: \beta_1 = \beta_2 = ... = 0$
3. For **Interaction (A×B)**:
   $H_0: (\alpha\beta)_{ij} = 0$

If interaction is significant, interpret it before looking at main effects.

---

### **Outputs:**

Two-way ANOVA produces **three F-statistics:**

1. For Factor A
2. For Factor B
3. For the Interaction term (A×B)

---

## 🔹 Interpreting Results

| Term                    | Interpretation                                           |
| ----------------------- | -------------------------------------------------------- |
| **F-statistic**         | Ratio of between-group variance to within-group variance |
| **p-value**             | Probability of observing F by chance under H₀            |
| **Significant p (< α)** | Reject H₀ — at least one group differs                   |
| **Post-hoc tests**      | Identify which specific groups differ                    |

---

## 🔹 Summary

| Type              | Factors | Example                                           | Main Goal                                                |
| ----------------- | ------- | ------------------------------------------------- | -------------------------------------------------------- |
| **One-Way ANOVA** | 1       | Compare test scores across 3 teaching methods     | Does the method affect performance?                      |
| **Two-Way ANOVA** | 2       | Compare scores across teaching methods and gender | Does method, gender, or their interaction affect scores? |

---

## ✅ In Short

* ANOVA tests whether **group means differ** significantly.
* The **F-ratio** compares between- vs. within-group variation.
* **One-way ANOVA** → 1 factor; **Two-way ANOVA** → 2 factors (can include interaction).
* **Post-hoc tests** help pinpoint which groups differ.

