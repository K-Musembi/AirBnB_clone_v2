#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base, place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Representation of an amenity"""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    amenity_id = Column(String(60), primary_key=True, nullable=False)

    places = relationship('Place', secondary=place_amenity, backref='amenities')

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[Amenity] ({self.id}) {self.name}"


# This relationship definition needs to be placed outside the Amenity class
# for Many-to-Many relationships with SQLAlchemy
