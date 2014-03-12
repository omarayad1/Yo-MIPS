class data_segment:
	def __init__(self):
		self.current_address = 0x1000fffc
		self.data = {}
	def append_data(self, machine_code_word):
		self.data.update({self.current_address+4 : [machine_code_word >> 24, (machine_code_word >> 16)&0x00ff, (machine_code_word >> 8)&0x0000ff, machine_code_word&0x000000ff]})
		self.current_address += 4
		return self.data
data_segment_instance = data_segment()