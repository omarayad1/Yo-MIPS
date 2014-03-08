class text_segment:
	def __init__(self):
		self.pc = 0x03FFFFC
		self.globl_main = []
	# def append_instruction(self, instruction, rs, rt, rd, shamt):
	# 	self.globl_main + [(self.pc+4, instruction, rs, rt, rd)]
	# 	return self.globl_main
	def append_instruction(self, instruction, rs, rt, immediate):
		self.globl_main += [(hex(self.pc+4), instruction, rs, rt, immediate)]
		return self.globl_main
	# def append_instruction(self, instruction, address):
	# 	self.globl_main + [(self.pc+4, instruction, address)]
	# 	return self.globl_main