#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023-11-28

@author: Roland VANDE MAELE

@abstract: this file is responsible for setting up and managing the database connection. 

"""

import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URI = os.getenv('DATABASE_URI')
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@contextmanager
def get_db():
    """
    Create a database session and handle its lifecycle.

    This function is a generator that creates a new SQLAlchemy session 
    using the SessionLocal factory, which is bound to the SQLAlchemy engine. 
    It yields this session to the caller and ensures that the session is 
    closed properly, regardless of whether an exception occurred or not.

    Yields:
        sqlalchemy.orm.Session: A SQLAlchemy session object that can be 
        used to interact with the database.

    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
