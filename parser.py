import struct
from instructions import *
from text import *
from registers import *

class parser:
	text_segment_instance = text_segment()
	registers_instance = register()
	def get_32_bits(self, machine_code_file):
		self.machine_code_word = machine_code_file.read(4)
		self.machine_code_word = struct.pack('<i', int(self.machine_code_word.encode('hex'), 16))
		self.machine_code_word = self.machine_code_word.encode('hex')
		return int(self.machine_code_word, 16)
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
		self.text_segment_instance.append_instruction(instruction.instruction_op_index[self.opcode_2], self.registers_instance.register_index[self.get_rs(machine_code_word)], self.registers_instance.register_index[self.get_rt(machine_code_word)], self.get_immediate(machine_code_word))
		return self.text_segment_instance.globl_main