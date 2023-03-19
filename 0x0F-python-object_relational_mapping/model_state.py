#!/usr/bin/python3
""" This script define a state calss from the declarative_base() class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ A state class that maps to the state table
        in the database
        __tablename__(str): name of table
        id (int): table id
        name(str): state name
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
