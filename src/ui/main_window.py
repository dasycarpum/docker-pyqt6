#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023-11-26

@author: Roland VANDE MAELE

@abstract: the main window contains all the application's interface functions.

"""

from PyQt6.QtWidgets import QMainWindow
import src.ui.main_window_UI as window


class MainWindow(QMainWindow, window.Ui_MainWindow):
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
