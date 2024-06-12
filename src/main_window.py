from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('cubeTimer.ui', self)




