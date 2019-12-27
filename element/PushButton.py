

from PySide2 import QtCore, QtWidgets, QtGui

from element.ElementStyles import styles

class DefaultPushButton(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(styles['DefaultPushButton'])


class PrimaryPushButton(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(styles['PrimaryPushButton'])


class InfoPushButton(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(styles['InfoPushButton'])