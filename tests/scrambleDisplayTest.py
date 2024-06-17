from PyQt5.QtWidgets import *


def input_scramble_dialog(parent, scramble_display):
    dialog = QDialog(parent)
    dialog.setWindowTitle("Input Scramble")
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

    # Execute dialog and return the input text on accept
    if dialog.exec_() == QDialog.Accepted:
        input_text = line_edit.text()
        print("Input submitted:", input_text)
        return input_text
    else:
        return None


# Example usage:
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    label = QLabel("Initial Text")
    input_text = input_scramble_dialog(None, label)
    print("Returned input:", input_text)
    sys.exit(app.exec_())
