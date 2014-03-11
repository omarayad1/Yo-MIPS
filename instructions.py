from registers import register_index
from text import text_segment_instance

class instruction:
	def __init__(self):
		self.type = 'I'
		self.opcode = 0
		self.funct = 0
	def excute(self):
		pass
class lui(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xf
	def __new__(self):
		__class__ = lui
		__name__ = lui
	def excute(self):
		text_segment_instance.globl_main[text_segment_instance.pc][2].value = text_segment_instance.globl_main[text_segment_instance.pc][3] << 16
		return text_segment_instance.globl_main[text_segment_instance.pc][2].value
class instruction_index:
	def __init__(self):
		self.instruction_op_index = {0xf : lui()}
instruction_instance = instruction_index()