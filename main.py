from instructions import *
from parser import *
from GUI import *

app = QtGui.QApplication(sys.argv)
ex = main_window()
sys.exit(app.exec_())