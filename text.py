class text_segment:
	def __init__(self):
		self.pc = 0x03FFFFC
		self.globl_main = {}
	def append_instruction(self, instruction, rs_or_address, rt = None, rd_or_immediate = None, shamt = None):
		if (rt is None) & (rd_or_immediate is None) & (shamt is None):
			self.globl_main.update({self.pc+4 : [instruction, rs_or_address]})
			self.pc += 4
			return self.globl_main
		elif shamt is None:
			self.globl_main.update({self.pc+4 : [instruction, rs_or_address, rt, rd_or_immediate]})
			self.pc += 4
			return self.globl_main
		else:
			self.globl_main.update({self.pc+4 : [instruction, rs_or_address, rt, rd_or_immediate, shamt]})
			self.pc += 4
			return self.globl_main
	def excute_instruction(self):
		self.globl_main[self.pc][0].excute()
		return self.pc
	def print_instruction(self):
		instruction_string = hex(self.pc) + ": " \
		+ self.globl_main[self.pc][0].name + " " \
		+ self.globl_main[self.pc][2].name + ", " \
		+ self.globl_main[self.pc][1].name + ", " \
		+ str(self.globl_main[self.pc][3]) + "\n"
		return instruction_string
text_segment_instance = text_segment()