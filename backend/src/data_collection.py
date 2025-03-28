from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from pathlib import Path
import logging

class DataCollection:
    def __init__(self, file_name):
        self.logger = logging.getLogger(__name__)

        self.data_dir = Path(__file__).parent.parent / 'data'
        self.file_path = self.data_dir / file_name
    def load_data(self):
        self.logger.info(f'Loading data from {self.file_path}')
        df = pd.read_csv(self.file_path)
        self.logger.info(f'Data shape: {df.shape}')
        print(df.columns.tolist(), 'list of columns')
        print(df.isnull().sum(), 'null values')
        print(df.head())

        return df

# data_dir = Path(__file__).parent.parent / 'data'

# df = pd.read_csv(data_dir / 'combined_spotify_data.csv')
# print(df.shape)
# print(df.columns.tolist(), 'list of columns')
# print(df.isnull().sum(), 'null values')
# print(df.head())

# initial_count = len(df)
# df = df.drop_duplicates(subset=['track_id'])
# print(f"\nRemoved {initial_count - len(df)} duplicate tracks")

# initial_count = len(df)
# df = df.dropna(subset=['tempo', 'danceability', 'energy', 'loudness', 'valence'])
# print(f"\nRemoved {initial_count - len(df)} tracks with missing features")

# audio_features = [
#     'danceability',
#     'energy', 
#     'tempo', 
#     'loudness', 
#     'valence',
#     'liveness', 
#     'speechiness', 
#     'acousticness', 
#     'instrumentalness',
#     'duration_ms'
# ]
# metadata = [
#     'track_id',
#     'track_name',
#     'track_artist',
#     'track_album_release_date',
# ]

# df = df[audio_features + metadata]
# print(f"\nDataframe shape after filtering: {df.shape}")

# scaler = StandardScaler()
# df[audio_features] = scaler.fit_transform(df[audio_features])

