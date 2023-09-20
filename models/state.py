#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column
from models import storage
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """Getter attribute for cities"""
        city_list = []

        for city, obj in storage.__objects.items:
            if "City" in city and (obj.state_id == State.id):
                city_list.append(obj)

        return city_list
