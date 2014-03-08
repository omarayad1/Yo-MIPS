class text_segment:
	def __init__(self):
		self.pc = 0x03FFFFC
		self.globl_main = []
	def append_instruction(self, instruction, rs_or_address, rt = None, rd_or_immediate = None, shamt = None):
		if (rt is None) & (rd_or_immediate is None) & (shamt is None):
			self.globl_main += [(self.pc+4, instruction, rs_or_address)]
			return self.globl_main
		elif shamt is None:
			self.globl_main += [(self.pc+4, instruction, rs_or_address, rt, rd_or_immediate)]
			return self.globl_main
		else:
			self.globl_main += [(self.pc+4, instruction, rs_or_address, rt, rd_or_immediate, shamt)]
			return self.globl_main