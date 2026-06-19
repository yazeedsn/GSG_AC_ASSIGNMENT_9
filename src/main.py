import pandas as pd
from clean import clean_chess
from fast_stats.descriptive import get_basic_stats
from pathlib import Path

# Global Paths
RAW_DATA_DIR = Path('data/raw')


if __name__ == '__main__':
    df = clean_chess(pd.read_csv(RAW_DATA_DIR/'chess_games.csv'))
