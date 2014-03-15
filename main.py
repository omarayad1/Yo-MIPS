"""
I want to take this moment to thank god for 

Chopin, Chocolate and Python 2.7
"""
"""
#Yo! MIPS
##authors:

Omar H. Ayad 	900112630

Sherif Ismail 	900120050
"""

from GUI import main_window
from PySide import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
ex = main_window()
sys.exit(app.exec_())