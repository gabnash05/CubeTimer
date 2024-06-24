from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from src.models.databaseModel import DatabaseModel


class TimesController():
  def __init__(self, main_window):
    self.db = DatabaseModel()
    self.main_window = main_window
    

  def uploadTime(self, solve_time):
    self.scramble = self.main_window.scrambleLabel.text()
    self.db.saveTimeRecord(solve_time, self.scramble)
    
  def getRecentTimes(self):
    recent_times = self.db.getTimeRecords()
    return recent_times

  def searchTime(self, solve_id):
    try:
      return self.db.searchTimeRecord(solve_id)
    except Exception as e:
      print(str(e))

  def deleteTime(self, solve_id):
    try:
      if self.confirmDeletion():
        self.db.deleteTimeRecord(solve_id)
        self.main_window.stop_watch.recent_times_display.renderList()
        return True
      else:
        return False
    except Exception as e:
      print(str(e))
      return False
  
  def plus2Time(self, solve_id):
    self.db.plus2TimeRecord(solve_id)

  def dnfTime(self, solve_id):
    self.db.dnfTimeRecord(solve_id)
  
  def getPBTime(self):
    return self.db.getPbRecord()

  def getWorstTime(self):
    return self.db.getWorstRecord()

  def updateAo5(self):
    self.db.saveAo5Records()
  
  def updateAo12(self):
    self.db.saveAo12Records()

  def getAo5(self):
    self.updateAo5()
    return self.db.getAo5Record()
  
  def getAo12(self):
    self.updateAo12()
    return self.db.getAo12Record()
      
  def getAo5Pb(self):
    self.updateAo5()
    return self.db.getAo5PbRecord()

  def getAo12Pb(self):
    self.updateAo12()
    return self.db.getAo12PbRecord()

  def getAverageTime(self):
    return self.db.getTotalAverageRecord()

  def searchAo5(self, ao5_date):
    return self.db.searchAo5(ao5_date)

  def searchAo12(self, ao12_date):
    return self.db.searchAo12(ao12_date)
    
  def updateScramble(self, solve_id, solve_scramble):
    self.db.updateTimeScramble(solve_id, solve_scramble)



  def confirmDeletion(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setWindowTitle("Confirm Deletion")
    msgBox.setText("Are you sure you want to delete this Time Record?")
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msgBox.setDefaultButton(QMessageBox.Yes)
    msgBox.setStyleSheet("""
                        QMessageBox {
                          font: 100 12pt "Gill Sans MT";
                          background-color: rgb(31, 31, 40);
                        }
                        QLabel {
                          background-color: rgb(31, 31, 40);
                          color: rgb(243, 243, 243);
                        }
                        QPushButton {
                          background-color: rgb(51, 51, 60);
                          color: rgb(243, 243, 243);
                          border: none;
                          border-radius: 5px;
                          padding: 4px;
                          min-width: 80px;
                          font: 10pt "Gill Sans MT";
                        }
                        QPushButton:hover {
                          background-color: rgb(71, 71, 80);
                         }
                        QPushButton:focus {
                          border: 2px solid rgb(243, 243, 243);
                          }
                        """)
    
    return_value = msgBox.exec()
    if return_value == QMessageBox.Yes:
        return True
    else:
        return False

  


