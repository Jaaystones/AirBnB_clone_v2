#!/bin/bash/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from models.engine.file_storage import FileStorage
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class / table model"""
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan",
                              backref="state")
    else:
        name = ""

        @property
        def cities(self) -> list:
            """Getter for all City instances with state_id == State.id"""
            city_list = []
            fs = FileStorage()
            all_cities = fs.all(City)
            
            for key, value in all_cities.items():
            if all_cities[key].__dict__["state_id"] == self.id:
                city_list.append({key: value})
        return city_list
