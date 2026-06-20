import os 
import pandas as pd 
import logging

logger = logging.getLogger(__name__)

def load_data(url: str, local_path: str) -> pd.DataFrame :
    if os.path.exists(local_path):
        logger.info(f'Loading from cache: {local_path}')
        return pd.read_csv(local_path)
    logger.info('Downloading from {url}...')
    df = pd.read_csv(url)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    df.to_csv(local_path)
    logger.info(f'Save to {local_path}')
    return df