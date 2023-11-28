#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023-11-28

@author: Roland VANDE MAELE

@abstract: handles the logic of the authentication process

"""

from sqlalchemy.orm import Session
from src.dal.example_repository import ExampleRepository


class AuthenticationException(Exception):
    """Exception raised for errors in the authentication process.

    Attributes:
        message -- explanation of the error

    """
    def __init__(self, message="Authentication failed"):
        self.message = message
        super().__init__(self.message)


def login_example(db_session: Session, login: str, password: str) -> bool:
    """
    Authenticates a example based on login credentials.

    Args:
        db_session (Session): The SQLAlchemy session for database operations.
        login (str): The login identifier for the example.
        password (str): The password for the example.

    Returns:
        bool: True if authentication is successful, False otherwise.

    Raises:
        AuthenticationException: If authentication fails due to incorrect login or password.
    """
    example_repo = ExampleRepository(db_session)

    # Retrieve the example by login
    example = example_repo.get_example_by_login(login)
    if not example:
        raise AuthenticationException(f"Login failed: No user found with login {login}.")

    # Check if the provided password matches
    if example.password != password:
        raise AuthenticationException("Login failed: Incorrect password.")

    return True
