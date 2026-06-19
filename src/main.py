import pandas as pd
from clean import clean_chess
from fast_stats.descriptive import basic_stats
from pathlib import Path

# Global Paths
RAW_DATA_DIR = Path('data/raw')


if __name__ == '__main__':
    df = clean_chess(pd.read_csv(RAW_DATA_DIR/'chess_games.csv'))

    # Descriptive Statistics
    turns_stats = basic_stats(df['turns'])
    rating_diff_stats = basic_stats(df['rating_diff'])
    stat_table = pd.concat(
        [
            pd.DataFrame(turns_stats.values(), index=turns_stats.keys()).T,
            pd.DataFrame(rating_diff_stats.values(), index=rating_diff_stats.keys()).T
        ]
    )
    stat_table.index = ['turns', 'rating_diff']
    print(stat_table)
