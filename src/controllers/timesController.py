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
    recent_times = self.db.getTimeRecords()
    return recent_times

  def deleteTime(self, solve_id):
    try:
      if self.confirmDeletion():
        self.db.deleteTimeRecord(solve_id)
    except Exception as e:
      print(str(e))
  

  def plus2Time(self, solve_id):
    self.db.plus2TimeRecord(solve_id)


  def dnfTime(self, solve_id):
    self.db.dnfTimeRecord(solve_id)


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

  


