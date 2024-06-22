from threading import Event, Thread
import threading
import time
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import os

from src.views.stopwatch import StopWatch
from src.views.recentTimesDisplay import RecentTimesDisplay
from src.views.scrambleDisplay import ScrambleDisplay
from src.views.timeStatsDisplay import TimeStatsDisplay


class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    # Load UI File
    ui_path = os.path.join(os.path.dirname(__file__), "E:/Programming/Programming Practice/CubeTimer/src/ui/cubeTimer.ui")
    uic.loadUi(ui_path, self)

    # Set up
    self.setFocusPolicy(Qt.StrongFocus)
    self.setFocus()
    
    # Initialize Thread the stop event
    self.stop_event = Event()

    # UI Components
    self.stop_watch = StopWatch(self)
    self.time_stats_display = TimeStatsDisplay(self)

    # Key event trackers
    self.last_key_time = 0
    self.debounce_threshold = 0.04  # Set debounce threshold in seconds
    
    self.viewing_mode = "Default"

    # Separate threads
    self.time_stats_thread = threading.Thread(target=self.updateTimeStats)
    self.time_stats_thread.start()



    # UI buttons
    self.viewing_mode_combobox = self.viewingModeComboBox
    self.viewing_mode_combobox.currentTextChanged.connect(self.changeViewingMode)
    self.exit_focus_button = self.exitFocusButton
    self.exit_focus_button.hide()
    self.exit_focus_button.pressed.connect(self.exitFocusMode)
  


  # Viewing mode update
  def changeViewingMode(self, value):
    if value == "Default":
      self.viewing_mode = "Default"
      self.exit_focus_button.hide()
      self.showNormal()
    if value == "Fullscreen":
      self.viewing_mode = "Fullscreen"
      self.exit_focus_button.hide()
      self.showFullScreen()
    if value == "Focus Mode":
      self.menuFrame.hide()
      self.statsFrame.hide()
      self.exit_focus_button.show()

  def exitFocusMode(self):
    self.menuFrame.show()
    self.statsFrame.show()
    self.changeViewingMode(self.viewing_mode)
    print(self.viewing_mode)
    self.viewing_mode_combobox.setCurrentText(self.viewing_mode)


  # Constant Time Stats update------------------------------------------------------------------
  def updateTimeStats(self):
    while not self.stop_event.is_set():
      self.time_stats_display.renderStatsDisplay()
      time.sleep(.5)  # Adding sleep to prevent tight loop
  


  # Handle key events------------------------------------------------------------------
  def keyPressEvent(self, event):
    current_time = time.time()
    if event.key() == Qt.Key_Space and current_time - self.last_key_time >= self.debounce_threshold:
      self.stop_watch.timer_display.setStyleSheet("color: rgb(0, 181, 6)")

  def keyReleaseEvent(self, event):
    current_time = time.time()
    if self.stop_watch.running and current_time - self.last_key_time >= self.debounce_threshold:
      self.stop_watch.startTimer()
      self.stop_watch.timer_display.setStyleSheet("color: rgb(243, 243, 243)")

    elif event.key() == Qt.Key_Space and current_time - self.last_key_time >= self.debounce_threshold:
      self.stop_watch.timer_display.setStyleSheet("color: rgb(243, 243, 243)")
      self.stop_watch.startTimer()
        
    self.last_key_time = time.time()  # Reset last_press_time on valid release
    
           
  
  # Handle close window event to prevent thread issues
  def closeEvent(self, event):
    self.stop_event.set()
    self.time_stats_thread.join()
    
    # Stopwatch
    if self.stop_watch.running:
      self.stop_watch.startTimer()
      super().closeEvent(event)
    
    super().closeEvent(event)
  
