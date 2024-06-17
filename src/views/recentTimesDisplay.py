from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from src.controllers.timesController import TimesController

class RecentTimesDisplay(QWidget):
  def __init__(self, main_window):
    super(RecentTimesDisplay, self).__init__()
    self.recent_times_display = main_window.recentTimesDisplay
    self.times_controller = TimesController(main_window)

    # Layout variables
    self.recent_times_frame = main_window.recentTimesFrame
    self.vertical_layout_6 = main_window.verticalLayout_6

    # Render list of recent times
    self.renderList()


  def renderList(self):
    self.clearFrame()
    recent_times = self.times_controller.getRecentTimes()

    for time in recent_times:
      solve_id = time[0]
      solve_time = time[1]
      is_plus_2 = False
      is_DNF = False

      if time[4] == 1:
        is_plus_2 = True
      if time[5] == 1:
        is_DNF = True
      
      self.renderTime(solve_id, solve_time, is_plus_2, is_DNF)


  def clearFrame(self):
    while self.vertical_layout_6.count():
      item = self.vertical_layout_6.takeAt(0)
      widget = item.widget()
      if widget is not None:
        widget.deleteLater()

  def renderTime(self, solveId, solveTime, isPlus2, isDNF):
    # Create a new QFrame to contain the time record
    recentTime = QtWidgets.QFrame(self.recent_times_frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(recentTime.sizePolicy().hasHeightForWidth())
    recentTime.setSizePolicy(sizePolicy)
    recentTime.setMinimumSize(QtCore.QSize(122, 80))
    recentTime.setFrameShape(QtWidgets.QFrame.StyledPanel)
    recentTime.setFrameShadow(QtWidgets.QFrame.Raised)

    # Layout for the recentTime frame
    horizontalLayout_4 = QtWidgets.QHBoxLayout(recentTime)
    horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_4.setSpacing(15)
    horizontalLayout_4.setObjectName("horizontalLayout_4")

    # Solve count label
    solveCountLabel = QtWidgets.QLabel(recentTime)
    solveCountLabel.setObjectName("solveCountLabel")
    solveCountLabel.setStyleSheet("font-size: 14pt;")
    horizontalLayout_4.addWidget(solveCountLabel)

    # Solve time button
    solveTimeButton = QtWidgets.QPushButton(recentTime)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(solveTimeButton.sizePolicy().hasHeightForWidth())
    solveTimeButton.setSizePolicy(sizePolicy)
    solveTimeButton.setMinimumSize(QtCore.QSize(87, 0))
    solveTimeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    solveTimeButton.setStyleSheet("color: rgb(0, 181, 6); font-size: 14pt;")
    solveTimeButton.setFlat(True)
    solveTimeButton.setObjectName("solveTimeButton")
    horizontalLayout_4.addWidget(solveTimeButton)

    # Spacer
    spacerItem = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
    horizontalLayout_4.addItem(spacerItem)

    # Plus 2 button
    plus2Button = QtWidgets.QPushButton(recentTime)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(plus2Button.sizePolicy().hasHeightForWidth())
    plus2Button.setSizePolicy(sizePolicy)
    plus2Button.setMinimumSize(QtCore.QSize(25, 0))
    plus2Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    plus2Button.setFlat(True)
    plus2Button.setStyleSheet("font-size: 14pt;")
    plus2Button.setObjectName("plus2Button")
    horizontalLayout_4.addWidget(plus2Button)

    # DNF button
    dnfButton = QtWidgets.QPushButton(recentTime)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(dnfButton.sizePolicy().hasHeightForWidth())
    dnfButton.setSizePolicy(sizePolicy)
    dnfButton.setMinimumSize(QtCore.QSize(45, 0))
    dnfButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    dnfButton.setFlat(True)
    dnfButton.setStyleSheet("font-size: 14pt;")
    dnfButton.setObjectName("dnfButton")
    horizontalLayout_4.addWidget(dnfButton)

    # Delete button
    deleteTimeButton = QtWidgets.QPushButton(recentTime)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(deleteTimeButton.sizePolicy().hasHeightForWidth())
    deleteTimeButton.setSizePolicy(sizePolicy)
    deleteTimeButton.setMinimumSize(QtCore.QSize(21, 0))
    deleteTimeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    deleteTimeButton.setFlat(True)
    deleteTimeButton.setStyleSheet("font-size: 14pt;")
    deleteTimeButton.setObjectName("deleteTimeButton")
    horizontalLayout_4.addWidget(deleteTimeButton)

    # Adjust stretches
    horizontalLayout_4.setStretch(0, 1)
    horizontalLayout_4.setStretch(1, 1)
    horizontalLayout_4.setStretch(3, 1)
    horizontalLayout_4.setStretch(4, 1)
    horizontalLayout_4.setStretch(5, 1)

    # Change plus2 and DNF button color
    if isPlus2:
        plus2Button.setStyleSheet("color: #747474; font-size: 14pt;")
    if isDNF:
        dnfButton.setStyleSheet("color: #747474; font-size: 14pt;")
        solveTimeButton.setStyleSheet("color: #747474; font-size: 14pt;")

    # Set text
    _translate = QtCore.QCoreApplication.translate
    solveCountLabel.setText(_translate("recentTimesDisplay", f'{solveId}.'))
    solveTimeButton.setText(_translate("recentTimesDisplay", str(solveTime)))
    plus2Button.setText(_translate("recentTimesDisplay", "+2"))
    dnfButton.setText(_translate("recentTimesDisplay", "DNF"))
    deleteTimeButton.setText(_translate("recentTimesDisplay", "X"))

    # Add connection for the buttons
    deleteTimeButton.pressed.connect(lambda solve_id=solveId:self.deleteTime(solve_id))
    plus2Button.pressed.connect(lambda solve_id=solveId:self.plus2(solve_id))
    dnfButton.pressed.connect(lambda solve_id=solveId:self.dnf(solve_id))

    # Add the recentTime widget to vertical_layout_6
    self.vertical_layout_6.addWidget(recentTime)
  
  def deleteTime(self, solve_id):
    self.times_controller.deleteTime(solve_id)
    self.renderList()

  def plus2(self, solve_id):
    self.times_controller.plus2Time(solve_id)
    self.renderList()
  
  def dnf(self, solve_id):
    self.times_controller.dnfTime(solve_id)
    self.renderList()


   
