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

## 1. t-test

The t-test is a statistical test used to determine if there is a significant difference between the means of two groups. There are two main types of t-tests: 
1. the independent samples t-test and 
2. the paired samples t-test.

Independent Samples t-Test:
The independent samples t-test is used to compare the means of two independent groups. The null hypothesis is that the two groups have equal means, while the alternative hypothesis is that they have different means.

The formula for the independent samples t-test is:

t = (x̄1 - x̄2) / (s√(1/n1 + 1/n2))

Where:
x̄1 and x̄2 are the means of the two groups
s is the pooled standard deviation
n1 and n2 are the sample sizes of the two groups

The independent samples t-test assumes that the variances of the two groups are equal. If they are not, a modified version of the t-test called Welch's t-test can be used.

Paired Samples t-Test:
The paired samples t-test is used to compare the means of two related groups, such as before and after measurements of the same group. The null hypothesis is that the mean difference between the two groups is zero, while the alternative hypothesis is that the mean difference is different from zero.

The formula for the paired samples t-test is:

t = d̄ / (s/√n)

Where:
d̄ is the mean difference between the two groups
s is the standard deviation of the differences
n is the sample size

The paired samples t-test assumes that the differences between the two groups are normally distributed.

Interpretation:
After calculating the t-value and degrees of freedom, the p-value can be obtained from the t-distribution table. If the p-value is less than the significance level, then the null hypothesis is rejected, indicating that there is a significant difference between the means of the two groups. If the p-value is greater than the significance level, then the null hypothesis cannot be rejected, indicating that there is not a significant difference between the means of the two groups.


---


## 2. ANOVA (Analysis of Variance) test

ANOVA (Analysis of Variance) is a statistical test used to determine whether there are significant differences between the means of three or more groups. It tests the null hypothesis that all group means are equal, against the alternative hypothesis that at least one group mean is different from the others.

The ANOVA test is based on the F-statistic, which is calculated by dividing the variance between the groups by the variance within the groups. The F-statistic follows an F-distribution with degrees of freedom based on the number of groups and the number of observations.

Here are the steps to perform an ANOVA test:

1. Formulate the null and alternative hypotheses:
    - H0: μ1 = μ2 = μ3 = ... = μk (all group means are equal)
    - Ha: at least one group mean is different from the others

2. Choose a significance level (α) and determine the degrees of freedom for the F-distribution:
    - Degrees of freedom between groups: k - 1
    - Degrees of freedom within groups: N - k, where N is the total number of observations

3. Collect and organize the data into groups.

4. Calculate the sum of squares between groups (SSbetween):
    - SSbetween = ∑ni(x̄i - x̄)^2, 
    
    where ni is the number of observations in group i, x̄i is the mean of group i, and x̄ is the overall mean

5. Calculate the sum of squares within groups (SSwithin):
    - SSwithin = ∑(xi - x̄i)^2, 
    
    where xi is the ith observation in group i

6. Calculate the mean square between groups (MSbetween):
    - MSbetween = SSbetween / (k - 1)

7. Calculate the mean square within groups (MSwithin):
    - MSwithin = SSwithin / (N - k)

8. Calculate the F-statistic:
    - F = MSbetween / MSwithin

9. Calculate the p-value associated with the F-statistic using a table of F-distributions or a statistical software package.

10. Compare the p-value to the significance level. If the p-value is less than the significance level, reject the null hypothesis and conclude that there is a significant difference between the means of at least two groups. If the p-value is greater than the significance level, fail to reject the null hypothesis and conclude that there is not enough evidence to suggest a significant difference between the means of any of the groups.

**Example:** Here's an example of an ANOVA test:

Suppose we want to compare the average test scores of students in three different schools (A, B, and C). We randomly sample 10 students from each school and obtain the following data:

- **School A:** 75, 80, 82, 85, 88, 90, 92, 94, 95, 98
- **School B:** 70, 75, 77, 80, 83, 85, 87, 88, 90, 92
- **School C:** 65, 70, 72, 75, 78, 80, 82, 84, 85, 88

1. Formulate the null and alternative hypotheses:
    - H0: μA = μB = μC
    - Ha: at least one group mean is different from the others

2. Choose a significance level (α) and determine the degrees of freedom for the F-distribution:
    - α = 0.05
    - Degrees of freedom between groups: 3 - 1 = 2
    - Degrees of freedom within groups: 30 - 3 = 27

3. Collect and organize the data into groups.

4. Calculate the sum of squares between groups (SSbetween):
    - SSbetween