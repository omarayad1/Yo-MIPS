"""
Instructions Module

- stores instruction classes with their properties & executions

- Handles SYSCALL instruction
"""
from registers import registers_instance
from text import text_segment_instance
from data import data_segment_instance
from output import output_segment_instance
import copy

class instruction:
	def __init__(self):
		self.opcode = 0
		self.funct = 0
		self.name = 'Unkown Instruction'
		self.load_store = False
		self.shift = False
	def execute(self):
		pass
class lui(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xf
		self.name = 'lui'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][3] << 16
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class ori(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xd
		self.name = 'ori'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value | \
		text_segment_instance.globl_main[text_segment_instance.pc][3]
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class addi(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x8
		self.name = 'addi'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value + \
		text_segment_instance.globl_main[text_segment_instance.pc][3]
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class add(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x20
		self.name = 'add'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value + \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class sub(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0
		self.funct = 0x22
		self.name = 'sub'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value - \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class addiu(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x9
		self.name = 'addiu'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value + \
		text_segment_instance.globl_main[text_segment_instance.pc][3]
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class lw(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x23
		self.name = 'lw'
		self.load_store = True
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = \
		data_segment_instance.load_word(text_segment_instance.globl_main[text_segment_instance.pc][1].value, \
		text_segment_instance.globl_main[text_segment_instance.pc][3])
class bne(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x5
		self.name = 'bne'
	def execute(self):
		if text_segment_instance.globl_main[text_segment_instance.pc][2].value != \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value:
			text_segment_instance.pc += (text_segment_instance.globl_main[text_segment_instance.pc][3] * 4)
		else: pass
class beq(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x4
		self.name = 'beq'
	def execute(self):
		if text_segment_instance.globl_main[text_segment_instance.pc][2].value == \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value:
			text_segment_instance.pc += (text_segment_instance.globl_main[text_segment_instance.pc][3] * 4)
		else: pass
class and_(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0
		self.funct = 0x24
		self.name = 'and'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value & \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class andi(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xc
		self.name = 'andi'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value & \
		text_segment_instance.globl_main[text_segment_instance.pc][3]
class syscall(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0xc
		self.name = 'syscall'
	def execute(self):
		if registers_instance.register_index[2].value == 10:
			output_segment_instance.append_output("Program has finished execution")
		elif registers_instance.register_index[2].value == 1:
			output_segment_instance.append_output(str(registers_instance.register_index[4].value))
		elif registers_instance.register_index[2].value == 4:
			string_address = registers_instance.register_index[4].value
			string_asciiz = ''
			char_batee5 = 'A'
			offset = 1
			while ord(char_batee5) != 0:
				char_batee5 = chr(data_segment_instance.load_byte(string_address, offset))
				string_asciiz += char_batee5
				offset += 1
			output_segment_instance.append_output(string_asciiz)
		else:
			pass
class slti(instruction):
        def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xa
		self.name = 'slti'
	def execute(self):
		if text_segment_instance.globl_main[text_segment_instance.pc][1].value < \
		text_segment_instance.globl_main[text_segment_instance.pc][3].value:
			text_segment_instance.globl_main[text_segment_instance.pc][2].value = 1
		else:
			text_segment_instance.globl_main[text_segment_instance.pc][2].value = 0
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value              
class or_(instruction):
        def __init__(self):
		instruction.__init__(self)
		self.opcode = 0
		self.funct = 0x25
		self.name = 'or'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value | \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class slt(instruction):
        def __init__(self):
		instruction.__init__(self)
		self.opcode = 0
		self.funct = 0x2a
		self.name = 'slt'
	def execute(self):
		if text_segment_instance.globl_main[text_segment_instance.pc][1].value < \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value:
			text_segment_instance.globl_main[text_segment_instance.pc][3].value = 1
		else:
			text_segment_instance.globl_main[text_segment_instance.pc][3].value = 0
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class subu(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x23
		self.name = 'subu'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value - \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class addu(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x21
		self.name = 'addu'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value + \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class xor(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x26
		self.name = 'add'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value ^ \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class sll(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x00
		self.name = 'sll'
		self.shift = True
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value << \
		text_segment_instance.globl_main[text_segment_instance.pc][4]
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class srl(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x02
		self.name = 'srl'
		self.shift = True
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value >> \
		text_segment_instance.globl_main[text_segment_instance.pc][4]
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class xori(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xe
		self.name = 'xori'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = \
		text_segment_instance.globl_main[text_segment_instance.pc][1].value ^ \
		text_segment_instance.globl_main[text_segment_instance.pc][3]
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class j(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x2
		self.name = 'j'
	def execute(self):
		text_segment_instance.pc = text_segment_instance.globl_main[text_segment_instance.pc][1] << 2
		text_segment_instance.pc -= 4
class jal(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x3
		self.name = 'jal'
	def execute(self):
		registers_instance.register_index[31].value = text_segment_instance.pc + 4
		text_segment_instance.pc = text_segment_instance.globl_main[text_segment_instance.pc][1] << 2
		text_segment_instance.pc -= 4
class jr(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x8
		self.name = 'jr'
	def execute(self):
		text_segment_instance.pc = (read_batee5_line_instance.register_index[31].value) - 4
class instruction_index:
	def __init__(self):
		self.instruction_op_index = {0xf : lui(), 0xd : ori(), 0x8 : addi(), 0x9  : addiu(), (0x0, 0x20) : add()\
		, 0x23 : lw(), 0x5 : bne(), (0x0, 0xc) : syscall(), (0x0, 0x22) : sub()\
		, (0x0,0x24) : and_(), 0xa : slti(), (0x0, 0x25) : or_(), (0x0, 0x2a) : slt(), (0x0, 0x23) : subu()\
		, (0x0, 0x21) : addu(), (0x0, 0x26) : xor(), (0x0, 0x0) : sll(), (0x0, 0x02) : srl()\
		, 0xe  : xori(), 0xc  : addi(), 0x4 : beq(), 0x2 : j(), 0x3 : jal(), 0xc : andi(), (0x0, 0x8) : jr()}
instruction_instance = instruction_index()
