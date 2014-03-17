"""
Symbol Table Module

- Replaces Addresses in branch & Jump instructions with labels

- prints out instructions TAL or MAL
"""
from text import text_segment_instance
from MAL_segment import MAL_segment_instance
import copy

class symbol_table:
	def __init__(self):
		self.symbol_table = {}
		self.instruction_count = 0
	def insert_ref(self, address):
		self.symbol_table.update({address : "nasr_label_" + str(self.instruction_count)})
		self.instruction_count += 1
	def connect_labels(self):
		text_segment_instance.pc = 0x03FFFFC + 4 + 4
		text_segment_instance.max_address = max(text_segment_instance.globl_main.keys())
		while text_segment_instance.pc <= text_segment_instance.max_address:
			if (text_segment_instance.globl_main[text_segment_instance.pc][0].name == 'beq') \
			| (text_segment_instance.globl_main[text_segment_instance.pc][0].name == 'bne'):
				self.insert_ref(text_segment_instance.pc + \
				(text_segment_instance.globl_main[text_segment_instance.pc][3] * 4) + 4)
			elif (text_segment_instance.globl_main[text_segment_instance.pc][0].name == 'j') \
			| (text_segment_instance.globl_main[text_segment_instance.pc][0].name == 'jal'):
				self.insert_ref(text_segment_instance.globl_main[text_segment_instance.pc][1] << 2)
			else: pass
			text_segment_instance.pc += 4
		text_segment_instance.pc = 0x03FFFFC + 4
	def print_instruction(self):
		instruction_string = ''
		text_segment_instance.pc = 0x03FFFFC + 4 + 4
		text_segment_instance.max_address = max(text_segment_instance.globl_main.keys())
		self.connect_labels()
		while text_segment_instance.pc <= text_segment_instance.max_address:
			opcode = text_segment_instance.globl_main[text_segment_instance.pc][0].opcode
			funct = text_segment_instance.globl_main[text_segment_instance.pc][0].funct
			if (opcode == 0) & (funct == 0xc):
				try:
					instruction_string += self.symbol_table[text_segment_instance.pc] + ": " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][0].name +"\n"
				except KeyError:
					instruction_string += hex(text_segment_instance.pc) + ": " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][0].name +"\n"
			elif (opcode == 0) & (funct == 0x8):
				try:
					instruction_string += self.symbol_table[text_segment_instance.pc] + ": " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][0].name +" "\
					+ text_segment_instance.globl_main[text_segment_instance.pc][1].name + "\n"
				except KeyError:
					instruction_string += hex(text_segment_instance.pc) + ": " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][0].name +" "\
					+ text_segment_instance.globl_main[text_segment_instance.pc][1].name + "\n"
			elif opcode == 0:
				if text_segment_instance.globl_main[text_segment_instance.pc][0].shift is True:
					try:
						instruction_string += self.symbol_table[text_segment_instance.pc] + ": " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][3].name + ", " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][2].name + ", " \
						+ str(text_segment_instance.globl_main[text_segment_instance.pc][4]) + "\n"
					except KeyError:
						instruction_string += hex(text_segment_instance.pc) + ": " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][3].name + ", " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][2].name + ", " \
						+ str(text_segment_instance.globl_main[text_segment_instance.pc][4]) + "\n"
				else:
					try:
						instruction_string += self.symbol_table[text_segment_instance.pc] + ": " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][3].name + ", " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][1].name + ", " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][2].name + "\n"
					except KeyError:
						instruction_string += hex(text_segment_instance.pc) + ": " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][3].name + ", " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][1].name + ", " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][2].name + "\n"
			elif (opcode == 2) | (opcode == 3):
				try:
					instruction_string += self.symbol_table[text_segment_instance.pc] + ": " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
					+ self.symbol_table[text_segment_instance.globl_main[text_segment_instance.pc][1] << 2] + "\n"
				except KeyError:
					instruction_string += hex(text_segment_instance.pc) + ": " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
					+ self.symbol_table[text_segment_instance.globl_main[text_segment_instance.pc][1] << 2] + "\n"
			elif text_segment_instance.globl_main[text_segment_instance.pc][0].load_store is True:
				try:
					instruction_string += self.symbol_table[text_segment_instance.pc] + ": " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][2].name + ", " \
					+ str(text_segment_instance.globl_main[text_segment_instance.pc][3]) + "(" \
					+ text_segment_instance.globl_main[text_segment_instance.pc][1].name + ")\n"
				except KeyError:
					instruction_string += hex(text_segment_instance.pc) + ": " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][2].name + ", " \
					+ str(text_segment_instance.globl_main[text_segment_instance.pc][3]) + "(" \
					+ text_segment_instance.globl_main[text_segment_instance.pc][1].name + ")\n"
			else:
				if (opcode == 0x4) | (opcode == 0x5):
					try:
						get_address_as_a_symbol = self.symbol_table[text_segment_instance.pc]
					except KeyError:
						get_address_as_a_symbol = hex(text_segment_instance.pc)
					batee5_key = (text_segment_instance.globl_main[text_segment_instance.pc][3]*4) + text_segment_instance.pc + 4
					batee5_key = self.symbol_table[batee5_key]
					instruction_string += get_address_as_a_symbol + ": " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][1].name + ", " \
					+ text_segment_instance.globl_main[text_segment_instance.pc][2].name + ", " \
					+ batee5_key + "\n"
				else:
					try:
						instruction_string += self.symbol_table[text_segment_instance.pc] + ": " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][2].name + ", " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][1].name + ", " \
						+ str(text_segment_instance.globl_main[text_segment_instance.pc][3]) + "\n"
					except KeyError:
						instruction_string += hex(text_segment_instance.pc) + ": " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][0].name + " " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][2].name + ", " \
						+ text_segment_instance.globl_main[text_segment_instance.pc][1].name + ", " \
						+ str(text_segment_instance.globl_main[text_segment_instance.pc][3]) + "\n"
			text_segment_instance.pc += 4
		text_segment_instance.pc = 0x03FFFFC #resets the program counter
		return instruction_string
	def print_MAL_instruction(self):
		instruction_string = ''
		MAL_segment_instance.MAL_pc = 0x03FFFFC + 4
		max_address = max(text_segment_instance.globl_main.keys())
		self.connect_labels()
		MAL_segment_instance.MAL_segment = copy.deepcopy(text_segment_instance.globl_main)
		MAL_segment_instance.replace_all()
		MAL_segment_instance.MAL_pc = 0x03FFFFC + 4
		while MAL_segment_instance.MAL_pc <= max_address:
			if (isinstance(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0], str)):
				MAL_instruction = MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0]
				try:
					if MAL_instruction == 'move':
						instruction_string += self.symbol_table[MAL_segment_instance.MAL_pc] + ": "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0] + " "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + "\n"
					elif MAL_instruction == 'li':
						instruction_string += self.symbol_table[MAL_segment_instance.MAL_pc] + ": "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0] + " "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", "\
						+ str(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2]) + "\n"
					elif MAL_instruction == 'la':
						instruction_string += self.symbol_table[MAL_segment_instance.MAL_pc] + ": "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0] + " "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", "\
						+ hex(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2]) + "\n"
					elif MAL_instruction == 'subi':
						instruction_string += self.symbol_table[MAL_segment_instance.MAL_pc] + ": "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0] + " "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", "\
						+ str(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3]) + "\n"
					else:
						pass
				except KeyError:
					if MAL_instruction == 'move':
						instruction_string += hex(MAL_segment_instance.MAL_pc) + ": "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0] + " "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + "\n"
					elif MAL_instruction == 'li':
						instruction_string += hex(MAL_segment_instance.MAL_pc) + ": "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0] + " "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", "\
						+ str(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2]) + "\n"
					elif MAL_instruction == 'la':
						instruction_string += hex(MAL_segment_instance.MAL_pc) + ": "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0] + " "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", "\
						+ hex(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2]) + "\n"
					elif MAL_instruction == 'subi':
						instruction_string += hex(MAL_segment_instance.MAL_pc) + ": "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0] + " "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", "\
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", "\
						+ str(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3]) + "\n"
					else:
						pass
				MAL_segment_instance.MAL_pc += 4
			elif (MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0] is None):
				instruction_string += hex(MAL_segment_instance.MAL_pc) + ":\n"
				MAL_segment_instance.MAL_pc += 4
			else:
				opcode = MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].opcode
				funct = MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].funct
				if (opcode == 0) & (funct == 0xc):
					try:
						instruction_string += self.symbol_table[MAL_segment_instance.MAL_pc] + ": " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name +"\n"
					except KeyError:
						instruction_string += hex(MAL_segment_instance.MAL_pc) + ": " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name +"\n"
				elif opcode == 0:
					if MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].shift is True:
						try:
							instruction_string += self.symbol_table[MAL_segment_instance.MAL_pc] + ": " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3].name + ", " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", " \
							+ str(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][4]) + "\n"
						except KeyError:
							instruction_string += hex(MAL_segment_instance.MAL_pc) + ": " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3].name + ", " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", " \
							+ str(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][4]) + "\n"
					else:
						try:
							instruction_string += self.symbol_table[MAL_segment_instance.MAL_pc] + ": " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3].name + ", " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + "\n"
						except KeyError:
							instruction_string += hex(MAL_segment_instance.MAL_pc) + ": " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3].name + ", " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + "\n"
				elif (opcode == 2) | (opcode == 3):
					try:
						instruction_string += self.symbol_table[MAL_segment_instance.MAL_pc] + ": " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
						+ self.symbol_table[MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1] << 2] + "\n"
					except KeyError:
						instruction_string += hex(MAL_segment_instance.MAL_pc) + ": " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
						+ self.symbol_table[MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1] << 2] + "\n"
				elif MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].load_store is True:
					try:
						instruction_string += self.symbol_table[MAL_segment_instance.MAL_pc] + ": " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", " \
						+ str(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3]) + "(" \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ")\n"
					except KeyError:
						instruction_string += hex(MAL_segment_instance.MAL_pc) + ": " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", " \
						+ str(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3]) + "(" \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ")\n"
				else:
					if (opcode == 0x4) | (opcode == 0x5):
						try:
							get_address_as_a_symbol = self.symbol_table[MAL_segment_instance.MAL_pc]
						except KeyError:
							get_address_as_a_symbol = hex(MAL_segment_instance.MAL_pc)
						batee5_key = (MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3]*4) + MAL_segment_instance.MAL_pc + 4
						batee5_key = self.symbol_table[batee5_key]
						instruction_string += get_address_as_a_symbol + ": " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", " \
						+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", " \
						+ batee5_key + "\n"
					else:
						try:
							instruction_string += self.symbol_table[MAL_segment_instance.MAL_pc] + ": " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", " \
							+ str(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3]) + "\n"
						except KeyError:
							instruction_string += hex(MAL_segment_instance.MAL_pc) + ": " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][0].name + " " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][2].name + ", " \
							+ MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][1].name + ", " \
							+ str(MAL_segment_instance.MAL_segment[MAL_segment_instance.MAL_pc][3]) + "\n"
				MAL_segment_instance.MAL_pc += 4
		MAL_segment_instance.MAL_pc = 0x03FFFFC #resets the program counter
		return instruction_string
symbol_table_instance = symbol_table()