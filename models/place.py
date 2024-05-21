#!/usr/bin/python3
""" Place Module for HBNB project """


from models.base_model import BaseModel, Base, place_amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

#Defined in base_model, imported in place.py and amenity.py
'''place_amenity = Table(
    "place_amenities",
    Base.metadata,
    extend_existing=True,
    Column("place_id", String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)'''


class Place(BaseModel, Base):
    """ A place to stay """
    
    __tablename__ = 'places'

    place_id = Column(String(60), ForeignKey('places.id'), primary_key=True, nullable=False)

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
    city = relationship("City", back_populates="places")

    # Relationship with Amenity model (Many-to-Many for DBStorage)
    amenities = relationship(
        "Amenity",  # Many-to-Many with Amenity
        secondary=place_amenity,
        backref='places',  # Backreference on Amenity
        viewonly=False  # Allow modifications for DBStorage
    )

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[Place] ({self.id}) {self.name}"

    # FileStorage relationship (getter property)
    @property
    def reviews(self):
        """Returns a list of Review instances linked to the current Place"""
        # Import models here to avoid circular dependencies
        from models import storage
        review_list = storage.all(Review, place_id=self.id)
        return list(review_list.values())

    @property
    def amenities(self):
        """Returns a list of Amenity instances linked to the current Place"""
        # Import models here to avoid circular dependencies
        from models import storage
        if self.amenity_ids:
            amenity_list = storage.all(Amenity, amenity_id=self.amenity_ids.split(","))
            return list(amenity_list.values())
        else:
            return []

    @amenities.setter
    def amenities(self, amenity):
        """Adds an Amenity.id to the amenity_ids attribute (FileStorage)"""
        from models.amenity import Amenity

        if isinstance(amenity, Amenity):
            if self.amenity_ids is None:
                self.amenity_ids = str(amenity.id)
            else:
                self.amenity_ids += "," + str(amenity.id)
