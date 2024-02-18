#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023-11-26

@author: Roland VANDE MAELE

@abstract: the main window contains all the application's interface functions.

"""

import numpy as np
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
        self.buttonBox.accepted.connect(self.handle_login)

        self.draw_a_matplotlib_plot()

    def handle_login(self):
        """Handles user login attempts.

        This method retrieves the login credentials inputted by the user, 
        attempts to authenticate these credentials, and emits a signal 
        indicating the success or failure of the authentication. If 
        authentication is successful, it updates the UI to reflect this. In 
        case of failure, it displays a warning message box.

        It uses a database session to verify credentials and handles any
        `AuthenticationException` that might occur during this process by showing a warning message.

        Args:
            None

        Returns:
            None

        Raises:
            AuthenticationException: If the authentication process fails, this
                exception is raised and caught within the method to display an
                error message to the user.

        """
        login = self.lineEdit_login.text()
        password = self.lineEdit_password.text()

        db_session = SessionLocal()
        try:
            authenticated, phrase_f, phrase_e = login_example(db_session, login, password)
            self.authentication_success.emit(authenticated)
            if authenticated:
                self.textBrowser_phrase.setText(phrase_f + '\n\n' + phrase_e)
        except AuthenticationException as e:
            QMessageBox.warning(self, "Login Failed", str(e))
            self.authentication_success.emit(False)
        finally:
            db_session.close()

    def draw_a_matplotlib_plot(self):
        """Draws a bar plot on the Matplotlib canvas within the application.

        This function creates a bar plot using Matplotlib and displays it on 
        the canvas of a custom QWidget designed to integrate Matplotlib plots 
        into the application. The data for the plot is hardcoded within the 
        function, consisting of x and y values representing the bar positions 
        and heights, respectively.

        Raises:
            TypeError: If an incorrect argument is passed to the Matplotlib bar 
            function.
        """
        # Data for plotting
        x = 0.5 + np.arange(8)  # X-axis values
        y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]  # Y-axis values (heights of the bars)

        # Attempt to create a bar plot
        try:
            widget = self.widget_matplotlib  # Reference to the Matplotlib widget in the MainWindow UI
            self.plot = widget.canvas.ax.bar(
                x, y, width=1, edgecolor="white", linewidth=0.7)  # Draw the bar plot
        except TypeError as e:
            print(f"Error drawing the matplotlib plot: {e}")
            raise
