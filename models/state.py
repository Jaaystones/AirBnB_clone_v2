#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models import storage


class State(BaseModel):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
    
    if getenv('HBNB_TYPE_STORAGE') !== 'db':
        @property
        def cities(self):
            """Returns the list of City objects from storage
            linked to the current State"""
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
