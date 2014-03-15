from text import text_segment_instance
import copy

class MAL:
	def __init__(self):
		self.MAL_segment = copy.deepcopy(text_segment_instance.globl_main)
	def move(self, address):
		original_instruction = self.MAL_segment[address]
		original_instruction.remove(zero())
		original_instruction[0] = "move"
		self.MAL_segment[address] = original_instruction
	def li(self, address):
		original_instruction = self.MAL_segment[address]
		original_instruction.remove(zero())
		original_instruction[0] = "li"
		self.MAL_segment[address] = original_instruction
	def la(self, address):
		original_instruction = self.MAL_segment[address]
		original_instruction.remove(zero())
		original_instruction[1] = self.MAL_segment[address+4][1]
		original_instruction[2] = (original_instruction[3] << 16) | self.MAL_segment[address+4][3]
		original_instruction[0] = "la"
		self.MAL_segment[address] = original_instruction
		self.MAL_segment[address+4] = None
	def subi(self, address):
		original_instruction = self.MAL_segment[address]
		original_instruction[0] = "subi"
		original_instruction[3] = 0 - original_instruction[3]
	def replace_all(self):
		MAL_pc = 0x03FFFFC + 4
		MAL_pc_max = max(sel.MAL_segment.keys())
		while MAL_pc <= MAL_pc_max:
			if (self.MAL_segment[MAL_pc][0].name == "add") & \
			((self.MAL_segment[MAL_pc][1].name == "$zero")\
			 | (self.MAL_segment[MAL_pc][2].name == "$zero")):
				self.move(MAL_pc)
			elif (self.MAL_segment[MAL_pc][0].name == "addiu") & \
			(self.MAL_segment[MAL_pc][1].name == "$zero"):
				self.li(MAL_pc)
			elif (self.MAL_segment[MAL_pc][0].name == "lui") & \
			(self.MAL_segment[MAL_pc + 4][0].name == "ori"):
				self.la(MAL_pc)
			elif (self.MAL_segment[MAL_pc][0].name == "addi") & \
			(self.MAL_segment[MAL_pc][3] < 0):
				self.subi(MAL_pc)
			else:
				pass
#move, li, la, subi
MAL_segment_instance = MAL()