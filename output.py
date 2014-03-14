class output_segment:
	def __init__(self):
		self.output = {}
		self.current_line = 0
	def append_output(self, output):
		self.output.update({self.current_line : output})
		self.current_line += 1
		return self.output
	def read_integer(self, char):
		self.output.update({self.current_line : read_batee5_line() })
class read_batee5_line:
	def __init__(self):
		pass
output_segment_instance = output_segment()
read_batee5_line_instance = read_batee5_line()