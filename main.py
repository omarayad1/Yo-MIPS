from instructions import *
from parser import *

machine_code = open('s1_data.bin','rb')
parser_instance = parser()

print parser_instance.parse_32_bit_data(parser_instance.get_32_bits(machine_code))
