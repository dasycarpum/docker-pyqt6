#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023-11-26

@author: Roland VANDE MAELE

@abstract: the main window contains all the application's interface functions.

"""

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSignal
import src.ui.main_window_UI as window
from src.business_logic.authentication import login_example,   AuthenticationException
from src.dal.database import SessionLocal


class MainWindow(QMainWindow, window.Ui_MainWindow):
    authentication_success = pyqtSignal(bool)
    """Main application window for the PyQt6 application.

    This class represents the main window of the application, inheriting from
    QMainWindow and the generated Ui_MainWindow class from Qt Designer.
    It initializes the UI components and sets up the main window.

    Attributes:
        None specific, inherits attributes from QMainWindow and Ui_MainWindow.

    Args:
        parent (QWidget, optional): The parent widget of this main window.
            Defaults to None, which means no parent widget.

    """
    def __init__(self, parent=None):
        """Initializes the MainWindow instance.

        This constructor initializes the main window with the parent widget,
        sets up the user interface components, and performs any additional
        setup required for the MainWindow.

        Args:
            parent (QWidget, optional): The parent widget of this main window.
                Passed to the QMainWindow constructor. Defaults to None.

        Returns:
            None

        """
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.handle_login)

    def handle_login(self):
        """Handles user login attempts.

        This method retrieves the login credentials inputted by the user, attempts to authenticate these credentials, and emits a signal indicating the success or failure of the authentication. If authentication is successful, it updates the UI to reflect this. In case of failure, it displays a warning message box.

        It uses a database session to verify credentials and handles any
        `AuthenticationException` that might occur during this process by showing a warning message.

        Args:
            None

        Returns:
            None

        Raises:
            AuthenticationException: If the authentication process fails, this
                exception is raised and caught within the method to display an error message to the user.

        """
        login = self.lineEdit_login.text()
        password = self.lineEdit_password.text()

        db_session = SessionLocal()
        try:
            authenticated = login_example(db_session, login, password)
            self.authentication_success.emit(authenticated)
            if authenticated:
                self.textBrowser_phrase.setText("OK")
        except AuthenticationException as e:
            QMessageBox.warning(self, "Login Failed", str(e))
            self.authentication_success.emit(False)
        finally:
            db_session.close()
