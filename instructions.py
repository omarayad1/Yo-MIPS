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
		self.instruction_op_index = {0xf : lui(), 0xd : ori(), 0x8 : addi(), (0x0, 0x20) : add(), 0x9  : addiu(), \
		0x23 : lw(), 0x5 : bne(), (0x0, 0xc) : syscall(), (0x0, 0x22) : sub(), (0x0,0x24):and_()}
instruction_instance = instruction_index()
