from sqlalchemy import Column, Integer, String
from database import Base
from pgvector.sqlalchemy import Vector

class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    track_id = Column(String, unique=True, index=True)
    track_name = Column(String)
    track_artist = Column(String)
    track_album_release_date = Column(String)
    vector = Column(Vector(10))
