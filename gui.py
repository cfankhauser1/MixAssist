# TODO: GUI options: instrument group colors, notify info

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QPushButton
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mix Assist")
        self.daw_list = ["ProTools", "Logic", "Ableton", "LUNA", "StudioOne"]
        self.layout = QGridLayout()
        self.directory_path = QLineEdit()
        self.program_path = QLineEdit()
        self.daw_select = QComboBox()
        self.daw_select.addItems(self.daw_list)
        self.submit = QPushButton("Set It Up")
        self.submit.clicked.connect(self.store_info)
        widgets = [
            self.daw_select,
            self.directory_path,
            self.program_path,
            self.submit
        ]
        for w in widgets:
            self.layout.addWidget(w)
        widget = QWidget()
        widget.setLayout(self.layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def store_info(self):
        self.data = {
            "selected_daw": self.daw_select.currentText(),
            "directory_path": self.directory_path.text()
        }
        print(self.data)
        return self.data




app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()