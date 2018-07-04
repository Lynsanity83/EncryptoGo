import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMainWindow, QPushButton, QMessageBox
from cipher import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'EncryptoGo'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.move(1750,750)

        self.textbox = QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(280, 40)

        self.button = QPushButton('encipher', self)
        self.button.move(20,80)
        self.button.clicked.connect(self.on_click_encipher)

        self.button2 = QPushButton('decipher', self)
        self.button2.move(200, 80)
        self.button2.clicked.connect(self.on_click_decipher)

        self.show()

    @pyqtSlot()
    def on_click_encipher(self):
        x = cipherADFGX(self.textbox.text())
        QMessageBox.question(self, 'New Message', x.encipher(), QMessageBox.Ok)
        self.textbox.setText("")

    @pyqtSlot()
    def on_click_decipher(self):
        x = cipherADFGX(self.textbox.text())
        QMessageBox.question(self, 'New Message', x.decipher(), QMessageBox.Ok)
        self.textbox.setText("")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    sys.exit(app.exec_())


