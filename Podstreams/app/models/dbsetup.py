import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

### Class Declarations for Tables ###

### Create db and bind ###

engine = create_engine('sqlite:///data/psdata.db')
Base.metadata.create_all(engine)
