from registers import register_index
from text import text_segment_instance

class instruction:
	def __init__(self):
		self.opcode = 0
		self.funct = 0
		self.name = 'Unkown Instruction'
		self.load_store = False
	def execute(self):
		pass
class lui(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xf
		self.name = 'lui'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = text_segment_instance.globl_main[text_segment_instance.pc][3] << 16
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class ori(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xd
		self.name = 'ori'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value | \
		text_segment_instance.globl_main[text_segment_instance.pc][3]
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class addi(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x8
		self.name = 'addi'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value + \
		text_segment_instance.globl_main[text_segment_instance.pc][3]
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class add(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x20
		self.name = 'add'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value + \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class sub(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0
		self.funct = 0x22
		self.name = 'sub'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value - \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class addiu(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x9
		self.name = 'addiu'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value + \
		text_segment_instance.globl_main[text_segment_instance.pc][3]
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class lw(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x23
		self.name = 'lw'
		self.load_store = True
	def execute(self):
		pass
class bne(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x5
		self.name = 'bne'
	def execute(self):
		pass
class and_(instruction):
        def __init__(self):
		instruction.__init__(self)
		self.opcode = 0
		self.funct = 0x24
		self.name = 'and'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value & \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class slti(instruction):
        def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xa
		self.name = 'slti'
	def execute(self):
		 if text_segment_instance.globl_main[text_segment_instance.pc][1].value < text_segment_instance.globl_main[text_segment_instance.pc][3].value:
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
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value | \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class slt(instruction):
        def __init__(self):
		instruction.__init__(self)
		self.opcode = 0
		self.funct = 0x2a
		self.name = 'slt'
	def execute(self):
                if text_segment_instance.globl_main[text_segment_instance.pc][1].value < text_segment_instance.globl_main[text_segment_instance.pc][2].value:
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
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value - \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class addu(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x21
		self.name = 'addu'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value + \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class xor(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x26
		self.name = 'add'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value ^ \
		text_segment_instance.globl_main[text_segment_instance.pc][2].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class sll(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x00
		self.name = 'sll'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = text_segment_instance.globl_main[text_segment_instance.pc][2].value << \
		text_segment_instance.globl_main[text_segment_instance.pc][4].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class srl(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0x02
		self.name = 'srl'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][3].value = text_segment_instance.globl_main[text_segment_instance.pc][2].value >> \
		text_segment_instance.globl_main[text_segment_instance.pc][4].value
		return text_segment_instance.globl_main[text_segment_instance.pc][3].value
class xori(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xe
		self.name = 'xori'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value ^ \
		text_segment_instance.globl_main[text_segment_instance.pc][3]
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value	
class addi(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xc
		self.name = 'addi'
	def execute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = text_segment_instance.globl_main[text_segment_instance.pc][1].value & \
		text_segment_instance.globl_main[text_segment_instance.pc][3]
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class beq(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x4
		self.name = 'beq'
	def execute(self):
		pass
class syscall(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0x0
		self.funct = 0xc
		self.name = 'syscall'
	def execute(self):
		pass
class instruction_index:
	def __init__(self):
		self.instruction_op_index = {0xf : lui(), 0xd : ori(), 0x8 : addi(), (0x0, 0x20) : add(), 0x9  : addiu(), 0x23 : lw(), 0x5 : bne(), (0x0, 0xc) : syscall(), (0x0, 0x22) : sub(), (0x0,0x24):and_(), 0xa: slti(), (0x0, 0x25) : or_(), (0x0, 0x2a) : slt(), (0x0, 0x23) : subu(), (0x0, 0x21) : addu(), (0x0, 0x26) : xor(), (0x0, 0x00) : sll(), (0x0, 0x02) : srl(), 0xe  : xori(), 0xc  : addi(), 0x4 : beq()}
instruction_instance = instruction_index()
