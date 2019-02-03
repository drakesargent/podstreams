import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Class Declarations for Tables


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    name = Column(String(80), nullable=False)
    user = relationship(User)


class Show(Base):
    __tablename__ = 'show'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(80), nullable=False)
    link = Column(String(80))
    user = relationship(User)


class ShowCatLink(Base):
    __tablename__ = 'showCatLink'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    show_id = Column(Integer, ForeignKey(Show.id), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    user = relationship(User)
    show = relationship(Show)
    category = relationship(Category)


class ShowUserLink(Base):
    __tablename__ = 'showUserLink'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    show_id = Column(Integer, ForeignKey(Show.id), nullable=False)
    user = relationship(User)
    show = relationship(Show)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    show_id = Column(Integer, ForeignKey(Show.id), nullable=False)
    text = Column(Text, nullable=False)
    createDate = Column(Date, nullable=False)
    updateDate = Column(Date)
    user = relationship(User)
    show = relationship(Show)

# Create db and bind

engine = create_engine('sqlite:///data/psdata.db')
Base.metadata.create_all(engine)

if __name__ == "__main__":
    return
