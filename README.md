> **Entry point:** `src/main.py`
# Assignment 9: Statistical Analysis
## Descriptive Statistics
| Metric       | mean     | std        | median | skew     | q1     | q2   | q3    |
|--------------|----------|------------|--------|----------|--------|------|-------|
| turns        | 60.465999| 33.570585  | 55.0   | 0.897284 | 37.0   | 55.0 | 79.0  |
| rating_diff  | 7.799880 | 249.036667 | 3.0    | 0.082723 | -108.0 | 3.0  | 122.0 |

Both metrics are skewed to the right with varying severity: **turns** number has **large skewness**  (mean > median and large values relative to standard deviation), while **rating difference** skewness is very **slight** (mean > median but small difference compared to the standard deviation).**


![turns distribution](output\turns_distribution.png)
![rating difference distribution](output\rating_difference.png)

Since rating_diff has slight skewness, we will only do normality tests and normalization for turns to fix its skewness.
Turns get a value of p=0.0 in normality tests.

Turns skewness after log transform is -1.611528418915271.

In this case, log transform is aggressive, so we will use sqrt transform instead to reduce turns skewness to -0.061886630234739656.