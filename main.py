from GUI import main_window
from PySide import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
ex = main_window()
sys.exit(app.exec_())