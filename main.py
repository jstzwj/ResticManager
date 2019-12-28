import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

from OpenDialog import OpenDialog

from element.ElementStyles import styles

app = None

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Restic Manager')

        self.setStyleSheet(styles['MainStyle'])


    def open_repo(self):
        self.dialog = OpenDialog(self)
        if self.dialog.exec_() == QtWidgets.QDialog.Accepted:
            pass
        else:
            pass

        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    main_window = MainWindow()
    main_window.resize(800, 600)
    main_window.show()
    main_window.open_repo()

    sys.exit(app.exec_())