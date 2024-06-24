from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import os

from src.controllers.timesController import TimesController
from src.util.formatFunctions import formatTime

class TimeInfoBox(QMainWindow):
  def __init__(self, solve_id, recentTimesDisplay, main_window):
    super(TimeInfoBox, self).__init__()
    # Load UI
    self.centralWidget = QWidget(self)
    self.setCentralWidget(self.centralWidget)
    self.layout = QVBoxLayout(self.centralWidget)

    self.setMaximumWidth(1000)
    self.setFixedHeight(650)

    # Keep window on top
    self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)

    self.times_controller = TimesController(main_window)
    self.recent_times_display = recentTimesDisplay
    self.main_window = main_window
    
    # State variables
    self.solve_id = solve_id
    self.isEditing = False

    self.renderUi()

  
  
  def renderUi(self):
    self.ui_path = os.path.join(os.path.dirname(__file__), "E:/Programming/Programming Practice/CubeTimer/src/ui/timeInfo.ui")
    self.timeInfoBox = uic.loadUi(self.ui_path)
    self.layout.addWidget(self.timeInfoBox)

    # Fetch time info
    self.solve = self.times_controller.searchTime(self.solve_id)
    self.solve_time = self.solve[0][1]
    self.solve_scramble = self.solve[0][2]
    self.solve_date = self.solve[0][3]
    self.solve_is_plus_2 = self.solve[0][4]
    self.solve_is_DNF = self.solve[0][5]

    if self.solve_is_DNF == 0:
      ao5 = self.times_controller.searchAo5(self.solve_date)
      ao5_time = ao5[0][1]

      ao12 = self.times_controller.searchAo12(self.solve_date)
      ao12_time = ao12[0][1]

    # Set Text and Styles
    self.timeInfoBox.scrambleInput_2.setText(str(self.solve_scramble))
    self.timeInfoBox.dateLabel_2.setText(str(self.solve_date))
    # DNF
    if self.solve_is_DNF == 0:
      self.timeInfoBox.timeLabel_2.setText(str(formatTime(self.solve_time)))
      self.timeInfoBox.ao5Label_2.setText("ao5: " + str(formatTime(ao5_time)))
      self.timeInfoBox.ao12Label_2.setText("ao12: " + str(formatTime(ao12_time)))
      self.timeInfoBox.dnfButton_2.setStyleSheet("background-color: rgb(31, 31, 40);")
    else:
      self.timeInfoBox.timeLabel_2.setText("DNF")
      self.timeInfoBox.ao5Label_2.setText("ao5: ")
      self.timeInfoBox.ao12Label_2.setText("ao12: ")
      self.timeInfoBox.dnfButton_2.setStyleSheet("background-color: rgb(61, 61, 70);")
    # Plus 2
    if self.solve_is_plus_2 == 1:
      self.timeInfoBox.plus2Button_2.setStyleSheet("background-color: rgb(61, 61, 70);")
    else:
      self.timeInfoBox.plus2Button_2.setStyleSheet("background-color: rgb(31, 31, 40);")

    # Connect Buttons
    self.timeInfoBox.exitButton_2.pressed.connect(self.close)
    self.timeInfoBox.plus2Button_2.pressed.connect(lambda solve_id=self.solve_id: self.plus2Time(solve_id))
    self.timeInfoBox.dnfButton_2.pressed.connect(lambda solve_id=self.solve_id: self.dnfTime(solve_id))
    self.timeInfoBox.editButton_2.pressed.connect(self.editTime)
    self.timeInfoBox.saveButton_2.pressed.connect(self.saveEdits)
    self.timeInfoBox.deleteButton_2.pressed.connect(self.deleteTime)
    self.timeInfoBox.copyScrambleButton_2.pressed.connect(self.copyScramble)

    # is editing
    if self.isEditing:
      self.timeInfoBox.plus2Button_2.setEnabled(True)
      self.timeInfoBox.dnfButton_2.setEnabled(True)
      self.timeInfoBox.scrambleInput_2.setEnabled(True)
      self.setStyleSheet("QMainWindow{background-color: rgb(18, 18, 36)}")
      self.timeInfoBox.editButton_2.hide()
      self.timeInfoBox.saveButton_2.show()
      self.timeInfoBox.exitButton_2.hide()
    else:
      self.setStyleSheet("QMainWindow{background-color: rgb(18, 18, 25)}")
      self.timeInfoBox.editButton_2.show()
      self.timeInfoBox.saveButton_2.hide()
      self.timeInfoBox.exitButton_2.show()
    

  def copyScramble(self):
    clipboard = QApplication.clipboard()
    scramble = self.timeInfoBox.scrambleInput_2.text()

    clipboard.setText(scramble)
    self.scrambleCopiedPopup()
  
  def scrambleCopiedPopup(self, message="Scramble copied"):
    popup = QDialog(self, Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    popup.setAttribute(Qt.WA_TranslucentBackground)
    popup.setStyleSheet("background-color: rgba(18, 18, 25, 60%); color: rgb(243, 243, 243); border-radius: 5px; padding: 15px;")

    layout = QHBoxLayout()
    label = QLabel(message, popup)
    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label)
    
    popup.setLayout(layout)
    popup.adjustSize()
    popup.move(self.geometry().center() - popup.rect().center())
    popup.show()
    
    # Automatically close the popup after 2 seconds
    QTimer.singleShot(1000, popup.close)

  def editTime(self):
    self.timeInfoBox.plus2Button_2.setEnabled(True)
    self.timeInfoBox.dnfButton_2.setEnabled(True)
    self.timeInfoBox.scrambleInput_2.setEnabled(True)

    self.timeInfoBox.editButton_2.hide()
    self.timeInfoBox.saveButton_2.show()
    self.timeInfoBox.exitButton_2.hide()

    self.setStyleSheet("QMainWindow{background-color: rgb(18, 18, 36)}")
    self.isEditing = True
  
  def saveEdits(self):
    self.timeInfoBox.plus2Button_2.setEnabled(False)
    self.timeInfoBox.dnfButton_2.setEnabled(False)
    self.timeInfoBox.scrambleInput_2.setEnabled(False)

    self.timeInfoBox.editButton_2.show()
    self.timeInfoBox.saveButton_2.hide()

    self.editScramble(self.solve_id, self.timeInfoBox.scrambleInput_2.text())
    self.isEditing = False
    self.close()

  def editScramble(self, solve_id, solve_scramble):
    self.times_controller.updateScramble(solve_id, solve_scramble)
    self.clearFrame()
    self.renderUi()

  def plus2Time(self, solve_id):
    self.times_controller.plus2Time(solve_id)
    self.times_controller.updateAo5()
    self.times_controller.updateAo12()
    self.clearFrame()
    self.renderUi()
  
  def dnfTime(self, solve_id):
    self.times_controller.dnfTime(solve_id)
    self.times_controller.updateAo5()
    self.times_controller.updateAo12()
    self.clearFrame()
    self.renderUi()
  
  def clearFrame(self):
    # Clear all widgets from the central widget layout
    central_widget = self.centralWidget
    if central_widget:
      layout = central_widget.layout()
    if layout:
      for i in reversed(range(layout.count())):
        widget_to_remove = layout.itemAt(i).widget()
        layout.removeWidget(widget_to_remove)
        widget_to_remove.setParent(None)
  
  def deleteTime(self):
    self.close()
    self.times_controller.deleteTime(self.solve_id)

  def closeEvent(self, event):
    self.main_window.startUpdateTimeThread()
    self.main_window.is_viewing_time = False
    self.recent_times_display.renderList()
    event.accept()



