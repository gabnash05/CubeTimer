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
    self.input_dialog = self.inputScrambleDialog(self, self.scramble_display)

  def renderScramble(self):
    if not self.scramble_locked:
      self.scramble_display.setText(generateScramble())

  def lockScramble(self):
    if self.scramble_locked:
      self.scramble_locked = False
      self.lock_scramble_button.setStyleSheet("""
                                              QPushButton {
                                              background-color: rgb(31, 31, 40);
                                              color: rgb(243, 243, 243);
                                              font: 125 15pt "Gill Sans MT";
                                              outline: none;
                                              border: none;
                                              border-radius: 5px;
                                              padding: 3px;
                                              }
                                              """)
    else:
      self.scramble_locked = True
      self.lock_scramble_button.setStyleSheet("""
                                              QPushButton {
                                              background-color: rgb(61, 61, 70);
                                              color: rgb(243, 243, 243);
                                              font: 125 15pt "Gill Sans MT";
                                              outline: none;
                                              border: none;
                                              border-radius: 5px;
                                              padding: 3px;
                                              }
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
  
  def inputScrambleDialog(self, parent, scramble_display):
    dialog = QDialog(parent)
    dialog.setWindowTitle("Edit Scramble")
    dialog.setStyleSheet("""
                      QDialog {
                        background-color: rgb(31, 31, 40);
                        color: rgb(243, 243, 243);
                      }
                      """)

    # Create layout
    layout = QVBoxLayout(dialog)

    # Create and add line edit
    line_edit = QLineEdit(dialog)
    line_edit.setStyleSheet("""
                            QLineEdit {
                              background-color: rgb(21, 21, 30);
                              color: rgb(243, 243, 243);
                              padding: 5px;
                              border: none;
                              font: 14pt "Gill Sans MT";
                            }
                            """)
    line_edit.setMinimumWidth(700)
    line_edit.setMaximumWidth(900)
    line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # Adjust size policy
    line_edit.setText(scramble_display.text())
    layout.addWidget(line_edit)

    # Create button layout
    button_layout = QHBoxLayout()
    submit_button = QPushButton("Submit", dialog)
    submit_button.setStyleSheet("""
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
    submit_button.clicked.connect(dialog.accept)
    button_layout.addWidget(submit_button)

    # Add button layout to main layout
    layout.addLayout(button_layout)

    dialog.setFixedWidth(700)
    dialog.setFixedHeight(100)
    
    # Execute dialog and return the input text on accept
    if dialog.exec_() == QDialog.Accepted:
      input_text = line_edit.text()
      self.scramble_display.setText(input_text)
      return input_text
    else:
      return None