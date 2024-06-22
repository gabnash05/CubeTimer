from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
import threading
import time

from src.controllers.timesController import TimesController
from src.views.recentTimesDisplay import RecentTimesDisplay
from src.views.scrambleDisplay import ScrambleDisplay
from src.views.timeStatsDisplay import TimeStatsDisplay
from src.util.formatFunctions import formatTime


class StopWatch(QWidget):
  def __init__(self, main_window):
    super(StopWatch, self).__init__()
    self.timer_display = main_window.timerDisplay

    # Initialize other Components
    self.times_controller = TimesController(main_window)
    self.recent_times_display = RecentTimesDisplay(main_window)
    self.scramble_display = ScrambleDisplay(main_window)


    # Stopwatch variables------------------------------------------
    self.running = False
    self.time_elapsed = 0
    self.previous_time = None

    
  


  # Stopwatch functionality------------------------------------------
  def startTimer(self):
    if self.running:
      self.previous_time = self.time_elapsed
      self.time_elapsed = 0
      self.running = False
      
      # Use times_controller to save time into databases
      self.times_controller.uploadTime(self.previous_time)

      # Update recent times
      self.recent_times_display.renderList()
      self.scramble_display.renderScramble()
      
    else:
      self.running = True
      self.timer_thread = threading.Thread(target=self.updateTimer)
      self.timer_thread.start()

      ### Add stylesheet changes to other parts to make the UI non-distracting ##########################################
      

  def updateTimer(self):
    start = time.time()
    if self.running:
      until_now = self.time_elapsed
    else:
      until_now = 0
    
    while self.running:
      self.time_elapsed = time.time() - start + until_now
      self.timer_display.setText(formatTime(self.time_elapsed))
      time.sleep(0.01) # Prevents timer visual bugs. sometimes the milliseconds default to .00

    