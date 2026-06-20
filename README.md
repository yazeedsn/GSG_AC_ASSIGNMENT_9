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

### Q4
Using the chi-square test to check independance between the winner and whether the games is rate or not. In the chess data we have the following distribution for winner over rated.

| Rated | Black | Draw | White |
|-------|------:|-----:|------:|
| False | 1723  | 231  | 1949  |
| True  | 7384  | 719  | 8052  |

Using the chi-square test over the previous results, we obtain a **p value of 0.00034** which means the hypthosis that the winner is indepndent from whether the game is rate or not is rejected. 
chi-square test yields the following expected values.

| Rated | Black     | Draw     | White     |
|-------|----------:|---------:|----------:|
| False | 1772.09   | 184.86   | 1946.05   |
| True  | 7334.91   | 765.14   | 8054.95   |

In the actual data, draw tend to occure more than expected in rated games. Thus, draw probability is dependant on a game being rated or not.

**Effect size (Cramers_v) = 0.028239**. This means that the reported results has little practical significane.