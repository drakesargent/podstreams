import gevent
from app.config import DB_URI
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from dbsetup import (Base, User, Show, Category, ShowCatLink, ShowUserLink,
                     Comment)


def startSession():
    '''
    Description here
    '''
    engine = create_engine(DB_URI, connect_args={'check_same_tread': False},
                           poolclass=StaticPool)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()


def addItem(session=startSession(), item):
    '''
    Description here
    '''
    try:
        session.add(item)
        session.commit()
    except gevent.Timeout:
        session.invalidate()
        raise
    except:
        session.rollback()
        raise


def deleteItem(session=startSession(), item):
    '''
    Description here
    '''
    try:
        session.delete(item)
        session.commit()
    except gevent.Timeout:
        session.invalidate()
        raise
    except:
        session.rollback()
        raise


def updateItem(item):
    '''
    Description here
    '''
    try:
        addItem(item=self.item)
    except:
        raise


# Read Cats, Read Shows
