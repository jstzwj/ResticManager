from PySide2 import QtCore, QtWidgets, QtGui
from element.LineEdit import LineEdit
from element.PushButton import DefaultPushButton

class FileEdit(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = LineEdit("")
        self.button = DefaultPushButton("Browse")
        self.button.clicked.connect(self.browse)
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.layout.setMargin(0)
        self.setLayout(self.layout)


    def browse(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, self.tr("Find Files"), QtCore.QDir.currentPath())

        if directory != '':
            self.label.setText(directory)
            self.label.setSelection(0, 0)
