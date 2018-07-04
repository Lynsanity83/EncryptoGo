"""
Simple encrypting and decrypting program.

@author Lynor Wilson
@version 1.0
Created 2018-07-04

© EncrypToGo 2018
"""

import os
import sys

from PyQt5.QtGui import QIcon

from GUI import *


app = QtWidgets.QApplication(sys.argv)
path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'venv\media\icon.png')
app.setWindowIcon(QIcon(path))
window = ETG_Main_Window()
window.show()

sys.exit(app.exec_())



