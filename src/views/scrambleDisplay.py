from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QClipboard
from PyQt5.QtCore import QTimer, Qt

from src.util.generateScramble import generateScramble

class ScrambleDisplay(QWidget):
  def __init__(self, main_window):
    super(ScrambleDisplay, self).__init__()
    self.scramble_display = main_window.scrambleLabel
    self.edit_scramble_button = main_window.editScrambleButton
    self.lock_scramble_button = main_window.lockScrambleButton
    self.copy_scramble_button = main_window.copyScrambleButton
    self.reset_scramble_button = main_window.resetScrambleButton

    # Bind buttons
    self.edit_scramble_button.pressed.connect(self.editScramble)
    self.lock_scramble_button.pressed.connect(self.lockScramble)
    self.copy_scramble_button.pressed.connect(self.copyScramble) 
    self.reset_scramble_button.pressed.connect(self.renderScramble)

    # Scramble variables
    self.scramble_locked = False

    self.renderScramble()
  
  def editScramble(self):
    pass

  def renderScramble(self):
    if not self.scramble_locked:
      self.scramble_display.setText(generateScramble())

  def lockScramble(self):
    if self.scramble_locked:
      self.scramble_locked = False
      self.lock_scramble_button.setStyleSheet("""
                                              background-color: rgb(31, 31, 40);
                                              color: rgb(243, 243, 243);
                                              font: 125 15pt "Gill Sans MT";
                                              outline: none;
                                              border: none;
                                              border-radius: 5px;
                                              padding: 3px;
                                              """)
    else:
      self.scramble_locked = True
      self.lock_scramble_button.setStyleSheet("""
                                              background-color: rgb(61, 61, 70);
                                              color: rgb(243, 243, 243);
                                              font: 125 15pt "Gill Sans MT";
                                              outline: none;
                                              border: none;
                                              border-radius: 5px;
                                              padding: 3px;
                                              """)
  
  def copyScramble(self):
    clipboard = QApplication.clipboard()
    scramble = self.scramble_display.text()

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
    
