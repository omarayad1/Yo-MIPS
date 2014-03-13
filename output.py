class output_segment:
	def __init__(self):
		self.output = {}
		self.current_line = 0
	def append_output(self, output):
		self.output.update({self.current_line : output})
		self.current_line += 1
		return self.output
output_segment_instance = output_segment()