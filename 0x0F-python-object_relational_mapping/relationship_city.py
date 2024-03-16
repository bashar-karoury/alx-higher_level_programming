#!/usr/bin/python3
""" Modules that contains the class definition of State.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """ Class City with  attributes id, name, state_id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    """state = relationship("State", back_populates="cities")"""
