from sqlalchemy import Column, Integer, String
from database import Base

class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True)
    artistName = Column(String(200), nullable=False)
    songName = Column(String(200),nullable=False)

    def __repr__(self):
        return f"<Song(artistName= {self.artistName}, songName= {self.songName})>"