import sys
from PySide import QtGui, QtCore
from instructions import *
from parser import parser_instance
from text import text_segment_instance
from data import data_segment_instance
class simulate_button(QtGui.QPushButton):
    def __init__(self, title, parent):
        super(simulate_button, self).__init__(title, parent)
        self.setStyleSheet(u'background-color: #eee')
    def clicked(self):
        print "clicked"
class console_box(QtGui.QTextEdit):
    def __init__(self, title, parent):
        super(console_box, self).__init__(title, parent)
        self.setAcceptDrops(False)
        self.setStyleSheet(u'min-height: 100px;background-color: #eee')
class data_box(QtGui.QTableWidget):
    def __init__(self, row, column, parent):
        super(data_box, self).__init__(row, column, parent)
        self.setAcceptDrops(True)
        self.setHorizontalHeaderLabels(['Value (+0)', 'Value (+1)', 'Value (+2)', 'Value (+3)'])
        self.setStyleSheet(u'background-color: #eee;')
    def dragMoveEvent(self, e):
        e.accept
    def dragEnterEvent(self, e):
        self.setStyleSheet(u'background-color: #333')
        e.accept()
    def dropEvent(self, e):
        self.binary_file = e.mimeData().text()
        self.setStyleSheet(u'background-color: #eee')
        self.binary_file = self.binary_file.replace('\r\n', '')
        self.binary_file = self.binary_file.replace('file://', '')
        machine_code = open(self.binary_file,'rb')
        batee5 = parser_instance.parse_all_data(machine_code)
        sorted_address = sorted(data_segment_instance.data)
        sorted_address = map(hex,sorted_address)
        self.setVerticalHeaderLabels(sorted_address)
        for i in xrange(1024):
            for x in xrange(4):
                item_teneen = QtGui.QTableWidgetItem(str(data_segment_instance.data[int(sorted_address[i],16)][x]))
                self.setItem(i, x, item_teneen)
class instruction_box(QtGui.QTextEdit):
    def __init__(self, title, parent):
        super(instruction_box, self).__init__(title, parent)
        self.setAcceptDrops(True)
        self.setStyleSheet(u'min-height: 400px;background-color: #eee')
    def dragEnterEvent(self, e):
        self.setStyleSheet(u'background-color: #333; color: #eee')
        e.accept()
    def dropEvent(self, e):
        self.binary_file = e.mimeData().text()
        self.setStyleSheet(u'background-color: #eee')
        self.binary_file = self.binary_file.replace('\r\n', '')
        self.binary_file = self.binary_file.replace('file://', '')
        machine_code = open(self.binary_file,'rb')
        batee5 = parser_instance.parse_all_instructions(machine_code)
        self.setText(text_segment_instance.print_instruction())
    def dragLeaveEvent(self, e):
        self.setStyleSheet(u'background-color: #eee;')
class main_window(QtGui.QWidget):
    def __init__(self):
        super(main_window, self).__init__()
        self.initUI()
    def initUI(self):
        instruction_preview = instruction_box("Drag the binary output of the text segment here", self)
        instruction_preview.move(190, 65)
        data_preview = data_box(1024, 4, self)
        data_preview.move(600, 65)
        console_preview = console_box("Press simulate to begin program emulation", self)
        console_preview.move(600, 280)
        simulate_preview = simulate_button("simulate", self)
        simulate_preview.move(600,600)
        self.setGeometry(200, 100, 1000, 650)
        self.setStyleSheet(u'background-color: #333')
        self.setWindowTitle('Yo! MIPS')
        self.show()