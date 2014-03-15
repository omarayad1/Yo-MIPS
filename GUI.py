"""
GUI Module

- Do I really need to explain ?
"""
import sys
from PySide import QtGui, QtCore
from parser import parser_instance
from text import text_segment_instance
from data import data_segment_instance
from output import output_segment_instance, read_batee5_line_instance
from registers import registers_instance
from symbol_table import symbol_table_instance
import copy
class MAL_checkbox(QtGui.QCheckBox):
    def __init__(self, title, parent):
        super(MAL_checkbox, self).__init__(title, parent)
    def parse_MAL_or_TAL(self):
        print self.isChecked()
class register_box(QtGui.QTableWidget):
    def __init__(self, row, column, parent):
        super(register_box, self).__init__(row, column, parent)
        self.setAcceptDrops(False)
        self.setStyleSheet(u'background-color: #eee; max-height: 100px;')
        self.setHorizontalHeaderLabels(['$zero', '$at', '$v0', '$v1', '$a0', '$a1', '$a2', '$a3', '$t0', \
        '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7', '$s0', '$s1', '$s2', '$s3', '$s4', '$s5', '$s6', \
        '$s7', '$t8', '$t9', '$k0', '$k1', '$gp', '$sp', '$fp', '$ra'])
class simulate_button(QtGui.QPushButton):
    def __init__(self, title, parent):
        super(simulate_button, self).__init__(title, parent)
        self.setStyleSheet(u'background-color: #eee')
class console_box(QtGui.QPlainTextEdit):
    def __init__(self, title, parent):
        super(console_box, self).__init__(title, parent)
        self.setAcceptDrops(False)
        self.setStyleSheet(u'min-height: 100px;background-color: #eee')
        self.setReadOnly(True)
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
class instruction_box(QtGui.QPlainTextEdit):
    def __init__(self, title, parent):
        super(instruction_box, self).__init__(title, parent)
        self.setAcceptDrops(True)
        self.setStyleSheet(u'min-height: 400px;background-color: #eee')
        self.setReadOnly(True)
    def dragEnterEvent(self, e):
        self.setReadOnly(False)
        self.setStyleSheet(u'background-color: #333; color: #eee')
        e.accept()
    def dropEvent(self, e):
        self.binary_file = e.mimeData().text()
        self.setStyleSheet(u'background-color: #eee')
        self.binary_file = self.binary_file.replace('\r\n', '')
        self.binary_file = self.binary_file.replace('file://', '') #this only works on *nix systems doesn't work on windows
        machine_code = open(self.binary_file,'rb')
        batee5 = parser_instance.parse_all_instructions(machine_code)
        self.setPlainText(symbol_table_instance.print_MAL_instruction())
        self.setReadOnly(True)
    def dragLeaveEvent(self, e):
        self.setStyleSheet(u'background-color: #eee;')
class main_window(QtGui.QWidget):
    def __init__(self):
        super(main_window, self).__init__()
        self.initUI()
    def instruction_execute_all(self):
        text_segment_instance.execute_all_instructions()
        max_address = output_segment_instance.current_line
        current_line = 0
        while current_line < max_address:
            self.console_preview.appendPlainText(output_segment_instance.output[current_line])
            current_line += 1
        for i in xrange(32):
            item_teneen_2 = QtGui.QTableWidgetItem(str(registers_instance.register_index[i].value))
            self.registers_preview.setItem(0, i, item_teneen_2)
    def initUI(self):
        instruction_preview = instruction_box("Drag the binary output of the text segment here", self)
        instruction_preview.move(190, 65)
        data_preview = data_box(1024, 4, self)
        data_preview.move(600, 65)
        self.registers_preview = register_box(1, 32, self)
        self.registers_preview.move(200, 500)
        self.console_preview = console_box("Press simulate to begin program emulation", self)
        self.console_preview.move(600, 280)
        simulate_preview = simulate_button("simulate", self)
        simulate_preview.move(600,600)
        simulate_preview.clicked.connect(self.instruction_execute_all)
        self.MAL_checkbox_preview = MAL_checkbox("MAL", self)
        self.MAL_checkbox_preview.move(450,100)
        self.setGeometry(200, 100, 1000, 650)
        self.setStyleSheet(u'background-color: #333')
        self.setWindowTitle('Yo! MIPS')
        self.show()