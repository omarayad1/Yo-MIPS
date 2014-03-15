"""
MAL segment Module

- stores instructions with equivalent pseudo instructions 
"""
class MAL:
	def __init__(self):
		self.MAL_segment = {}
		self.MAL_pc = 0x03FFFFC + 4
	def move(self, address):
		original_instruction = self.MAL_segment[address]
		original_instruction.pop(1)
		original_instruction[0] = "move"
		self.MAL_segment[address] = original_instruction
	def li(self, address):
		original_instruction = self.MAL_segment[address]
		original_instruction.pop(1)
		original_instruction[0] = "li"
		self.MAL_segment[address] = original_instruction
	def la(self, address):
		original_instruction = self.MAL_segment[address]
		original_instruction.pop(1)
		original_instruction[1] = self.MAL_segment[address+4][2]
		original_instruction[2] = (original_instruction[2] << 16) | self.MAL_segment[address+4][3]
		original_instruction[0] = "la"
		self.MAL_segment[address] = original_instruction
		self.MAL_segment[address+4][0] = None
	def subi(self, address):
		original_instruction = self.MAL_segment[address]
		original_instruction[0] = "subi"
		original_instruction[3] = 0 - original_instruction[3]
	def replace_all(self):
		self.MAL_pc = 0x03FFFFC + 4
		MAL_pc_max = max(self.MAL_segment.keys())
		while self.MAL_pc <= MAL_pc_max:
			try:
				if (self.MAL_segment[self.MAL_pc][0].name == "add") & \
				((self.MAL_segment[self.MAL_pc][1].name == "$zero")\
				 | (self.MAL_segment[self.MAL_pc][2].name == "$zero")):
					self.move(self.MAL_pc)
				elif (self.MAL_segment[self.MAL_pc][0].name == "addiu") & \
				(self.MAL_segment[self.MAL_pc][1].name == "$zero"):
					self.li(self.MAL_pc)
				elif (self.MAL_segment[self.MAL_pc][0].name == "lui") & \
				(self.MAL_segment[self.MAL_pc + 4][0].name == "ori"):
					self.la(self.MAL_pc)
				elif (self.MAL_segment[self.MAL_pc][0].name == "addi") & \
				(self.MAL_segment[self.MAL_pc][3] < 0):
					self.subi(self.MAL_pc)
				else:
					pass
			except AttributeError:
				pass
			except KeyError:
				pass
			self.MAL_pc += 4
#move, li, la, subi
MAL_segment_instance = MAL()