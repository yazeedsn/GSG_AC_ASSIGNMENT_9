import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def matrix(
        df: pd.DataFrame,
        drop_columns: list[str]=None,
        method: str='pearson', 
        round:int=3
    ) -> pd.DataFrame:
    """
    Calculates the correlation between the numerical types in the dataframe.

    Args:
        df (pd.DataFrame): the dataframe to get the correlation matrix of.
        drop_columns (list[str]): any columns to ignore from the matrix.
        method (str): correlation method, see pd.corr documentation for more.
        round (int): the number of decimal digits to round to.

    Return:
        pd.DataFrame: the result correlation matrix.
    """
    df = df.copy().select_dtypes('number')
    if drop_columns != None:
        df = df.drop(columns=drop_columns)
    return df.corr(method=method).round(round) 
    

def heatmap(
        matrix: pd.DataFrame, 
        save_path: str, 
        title: str='',
        figsize=(6, 6)
    ) -> None:
    """
    Draws a heatmap for the provided correlation matrix.

    Args:
        matrix (pd.DataFrame): the correlation matrix to use for the heatmap.
        save_path (str): the path to save the resulted figure in.
        title (str): the title of the figure.
    
    Returns:
        None
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(matrix, cmap='Blues', vmin=0, vmax=1.0)
    ax.set_title(title)
    fig.tight_layout()
    plt.savefig(save_path, dpi=150)


def strongest(matrix: pd.DataFrame, column: str, n: int=1) -> pd.DataFrame:
    """
    Gets n highest correlated columns with the given column.
    Considers both negative and positive correlations.

    Args:
        matrix (pd.DataFrame): the correlation matrix to use.
        column (str): the reference column to get the correlation for.
        n (int): the number of correlations to return.
    
    Returns:
        pd.DataFrame: a dataframe of n highest correlated columns with column 
            and their correlation values
    """
    matrix = matrix.copy()
    corr = matrix[column].drop(column)
    top_pos = corr.nlargest(n)
    top_neg = corr.nsmallest(n)
    stack = pd.concat([top_pos, top_neg])
    stack = stack.sort_values(key=lambda col: col.abs(), ascending=False)
    return stack.head(n)