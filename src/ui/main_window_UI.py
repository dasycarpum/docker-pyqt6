# Form implementation generated from reading ui file '/home/roland/Bureau/docker-pyqt6/src/ui/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 630)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 630))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 630))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_login = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_login.setMinimumSize(QtCore.QSize(80, 0))
        self.label_login.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_login.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_login.setObjectName("label_login")
        self.gridLayout.addWidget(self.label_login, 1, 0, 1, 1)
        self.lineEdit_login = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_login.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.gridLayout.addWidget(self.lineEdit_login, 1, 1, 1, 1)
        self.textBrowser_phrase = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_phrase.setMinimumSize(QtCore.QSize(0, 100))
        self.textBrowser_phrase.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textBrowser_phrase.setObjectName("textBrowser_phrase")
        self.gridLayout.addWidget(self.textBrowser_phrase, 1, 2, 2, 3)
        self.label_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_password.setMinimumSize(QtCore.QSize(80, 0))
        self.label_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 2, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_password.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 2, 1, 1, 1)
        self.groupBox_matplotlib = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_matplotlib.setObjectName("groupBox_matplotlib")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_matplotlib)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_matplotlib = MplWidget(parent=self.groupBox_matplotlib)
        self.widget_matplotlib.setObjectName("widget_matplotlib")
        self.verticalLayout.addWidget(self.widget_matplotlib)
        self.gridLayout.addWidget(self.groupBox_matplotlib, 3, 0, 1, 2)
        self.groupBox_seaborn = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_seaborn.setObjectName("groupBox_seaborn")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_seaborn)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_seaborn = MplWidget(parent=self.groupBox_seaborn)
        self.widget_seaborn.setObjectName("widget_seaborn")
        self.verticalLayout_2.addWidget(self.widget_seaborn)
        self.gridLayout.addWidget(self.groupBox_seaborn, 3, 2, 1, 1)
        self.groupBox_plotly = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_plotly.setObjectName("groupBox_plotly")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_plotly)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_plotly = QtWidgets.QVBoxLayout()
        self.verticalLayout_plotly.setObjectName("verticalLayout_plotly")
        self.verticalLayout_4.addLayout(self.verticalLayout_plotly)
        self.gridLayout.addWidget(self.groupBox_plotly, 3, 3, 1, 2)
        self.label_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_title.setMinimumSize(QtCore.QSize(0, 80))
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 0, 1, 5)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.centralwidget)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 5)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "docker-pyqt6"))
        self.label_login.setText(_translate("MainWindow", "Login :"))
        self.label_password.setText(_translate("MainWindow", "Password :"))
        self.groupBox_matplotlib.setTitle(_translate("MainWindow", "Matplotlib"))
        self.groupBox_seaborn.setTitle(_translate("MainWindow", "Seaborn"))
        self.groupBox_plotly.setTitle(_translate("MainWindow", "Plotly"))
        self.label_title.setText(_translate("MainWindow", "Hello Docker, PyQt6, PostgreSQL and plots !"))
from src.ui.mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
