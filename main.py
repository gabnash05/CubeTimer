from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from src.mainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Cube Timer")
    window.show()
    app.exec()

# TIME DETAILS