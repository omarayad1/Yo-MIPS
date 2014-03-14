class symbol_table:
	def __init__(self):
		self.symbol_table = {}
		self.instruction_count = 0
	def insert_ref(self, address):
		self.symbol_table.update({address : "batee5_label" + self.instruction_count})
		self.instruction_count += 1
symbol_table_instance = symbol_table()