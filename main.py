from PyQt5.QtWidgets import *
from src.mainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Cube Timer")
    window.show()
    app.exec()

# BAZINGA!!!