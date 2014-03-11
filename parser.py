import struct
import copy
from instructions import instruction_instance
from text import text_segment_instance
from registers import register_index
from data import data_segment_instance
from registers import registers_instance

class parser:
	def get_32_bits(self, machine_code_file):
		self.machine_code_word = machine_code_file.read(4)
		try:
			self.machine_code_word = struct.pack('<I', int(self.machine_code_word.encode('hex'), 16))
			self.machine_code_word = self.machine_code_word.encode('hex')
			return int(self.machine_code_word, 16)
		except ValueError:
			return ''
	def get_instruction_type(self, machine_code_word):
		self.opcode = machine_code_word >> 26
		return self.opcode
	def get_rs(self, machine_code_word):
		self.rs = (machine_code_word >> 21) & 0x1f
		return self.rs
	def get_rt(self, machine_code_word):
		self.rt = (machine_code_word >> 16) & 0x1f
		return self.rt
	def get_rd(self, machine_code_word):
		self.rd = (machine_code_word >> 11) & 0x1f
		return self.rd
	def get_shamt(self, machine_code_word):
		self.shamt = (machine_code_word >> 6) & 0x1f
		return self.shamt
	def get_funct(self, machine_code_word):
		self.funct = (machine_code_word >> 0) & 0x3f
		return self.funct
	def get_immediate(self, machine_code_word):
		self.immediate = (machine_code_word >> 0) & 0xffff
		return self.immediate
	def get_address(self, machine_code_word):
		self.address = (machine_code_word >> 0) & 0x3ffffff
		return self.address
	def parse_instruction(self, machine_code_word):
		self.opcode_2 = self.get_instruction_type(machine_code_word)
		if self.opcode_2 == 0:
			try:
				text_segment_instance.append_instruction(instruction_instance.instruction_op_index[(self.opcode_2, self.get_funct(machine_code_word))], \
												registers_instance.register_index[self.get_rs(machine_code_word)], \
												registers_instance.register_index[self.get_rt(machine_code_word)], \
												registers_instance.register_index[self.get_rd(machine_code_word)], \
												registers_instance.register_index[self.get_shamt(machine_code_word)])
			except KeyError:
				pass
		elif (self.opcode_2 == 2) | (self.opcode_2 == 3):
			try:
				text_segment_instance.append_instruction(instruction_instance.instruction_op_index[self.opcode_2], \
												registers_instance.register_index[self.get_address(machine_code_word)])
			except KeyError:
				pass
		else:
			try:
				text_segment_instance.append_instruction(instruction_instance.instruction_op_index[self.opcode_2], \
												registers_instance.register_index[self.get_rs(machine_code_word)], \
												registers_instance.register_index[self.get_rt(machine_code_word)], \
												self.get_immediate(machine_code_word))
			except KeyError:
				pass
		return text_segment_instance.globl_main
	def parse_32_bit_data(self, machine_code_word):
		data_segment_instance.append_data(machine_code_word)
		return data_segment_instance.data
	def parse_all_instructions(self, machine_code_file):
		try:
			word = self.get_32_bits(machine_code_file)
			while word != '':
				self.parse_instruction(word)
				word = self.get_32_bits(machine_code_file)
		finally:
			machine_code_file.close()