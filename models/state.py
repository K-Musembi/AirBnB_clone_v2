#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Relationship - one to many; cascade delete for DBStorage)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[State] ({self.id}) {self.name}"

    #FileStorage relationship
    @property
    def cities(self):
        """Returns a list of City instances linked to the current State"""
        #Import models here to avoid circular dependencies
        from models import storage
        city_list = storage.all(City)
        return list(city_list.values())
