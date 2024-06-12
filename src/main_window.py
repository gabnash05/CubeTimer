from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import os

from .views.stop_watch import StopWatch


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    # Load UI File
    ui_path = os.path.join(os.path.dirname(__file__), "E:/Programming/Programming Practice/CubeTimer/src/ui/cubeTimer.ui")
    uic.loadUi(ui_path, self)

    # Set up
    self.setFocusPolicy(Qt.StrongFocus)
    self.setFocus()

    # UI Components
    self.stop_watch = StopWatch(self)














  # Handle key events
  def keyPressEvent(self, event):
    pass
    
  
  def keyReleaseEvent(self, event):
    if event.key() == Qt.Key_Space:
      self.stop_watch.startTimer()
    
    if not self.stop_watch.running:
      print(f'Your time is: {self.stop_watch.previous_time}')
      ### Add timelist connector to save times ##########################################
           
  
  # Handle close window event to prevent thread issues
  def closeEvent(self, event):

    if self.stop_watch.running:
      self.stop_watch.startTimer()
      super().closeEvent(event)
  
