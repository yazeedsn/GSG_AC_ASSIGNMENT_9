import pandas as pd
import numpy as np 
from scipy import stats
from pathlib import Path

from fetch import load_data
from clean import clean_chess, clean_who
from fast_stats import distribution, correlation
from fast_stats.descriptive import basic_stats

# Global Paths and urls
RAW_DATA_DIR = Path('data/raw')
WHO_URL = 'https://github.com/Priyankkoul/Life-Expectancy-WHO---Data-Analytics/blob/master/DATASET.csv?raw=true'



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

    WHO_df = load_data(WHO_URL, RAW_DATA_DIR/'who.csv')
    WHO_df = clean_who(WHO_df)
    
    corr_matrix = correlation.matrix(WHO_df, drop_columns=['YEAR'], method='pearson')
    correlation.heatmap(
        corr_matrix, 
        'output/corr_matirx.png', 
        title='WHO Correlation Matrix',
        figsize=(8,8)
    )

    highest = correlation.strongest(corr_matrix, 'ALCOHOL', 3)
    print('ALCOHOL has the highest correlations with: ')
    print(highest)

    distribution.plot(WHO_df['GDP'], 'output/gdp_distribution.png')
    sample_df = WHO_df[(WHO_df['GDP'] < 500)]
    print(f"Population Size: {len(WHO_df)}")
    print(f"Sample Size: {len(sample_df)}")

    corr_matrix = correlation.matrix(
        sample_df[['ALCOHOL','INCOME_COMPOSITION_OF_RESOURCES']],
        method='pearson'
    )
    print('ALCOHOL and INCOME_COMPOSITION_OF_RESOURCES under controlled GDP')
    print(corr_matrix)