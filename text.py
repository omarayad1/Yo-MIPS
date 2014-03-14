
class text_segment:
	def __init__(self):
		self.pc = 0x03FFFFC
		self.globl_main = {}
		self.max_address = 0;
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
	def execute_instruction(self):
		self.globl_main[self.pc][0].execute()
		return self.pc
	def execute_all_instructions(self):
		self.pc = 0x03FFFFC + 4
		self.max_address = max(self.globl_main.keys())
		while self.pc <= self.max_address:
			self.execute_instruction()
			self.pc += 4
		self.pc = 0x03FFFFC + 4
text_segment_instance = text_segment()