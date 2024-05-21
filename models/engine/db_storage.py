#!/usr/bin/python3
'''Database storage engine'''


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from os import getenv

Base = declarative_base()

class DBStorage:
    '''Database storage'''

    __engine = None
    __session = None

    def __init__(self):
        '''Initialize object'''

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                format(
                    getenv("HBNB_MYSQL_USER"),
                    getenv("HBNB_MYSQL_PWD"),
                    getenv("HBNB_MYSQL_HOST"),
                    getenv("HBNB_MYSQL_DB")),
                pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Query current database session'''

        # Query all objects based on class name
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = self.__session.query(BaseModel).all()

        # Return dictionary with key and value as class-name.object-id and object
        return {obj.__class__.__name__ + '.' + obj.id: obj for obj in objects}

    def new(self, obj):
        '''Add object to current session'''
        self.__session.add(obj)

    def save(self):
        '''Commit all changes to the database'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Delete object from session if provided'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''Create all tables in the database and create new session'''
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        '''Close session'''
        if self.__session is not None:
            self.__session.close()
