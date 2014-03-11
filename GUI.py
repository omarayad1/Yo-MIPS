import sys
from PySide import QtGui, QtCore

class instruction_box(QtGui.QLabel):
    def __init__(self, title, parent):
        super(instruction_box, self).__init__(title, parent)
        self.setAcceptDrops(True)
        self.setStyleSheet(u'min-height: 400px;background-color: #fff')
    def dragEnterEvent(self, e):
        self.setStyleSheet(u'background-color: #333')
        e.accept()
    def dropEvent(self, e):
        binary_file = e.mimeData().text()
        self.setStyleSheet(u'background-color: #fff')
    def dragLeaveEvent(self, e):
        self.setStyleSheet(u'background-color: #fff;')
class main_window(QtGui.QWidget):

    def __init__(self):
        super(main_window, self).__init__()
        self.initUI()

    def initUI(self):

        instruction_preview = instruction_box("Drag the binary output of the text segment here", self)
        instruction_preview.move(190, 65) 

        self.setGeometry(200, 100, 1000, 650)
        self.setWindowTitle('Yo MIPS')
        self.show()