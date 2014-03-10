from instructions import *
from parser import *

machine_code = open('s1.bin','rb')
parser_instance = parser()

batee5 = parser_instance.parse_instruction(parser_instance.get_32_bits(machine_code))
instruction_instance = batee5[4194304][0]
print instruction_instance
print instruction_instance.excute()