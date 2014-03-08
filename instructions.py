class instruction:
	def __init__(self):
		self.type = 'I'
		self.opcode = 0
		self.immedite = 0
		self.source = 0
		self.target = 0
		self.destination = 0
		self.address = 0
		self.shamt = 0
	def excute(self):
		pass
class lui(instruction):
	def __init__(self):
		instruction.__init__(self)
		self.opcode = 0xf
	def __new__(self):
		__class__ = lui
		__name__ = lui
	def excute(self):
		self.target.value = self.immediate << 16
		return self.target.value
class add(instruction):
	def __init__(self):
		self.type = 'I'
		self.opcode = 0
		self.immedite = 0
		self.source = 0
		self.target = self.immedite + self.source
	def __new__(self):
		__class__ = add
		__name__ = add

instruction.instruction_op_index = {0xf : lui()}