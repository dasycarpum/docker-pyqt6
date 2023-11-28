#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023-11-29

@author: Roland VANDE MAELE

@abstract: this ORM (Object-Relational Mapping) model represents the example
table in the PostgreSQL database with fields for login, password and phrases.

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Example(Base):
    """Represents a example within the authentication system.
    
    This class provides a Example model for the SQLAlchemy ORM and
    represents the structure and relationship of the example data in the database.
    
    Attributes:
        login (str): unique identifier, serves as the primary key
        password (str): password for the user
        phrase_french (str): french phrase after authentication
        phrase_english (str): french phrase after authentication

    """
    __tablename__ = 'example'

    login = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    phrase_french = Column(String, nullable=False)
    phrase_english = Column(String, nullable=False)

    # Representation method for debugging and logging purposes
    def __repr__(self):
        """Represents the Example object as a string.
        
        Returns:
            str: readable representation of the Example object, including the
            login.
        """
        return f"<Example(login='{self.login}')>"
