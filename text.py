class text_segment:
	def __init__(self):
		self.pc = 0x03FFFFC
		self.globl_main = {}
	def append_instruction(self, instruction, rs_or_address, rt = None, rd_or_immediate = None, shamt = None):
		if (rt is None) & (rd_or_immediate is None) & (shamt is None):
			self.globl_main.update({self.pc+4 : [instruction, rs_or_address]})
			self.pc += 4
			instruction.address = rs_or_address
			return self.globl_main
		elif shamt is None:
			self.globl_main.update({self.pc+4 : [instruction, rs_or_address, rt, rd_or_immediate]})
			self.pc += 4
			instruction.source = rs_or_address
			instruction.target = rt
			instruction.immediate = rd_or_immediate
			return self.globl_main
		else:
			self.globl_main.update({self.pc+4 : [instruction, rs_or_address, rt, rd_or_immediate, shamt]})
			self.pc += 4
			instruction.source = rs_or_address
			instruction.target = rt
			instruction.destination = rd_or_immediate
			instruction.shamt = shamt
			return self.globl_main
	def excute_instruction(self):
		self.globl_main[self.pc][0].excute()
		self.pc += 4
		return self.pc
text_segment_instance = text_segment()