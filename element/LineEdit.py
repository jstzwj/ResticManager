
from PySide2 import QtCore, QtWidgets, QtGui

from element.ElementStyles import styles

class LineEdit(QtWidgets.QLineEdit):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(styles['LineEdit'])
