"""
I want to take this moment to thank god for 

Chopin, Chocolate and Python 2.7
"""
"""
Knowledge is Power,

France is Bacon
"""
"""
# Yo! MIPS
## MIPS with SWAG
### authors:

Omar H. Ayad 	900112630

Sherif Ismail 	900120050
"""
"""
If you absolutly need to build the project from 
scratch you need Qt4.8 installed then install Python 2.7
then Pyside python Module (Don't use pip or easy_install use the binaries instead)

- Qt 4.8: http://qt-project.org/downloads
- Python 2.7: https://www.python.org/download/releases/2.7.5/
- Pyside: http://qt-project.org/wiki/Get-PySide
"""
from GUI import main_window
from PySide import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
ex = main_window()
sys.exit(app.exec_())