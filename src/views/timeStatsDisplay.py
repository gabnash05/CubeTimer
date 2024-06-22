import threading
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

from src.controllers.timesController import TimesController
from src.util.formatFunctions import formatTime

class TimeStatsDisplay(QWidget):
  def __init__(self, main_window):
    super(TimeStatsDisplay, self).__init__()
    self.times_controller = TimesController(main_window)
    
    self.pb_display = main_window.pbDisplay
    self.ao5_pb_display = main_window.ao5pbDisplay
    self.ao12_pb_display = main_window.ao12pbDisplay
    self.worst_display = main_window.worstDisplay
    self.avg_display = main_window.avgDisplay
    self.ao5_display = main_window.ao5Display
    self.ao12_display = main_window.ao12Display

    # Time stats display--------------------------------------------
    self.renderStatsDisplay()
    
  
  def renderStatsDisplay(self):
    self.updatePb()
    self.updateAo5Pb()
    self.updateAo12Pb()
    self.updateWorst()
    self.updateAo5()
    self.updateAo12()
    self.updateAverage()
  
  def updatePb(self):
    pb_time = formatTime(self.times_controller.getPBTime())
    self.pb_display.setText(pb_time)
  
  def updateAo5Pb(self):
    ao5Pb = formatTime(self.times_controller.getAo5Pb())
    self.ao5_pb_display.setText(ao5Pb)
  
  def updateAo5(self):
    ao5 = formatTime(self.times_controller.getAo5())
    self.ao5_display.setText(ao5)

  def updateAo12Pb(self):
    ao12Pb = formatTime(self.times_controller.getAo12Pb())
    self.ao12_pb_display.setText(ao12Pb)
  
  def updateAo12(self):
    ao12 = formatTime(self.times_controller.getAo12())
    self.ao12_display.setText(ao12)

  def updateWorst(self):
    worst_time = formatTime(self.times_controller.getWorstTime())
    self.worst_display.setText(worst_time)
  
  def updateAverage(self):
    average_time = formatTime(self.times_controller.getAverageTime())
    self.avg_display.setText(average_time)