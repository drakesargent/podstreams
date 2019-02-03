from sqlalchemy.exc import TimeoutError
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from dbsetup import (Base, User, Show, Category, ShowCatLink, ShowUserLink,
                     Comment)


DB_URI = 'sqlite:///data/psdata.db'


def startSession():
    '''
    Description here
    '''
    engine = create_engine(DB_URI, connect_args={'check_same_thread': False},
                           poolclass=StaticPool)
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    return DBSession()


def addItem(item, session=startSession()):
    '''
    Description here
    '''
    try:
        session.add(item)
        session.commit()
    except TimeoutError:
        session.invalidate()
        raise
    except:
        session.rollback()
        raise


def deleteItem(item, session=startSession()):
    '''
    Description here
    '''
    try:
        session.delete(item)
        session.commit()
    except TimeoutError:
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
