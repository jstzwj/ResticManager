
from PySide2 import QtCore, QtWidgets, QtGui

from element.ElementStyles import styles

class Label(QtWidgets.QLabel):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(styles['Label'])
