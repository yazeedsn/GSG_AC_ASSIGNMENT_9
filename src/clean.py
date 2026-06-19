import pandas as pd 

def clean_chess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean chess dataframe and add a rating_diff column

    Args: 
        df (pd.DataFrame): original chess dataframe to clean.
    
    Returns:
        pd.DataFrame: New chess dataframe with unamed and opeining_response droped,
            and rating_diff column added.
    """
    df = df.copy()
    df = df.drop(columns=['Unnamed: 0'])
    df['rating_diff'] = df['white_rating'] - df['black_rating']
    df = df.drop(columns=['opening_response'])
    assert df['rating_diff'].notna().all()
    assert df.duplicated().sum() == 0
    return df