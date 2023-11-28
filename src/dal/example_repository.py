#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023-11-28

@author: Roland VANDE MAELE

@abstract: abstracts the data access for examples

"""

import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.example import Example

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class ExampleRepository:
    """Handles operations related to Example data in the database.

    This repository class provides methods to interact with the Example
    data in the database.

    Attributes:
        db_session (Session): A SQLAlchemy session instance for database operations.

    """
    def __init__(self, db_session: Session):
        """Initializes the ExampleRepository with a database session.

        Args:
            db_session (Session): The SQLAlchemy session for database operations.

        """
        self.db_session = db_session

    def get_example_by_login(self, login: str):
        """Retrieve a example by their login.

        Queries the database for a Example with the specified login. If a 
        example is found, returns the Example object, otherwise returns None.

        Args:
            login (str): The login identifier of the example.

        Returns:
            Example or None: The Example object if found, otherwise None.

        """
        try:
            example = self.db_session.query(Example).filter_by(login=login).first()
            return example
        except SQLAlchemyError as e:
            logging.error("An error occurred when fetching the example: %s", e)
            return None
