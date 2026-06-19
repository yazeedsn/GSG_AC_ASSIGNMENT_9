import matplotlib.pyplot as plt
import os
import pandas as pd

def plot(series: pd.Series, save_path: str, figsize: tuple[int, int]=(8, 4)) -> None:
    """
    Plots the distribution of the data, highlighting the mean and the median of the series.

    Args:
        series (pd.Series): pandas series that contains the data to plot.
        save_path (str): the path to save the plot to (directories are created if not exist).
        figsize (tuple[int, int]): the plot figure size.
    
    Returns:
        None
    """
    dir = os.path.dirname(save_path)
    if dir:
        os.makedirs(dir, exist_ok=True)

    fig, ax = plt.subplots(figsize=figsize) 
    ax.hist(series, bins=50, color='#1B3A2D', edgecolor='white', linewidth=0.3) 
    ax.axvline(
        series.mean(), 
        color='#C9A84C', 
        lw=2, 
        label=f"Mean: {series.mean():.0f}"
    ) 
    ax.axvline(
        series.median(), 
        color='#E8C96A', 
        lw=2, 
        ls='--', 
        label=f"Median: {series.median():.0f}"
    ) 
    ax.set_title(str.title(series.name))
    ax.legend()
    fig.tight_layout()
    plt.savefig(save_path, dpi=150)
