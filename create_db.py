from database import Base, engine
from models import Song

Base.metadata.create_all(engine)