import time
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import os

from .views.stopwatch import StopWatch
from .models.databaseModel import DatabaseModel


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

    # Database Test
    #self.database = DatabaseModel(self)

    # Key event trackers
    self.space_bar_pressed = False
    self.last_key_time = 0
    self.debounce_threshold = 0.04  # Set debounce threshold in seconds











  # Handle key events
  def keyPressEvent(self, event):
    current_time = time.time()
    if event.key() == Qt.Key_Space and current_time - self.last_key_time >= self.debounce_threshold:
      self.stop_watch.timer_display.setStyleSheet("color: rgb(0, 181, 6)")

  def keyReleaseEvent(self, event):
    current_time = time.time()
    if event.key() == Qt.Key_Space and current_time - self.last_key_time >= self.debounce_threshold:
      
      self.stop_watch.timer_display.setStyleSheet("color: rgb(243, 243, 243)")
      self.stop_watch.startTimer()
      
      self.space_bar_pressed = False
    
      if not self.stop_watch.running:
          print(f'Your time is: {self.stop_watch.previous_time}')

    self.last_key_time = time.time()  # Reset last_press_time on valid release
           
  
  # Handle close window event to prevent thread issues
  def closeEvent(self, event):

    if self.stop_watch.running:
      self.stop_watch.startTimer()
      super().closeEvent(event)
  
