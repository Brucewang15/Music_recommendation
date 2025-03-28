import pandas as pd
from sklearn.preprocessing import StandardScaler
import logging


class DataProcessing:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.audio_features = [
            'danceability',
            'energy', 
            'tempo', 
            'loudness', 
            'valence',
            'liveness', 
            'speechiness', 
            'acousticness', 
            'instrumentalness',
            'duration_ms'
        ]
        self.metadata = [
            'track_id',
            'track_name',
            'track_artist',
            'track_album_release_date'
        ]
        self.scaler = StandardScaler()

    def preprocess_data(self, df):
        initial_count = len(df)
        df = df.drop_duplicates(subset=['track_id'])
        self.logger.info(f"Removed {initial_count - len(df)} duplicate tracks")

        initial_count = len(df)
        df = df.dropna(subset=['tempo', 'danceability', 'energy', 'loudness', 'valence'])
        self.logger.info(f"Removed {initial_count - len(df)} tracks with missing features")

        df = df[self.audio_features + self.metadata]
        self.logger.info(f"Dataframe shape after filtering: {df.shape}")

        df[self.audio_features] = self.scaler.fit_transform(df[self.audio_features])

        return df