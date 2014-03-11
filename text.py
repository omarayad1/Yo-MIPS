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
	def execute_instructions(self):
		self.globl_main[self.pc][0].execute()
		return self.pc
	def print_instruction(self):
		instruction_string = ''
		self.pc = 0x03FFFFC + 4
		max_address = max(self.globl_main.keys())
		while self.pc <= max_address:
			opcode = self.globl_main[self.pc][0].opcode
			if opcode == 0:
				instruction_string += hex(self.pc) + ": " \
				+ self.globl_main[self.pc][0].name + " " \
				+ self.globl_main[self.pc][3].name + ", " \
				+ self.globl_main[self.pc][1].name + ", " \
				+ self.globl_main[self.pc][2].name + "\n"
			elif (opcode == 2) | (opcode == 3):
				pass
			elif self.globl_main[self.pc][0].load_store is True:
				instruction_string += hex(self.pc) + ": " \
				+ self.globl_main[self.pc][0].name + " " \
				+ self.globl_main[self.pc][2].name + ", " \
				+ str(self.globl_main[self.pc][3]) + "(" \
				+ self.globl_main[self.pc][1].name + ")\n"
			else:
				instruction_string += hex(self.pc) + ": " \
				+ self.globl_main[self.pc][0].name + " " \
				+ self.globl_main[self.pc][1].name + ", " \
				+ self.globl_main[self.pc][2].name + ", " \
				+ str(self.globl_main[self.pc][3]) + "\n"
			self.pc += 4
		self.pc = 0x03FFFFC #resets the program counter
		return instruction_string
text_segment_instance = text_segment()