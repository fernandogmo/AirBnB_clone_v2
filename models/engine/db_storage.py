#!/usr/bin/python3
"""
This DBStorage class will serve as the
storage engine for AirBnB clone objects.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
    """
    __engine = None
    __session = None
    all_classes = ['Amenity',
                   'City',
                   'Place',
                   'Review',
                   'State',
                   'User']

    def __init__(self):
        """
        Instantiation of DBStorage class.

        Creates engine and links it to MySQL database.
        Parameters for linking to MySQL database are
        retrieved via environment variables:

        HBNB_MYSQL_USER: MySQL username
        HBNB_MYSQL_PWD: MySQL password
        HBNB_MYSQL_HOST: MySQL host to connect to
        HBNB_MYSQL_DB: MySQL database
        HBNB_ENV: test or db. db: actual database, test: isolated environment
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.environ['HBNB_MYSQL_USER'],
                                              os.environ['HBNB_MYSQL_PWD'],
                                              os.environ['HBNB_MYSQL_HOST'],
                                              os.environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)
        try:
            if os.environ['HBNB_ENV'] == 'test':
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        """
        Query objects from current database session.

        If cls is given, all objects of that class will be queried.
        If not, all objects will be queried.

        Returns a dictionary with all objects queried.
        """
        obj_dict = {}
        all_objs = []
        if cls:
            all_objs = self.__session.query(eval(cls)).all()
        else:
            for table in self.all_classes:
                all_objs += self.__session.query(eval(table)).all()
        obj_dict = {obj.__class__.__name__ + '.' + obj.id: obj
                    for obj in all_objs}
        # TODO BUG: includes <sqlalchemy> object in dict
        return obj_dict

    def new(self, obj):
        """
        Adds obj to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits/saves all changes of current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from current database session if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in database and
        create current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ Closes the current session """
        self.__session.close()
