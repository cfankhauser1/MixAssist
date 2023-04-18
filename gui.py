# TODO: GUI options: instrument group colors, notify info

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mix Assist")

        layout = QVBoxLayout()
        directory_path = QLineEdit()
        program_path = QLineEdit()
        daw_select = QComboBox()
        daw_select.addItems(["ProTools", "Logic", "Ableton", "LUNA", "StudioOne"])
        widgets = [
            daw_select,
            directory_path,
            program_path
        ]
        for w in widgets:
            layout.addWidget(w)
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()