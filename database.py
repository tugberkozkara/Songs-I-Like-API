from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os



# Local Postgres
#engine = create_engine("postgresql://postgres:postgres@localhost/songs_db",
#    echo=True
#)

# Heroku Postgres
engine = create_engine(os.environ['DATABASE_URL'])


Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)