import pandas as pd 

def clean_chess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans chess dataframe and add a rating_diff column

    Args: 
        df (pd.DataFrame): original chess dataframe to clean.
    
    Returns:
        pd.DataFrame: New chess dataframe with unnamed and opeining_response droped,
            and rating_diff column added.
    """
    df = df.copy()
    df = df.drop(columns=['Unnamed: 0'])
    df['rating_diff'] = (df['white_rating'] - df['black_rating'])
    df = df.drop(columns=['opening_response'])
    assert df['rating_diff'].notna().all()
    assert df.duplicated().sum() == 0
    return df

def clean_who(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans WHO dataframe.

    Args: 
        df (pd.DataFrame): original WHO dataframe to clean.
    
    Returns:
        pd.DataFrame: New WHO dataframe with unnamed droped,
    """
    df = df.copy()
    df = df.drop(columns=['Unnamed: 0'])
    df.columns = df.columns.str.strip().str.upper().str.replace(' ', '_')
    return df