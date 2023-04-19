
#TODO:GUI options: notify info, save location(can I do this as a file exploerer?)
#TODO: set up prefrences window to set colors and track groups etc
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
    QPushButton,
    QFileDialog
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mix Assist")
        self.daw_list = ["ProTools", "Logic", "Ableton", "LUNA", "StudioOne"]
        self.layout = QGridLayout()
        self.directory = QPushButton("Choose Audio Directory:")
        self.directory.clicked.connect(self.find_audio_directory)
        self.project_name_label = QLabel("Enter project name:")
        self.project_name = QLineEdit()
        self.save_location = QPushButton("Choose Save Location")
        self.save_location.clicked.connect(self.find_save_location)
        self.file_dialog = QFileDialog
        self.daw_select = QComboBox()
        self.save_location_label = QLabel("")
        self.daw_select.addItems(self.daw_list)
        self.submit = QPushButton("Set It Up")
        self.submit.clicked.connect(self.store_info)
        widgets = [
            self.daw_select,
            self.project_name_label,
            self.project_name,
            self.directory,
            self.save_location,
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
            "directory_path": self.directory.text(),
            "project_name": self.project_name.text(),
            "save_location": self.save_location.text()
        }
        window.close()
        print(self.data)
        return self.data

    def find_save_location(self):
        fname = QFileDialog.getOpenFileName(self, "Choose Save Location", "")
        if fname:
            self.save_location.setText(fname[0])
    def find_audio_directory(self):
        fname = QFileDialog.getOpenFileName(self, "Choose Audio Directory", "")
        if fname:
            self.directory.setText(fname[0])



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()