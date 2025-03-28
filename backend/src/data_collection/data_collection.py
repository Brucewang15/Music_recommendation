
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from pathlib import Path


data_dir = Path(__file__).parent.parent.parent / 'data'

df = pd.read_csv(data_dir / 'combined_spotify_data.csv')
print(df.shape)
print(df.columns.tolist(), 'list of columns')
print(df.isnull().sum(), 'null values')
print(df.head())

initial_count = len(df)
df = df.drop_duplicates(subset=['track_id'])
print(f"\nRemoved {initial_count - len(df)} duplicate tracks")

initial_count = len(df)
df = df.dropna(subset=['tempo', 'danceability', 'energy', 'loudness', 'valence'])
print(f"\nRemoved {initial_count - len(df)} tracks with missing features")

audio_features = [
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
metadata = [
    'track_id',
    'track_name',
    'track_artist',
    'track_album_release_date',
]

df = df[audio_features + metadata]
print(f"\nDataframe shape after filtering: {df.shape}")

