#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2023-11-26

@author: Roland VANDE MAELE

@abstract: the entry point of the program.

"""

import sys
from PyQt6.QtWidgets import QApplication
from src.ui.main_window import MainWindow


def main():
    """Entry point for the PyQt6 application.

    This function creates the QApplication, initializes the main window,
    and starts the event loop.

    """
    app = QApplication(sys.argv)  # Create an instance of QApplication

    main_window = MainWindow()  # Create an instance of the main window
    main_window.show()  # Show the main window

    sys.exit(app.exec())  # Start the event loop and exit when it's finished

if __name__ == "__main__":
    main()
