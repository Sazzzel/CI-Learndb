from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#executing the instruction from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# Instead of connecting the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the session() subclass defined above
session = Session()

# create the database using declarative_base subclass
base.metadata.create_all(db)


