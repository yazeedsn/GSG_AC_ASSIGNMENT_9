import pandas as pd
from pandas.api.types import is_numeric_dtype


def basic_stats(series: pd.Series) -> dict[str, float]:
    """
    Takes a numeric pandas series and returns its basic statistics in dictonary.
    measures mean, std, median, skew, q1, q2, and q3.

    Args:
        series (pd.Series): Numerical series to get its statistics.
    Returns:
        dict[str: float]: a dictonary of the mapping statistic_name -> statistic_value.
    """
    assert is_numeric_dtype(series), 'series is non-numeric type!'

    return {
        'mean': series.mean(),
        'std' : series.std(),
        'median' : series.median(),
        'skew' : series.skew(),
        'q1' : series.quantile(0.25),
        'q2' : series.quantile(0.50),
        'q3' : series.quantile(0.75),
    }
