import pandas as pd
import numpy as np
from sqlalchemy.exc import SQLAlchemyError
from db.database import SessionLocal, Base, engine
from db.models import Track
import faiss
from pathlib import Path

def normalize_vector(vector):   
    vector = np.asarray(vector, dtype='float32').reshape(1, -1)
    faiss.normalize_L2(vector)
    return vector[0]

def insert_data_to_csv(csv_path):
    df = pd.read_csv(csv_path)

    Base.metadata.create_all(bind=engine)
    data_columns = [
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

    session = SessionLocal()

    tracks = []

    for _, row in df.iterrows():
        vector = normalize_vector(row[data_columns].values)
        track = Track(
            track_id=row['track_id'],
            track_name=row['track_name'],
            track_artist=row['track_artist'],
            track_album_release_date=row['track_album_release_date'],
            vector=vector
        )
        tracks.append(track)
    session.bulk_save_objects(tracks)
    session.commit()
    print("Data inserted successfully")
    session.close()
if __name__ == "__main__":
    csv_path = Path(__file__).parent.parent / 'data' / 'processed_data.csv'
    insert_data_to_csv(csv_path)
