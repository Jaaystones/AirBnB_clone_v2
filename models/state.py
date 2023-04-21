#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """State class"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        if storage_type == db:
            __tablename__ = 'states'
            name = Column(String(128), nullable=False)
            cities = relationship('City', cascade='all, delete', backref='state')
    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
            with state_id == current State.id"""
            from models import storage
            cities_dict = storage.all(City)
            return [city for city in cities_dict.values() if city.state_id == self.id]
