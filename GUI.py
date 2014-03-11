import sys
from PySide import QtGui, QtCore
from instructions import *
from parser import *
from text import text_segment_instance

class instruction_box(QtGui.QTextEdit):
    def __init__(self, title, parent):
        super(instruction_box, self).__init__(title, parent)
        self.setAcceptDrops(True)
        self.setStyleSheet(u'min-height: 400px;background-color: #eee;padding-left: 20px;')
    def dragEnterEvent(self, e):
        self.setStyleSheet(u'background-color: #333; color: #eee')
        e.accept()
    def dropEvent(self, e):
        self.binary_file = e.mimeData().text()
        self.setStyleSheet(u'background-color: #eee')
        self.binary_file = self.binary_file.replace('\r\n', '')
        self.binary_file = self.binary_file.replace('file://', '')
        machine_code = open(self.binary_file,'rb')
        parser_instance = parser()
        batee5 = parser_instance.parse_all_instructions(machine_code)
        self.setText(text_segment_instance.print_instruction())
        print text_segment_instance.globl_main
    def dragLeaveEvent(self, e):
        self.setStyleSheet(u'background-color: #eee;')
class main_window(QtGui.QWidget):
    def __init__(self):
        super(main_window, self).__init__()
        self.initUI()
    def initUI(self):
        instruction_preview = instruction_box("Drag the binary output of the text segment here", self)
        instruction_preview.move(190, 65) 
        self.setGeometry(200, 100, 1000, 650)
        self.setStyleSheet(u'background-color: #333')
        self.setWindowTitle('Yo! MIPS')
        self.show()