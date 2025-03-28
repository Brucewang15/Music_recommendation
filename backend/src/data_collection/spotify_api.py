
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from pathlib import Path


data_dir = Path(__file__).parent.parent.parent / 'data'

df = pd.read_csv(data_dir / 'combined_spotify_data.csv')
print(df.shape)
print(df.columns.tolist(), 'list of columns')
print(df.isnull().sum(), 'null values')