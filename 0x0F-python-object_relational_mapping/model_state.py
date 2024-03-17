#!/usr/bin/python3

"""
Write a python file that contains the class definition of a State
and an instance Base.
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

""" Creating the directive base """
Base = declarative_base()


class State(Base):
    """
     The state Class Definition
    Params:
       id: id field ogf the class
       name: state name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
