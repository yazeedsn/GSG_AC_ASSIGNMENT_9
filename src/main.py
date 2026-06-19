import pandas as pd
from clean import clean_chess
from fast_stats import distribution
from fast_stats.descriptive import basic_stats
from scipy import stats
from pathlib import Path
from fetch import load_data
import numpy as np 

# Global Paths and urls
RAW_DATA_DIR = Path('data/raw')



if __name__ == '__main__':
    df = clean_chess(pd.read_csv(RAW_DATA_DIR/'chess_games.csv'))

    turns = df['turns']
    rating_diff = df['rating_diff']

    # Descriptive Statistics
    turns_stats = basic_stats(turns)
    rating_diff_stats = basic_stats(rating_diff)
    stat_table = pd.concat(
        [
            pd.DataFrame(turns_stats.values(), index=turns_stats.keys()).T,
            pd.DataFrame(rating_diff_stats.values(), index=rating_diff_stats.keys()).T
        ]
    )
    stat_table.index = ['turns', 'rating_diff']
    print(stat_table)

    # Plot distributions
    distribution.plot(turns, 'output/turns_distribution.png')
    distribution.plot(rating_diff, 'output/rating_difference.png')

    # Test normality     
    print('Turns Normality Tests')
    stat, p = stats.shapiro(turns.sample(1000, random_state=42)) 
    print(f"Shapiro-Wilk  p = {p:.6f}")  
    
    # normalization
    df['turns_log'] = np.log(turns)
    print('turns skewness after log transform', df['turns_log'].skew())
    df['turns_sqrt'] = np.sqrt(rating_diff - rating_diff.min())
    print('turns skewness after sqrt transform', df['turns_sqrt'].skew())

