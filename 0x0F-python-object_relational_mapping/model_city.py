#!/usr/bin/python3
""" This script define a city calss from the declarative_base() class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """ A state class that maps to the city table
        in the database
        __tablename__(str): name of table
        id (int): table id
        name(str): city name
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
