import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMainWindow, QPushButton, QMessageBox
from cipher import *
from GUI import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'EncryptoGo'
