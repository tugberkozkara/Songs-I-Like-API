from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import SessionLocal
import models

app = FastAPI()


class Song(BaseModel):
    id: Optional[int]
    artistName:str 
    songName:str

    class Config:
        orm_mode=True


db = SessionLocal()

@app.get("/")
def home():
    return {"error": "Wrong use!",
            "try":{
                "get":["/api/songs",
                        "/api/song/<song_id>"],
                "post":"/api/songs",
                "put":"/api/song/<song_id>",
                "delete":"/api/song/<song_id>"}
            }


@app.get("/api/songs", response_model=list[Song], status_code=status.HTTP_200_OK)
def get_all_songs():
    allSongs = db.query(models.Song).all()
    return allSongs




@app.get("/api/song/{song_id}", response_model=Song, status_code=status.HTTP_200_OK)
def get_exact_song(song_id:int):
    song = db.query(models.Song).filter(models.Song.id==song_id).first()

    if song is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such song!")

    return song




@app.post("/api/songs", response_model=Song, status_code=status.HTTP_201_CREATED)
def add_song(song:Song):
    
    newSong = models.Song(
        artistName = song.artistName,
        songName = song.songName
    )
    
    existingSong = db.query(models.Song).filter(models.Song.artistName==newSong.artistName,
                                                models.Song.songName==newSong.songName).first()

    if existingSong is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Song already exists!")

    db.add(newSong)
    db.commit()

    return newSong
    



@app.put("/api/song/{song_id}", response_model=Song, status_code=status.HTTP_200_OK)
def update_song(song_id:int, song:Song):
    updateSong = db.query(models.Song).filter(models.Song.id==song_id).first()
    updateSong.artistName = song.artistName
    updateSong.songName = song.songName
    
    db.commit()

    return updateSong




@app.delete("/api/song/{song_id}")
def delete_song(song_id:int):
    deleteSong = db.query(models.Song).filter(models.Song.id==song_id).first()

    if deleteSong is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such song!")
    
    db.delete(deleteSong)
    db.commit()

    return deleteSong