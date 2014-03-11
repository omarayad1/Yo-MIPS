from instructions import *
from parser import *
from GUI import *


binary_file = ''
app = QtGui.QApplication(sys.argv)
ex = main_window()
sys.exit(app.exec_())
machine_code = binary_file
parser_instance = parser()

batee5 = parser_instance.parse_instruction(parser_instance.get_32_bits(machine_code))
instruction_instance = batee5[4194304][0]
print instruction_instance
print instruction_instance.excute()
