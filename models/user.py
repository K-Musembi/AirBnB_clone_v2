#!/usr/bin/python3
"""This module defines a class User"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship(
            "Place", backref="user", cascade="all, delete-orphan")
    reviews = relationship(
            "Review", backref="user", cascade="all, delete-orphan")


    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[User] ({self.id}) {self.email}"
