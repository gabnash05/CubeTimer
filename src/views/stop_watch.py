from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
import threading
import time

class StopWatch(QWidget):
  def __init__(self, main_window):
    super(StopWatch, self).__init__()
    self.timer_display = main_window.timerDisplay

    # Stopwatch variables------------------------------------------
    self.running = False
    self.time_elapsed = 0
    self.previous_time = None


  # Stopwatch functionality------------------------------------------
  def startTimer(self):
    if self.running:
      self.previous_time = self.formatTime(self.time_elapsed)
      self.time_elapsed = 0
      self.running = False
  
    else:
      self.running = True
      self.timer_thread = threading.Thread(target=self.updateTimer).start()

      ### Add stylesheet changes to other parts to make the UI non-distracting ##########################################
      

  def updateTimer(self):
    start = time.time()
    if self.running:
      until_now = self.time_elapsed
    else:
      until_now = 0
    
    while self.running:
      self.time_elapsed = time.time() - start + until_now
      self.timer_display.setText(self.formatTime(self.time_elapsed))
      time.sleep(0.01) # Prevents timer visual bugs. sometimes the milliseconds default to .00
  

  def formatTime(self, time):
    secs = time % 60
    mins = time // 60
    hours = mins // 60

    # Ensure proper time format based on duration of timer
    if hours:
      return(f"{int(hours):2d}:{int(mins):02d}:{int(secs):02d}.{int((self.time_elapsed % 1) * 100):02d}")
    if mins:
      return(f"{int(mins):2d}:{int(secs):02d}.{int((self.time_elapsed % 1) * 100):02d}")
    if secs:
      return(f"{int(secs)}.{int((self.time_elapsed % 1) * 100):02d}")
    