from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from src.models.databaseModel import DatabaseModel



class TimesController():
  def __init__(self, main_window):
    self.db = DatabaseModel()
    self.scramble = main_window.scrambleLabel.text()

  def uploadTime(self, solve_time):
    self.db.saveTimeRecord(solve_time, self.scramble)
    
  def getRecentTimes(self):
    recentTimes = self.db.getTimeRecords()
    return recentTimes

  


