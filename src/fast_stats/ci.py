from scipy import stats
from scipy.stats import t as t_dist 

import pandas as pd 
import numpy as np

def confidence_interval(series: pd.Series, confidence: float=0.95) -> tuple[float, float]:
    """
    Gives the confidence interval for the given series.

    Args:
        series (pd.Series): the series to measure the confidence interval for.
        confidence (float): confidence degree to find the interval for.

    Returns:
        
    """
    n = len(series)
    mean = series.mean()
    se = stats.sem(series)    
    h = se * t_dist.ppf((1 + confidence) / 2., n - 1)    
    return mean - h, mean + h 




def bootstrap_ci(series: pd.Series, n_boot: int=1000, confidence: float=0.95):    
    rng = np.random.default_rng(42)    
    means = [rng.choice(series, len(series), replace=True).mean() for _ in range(n_boot)]    
    a = (1 - confidence) / 2    
    return np.percentile(means, [a*100, (1-a)*100]) 
