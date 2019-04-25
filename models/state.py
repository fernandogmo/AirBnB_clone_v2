#!/usr/bin/python3
"""This is the state class"""
import os
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """
    This is the class for State objects.
    It is associated with the SQL table 'states'.

    Attributes:
        name: String, 128 characters
    """
    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)

    if 'HBNB_TYPE_STORAGE' in os.environ:
        if os.environ['HBNB_TYPE_STORAGE'] == 'db':
            cities = relationship('City',
                                  cascade='delete, delete-orphan',
                                  backref='state')
        elif os.environ['HBNB_TYPE_STOREGE'] == 'fs':
            @property
            def cities(self):
                """Property getter of list of city instances
                where state_id equals current State.id"""
                city_dict = storage.all(City)
                return [city for city in city_dict.values()
                        if city.state_id == self.id]
