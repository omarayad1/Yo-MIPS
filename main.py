from instructions import *
from parser import *

machine_code = open('s1.bin','rb')
parser = parser()
batee5 = bin(5)
print parser.parse_instruction(parser.get_32_bits(machine_code))
