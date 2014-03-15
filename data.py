"""
Data segment Module

- stores program data

- handles load instructions
"""
class data_segment:
	def __init__(self):
		self.current_address = 0x1000fffc
		self.data = {}
	def append_data(self, machine_code_word):
		self.data.update({self.current_address+4 : [machine_code_word >> 24, (machine_code_word >> 16)&0x00ff, (machine_code_word >> 8)&0x0000ff, machine_code_word&0x000000ff]})
		self.current_address += 4
		return self.data
	def load_word(self, address, offset):
		whole_address = address + offset
		word = (self.data[whole_address][0] << 24) + (self.data[whole_address][1] << 16) + (self.data[whole_address][2] << 8) + (self.data[whole_address][3])
		return word
	def load_half_word(self, address, offset):
		whole_address = address + offset
		half_word = (self.data[whole_address][0] << 8) + (self.data[whole_address][1])
		return half_word
	def load_byte(self, address, offset):
		whole_address = address + offset
		address_offset = whole_address % 4
		whole_address = whole_address - address_offset
		byte = (self.data[whole_address][address_offset])
		return byte
data_segment_instance = data_segment()