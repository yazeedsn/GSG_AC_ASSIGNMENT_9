> **Entry point:** `src/main.py`
# Assignment 9: Statistical Analysis
## Descriptive Statistics
| Metric       | mean     | std        | median | skew     | q1     | q2   | q3    |
|--------------|----------|------------|--------|----------|--------|------|-------|
| turns        | 60.465999| 33.570585  | 55.0   | 0.897284 | 37.0   | 55.0 | 79.0  |
| rating_diff  | 7.799880 | 249.036667 | 3.0    | 0.082723 | -108.0 | 3.0  | 122.0 |

### Q1
Both metrics are skewed to the right with varying severity: **turns** number has **large skewness**  (mean > median and large values relative to standard deviation), while **rating difference** skewness is very **slight** (mean > median but small difference compared to the standard deviation).**


![turns distribution](output\turns_distribution.png)
![rating difference distribution](output\rating_difference.png)

### Q2

Since rating_diff has slight skewness, we will only do normality tests and normalization for turns to fix its skewness.

**Turns** get a value of **p=0.0 in normality tests**. Thus, we will normalize it with either log or sqrt.

Turns skewness after **log transform** is **-1.611528418915271**.

In this case, log transform is aggressive, so we will use **sqrt transform** instead to reduce turns skewness to **-0.061886630234739656**.
### Q3
![WHO correlation matrix](output\corr_matirx.png)

**Alcohol** and **Income composition of reasources** are **strongly correlated (0.45)**, but its unlikely that there is a causation between the two variable. The correlation is probably the result of a cofounder between both variables. One suspicion is that **cofounder** is the **GDP**. To test this hypothesis, we will **confine the GDP to a limited range and see whether the correlation persists.**

![GPD](output\gdp_distribution.png)
Taking entries with a GDP under 500 will give a **sample of size 666** which is acceptable compared to the **original population size of 2938**.

Within our sample, the **correlation** between Alcohol consumption and income composition of reasoruces **drops to 0.268**, which confirms our assumption that the **GDP is a cofounder** between alcohol and income composition of reasources.