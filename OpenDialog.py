from PySide2 import QtCore, QtWidgets, QtGui

from FileEdit import FileEdit
from element.ElementStyles import styles
from element.PushButton import PrimaryPushButton
from element.LineEdit import LineEdit
from element.Label import Label

class OpenDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Open a repository')
        
        self.text = Label("Open a repository")
        self.repo_position = FileEdit()
        self.password = LineEdit()
        # self.password.setEnabled(False)
        self.button = PrimaryPushButton("open")

        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.repo_position)
        self.layout.addWidget(self.password)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.resize(400,140)
