#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
import os
from sqlalchemy import MetaData


metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ The place class"""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete, delete-orphan",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, backref="place_amenities")

    else:
        @property
        def reviews(self):
            """There are the reviews for this place"""

            from models import storage
            list_review = []
            for review, obj in storage.__objects.items():
                if "Review" in review and (obj.place_id == Place.id):
                    list_review.append(obj)
            return list_review

        @property
        def amenities(self):
            """list all amenities instances that is linked to place"""

            from models import storage
            from models.amenity import Amenity
            list_amenities = []
            for amenity in storage.all(Amenity):
                if amenity.id in self.amenity_ids:
                    list_amenities.append(amenity)
            return list_amenties

        @amenities.setter
        def amenities(self, amenity=None):
            """Append to the amenities_ids list"""
            from models.amenity import Amenity
            if (amenity and isinstance(amenity, Amenity) and (
                    amenity.id not in self.amenity_ids)):
                Place.amenity_ids.append(amenity.id)
