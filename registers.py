"""
Registers Module

- Stores registers and their properties
"""
class register:
	def __init__(self):
		self.number = 0
		self.value = 0
		self.modifiable = True
		self.name = '$'
class zero(register):
	def __init__(self):
		register.__init__(self)
		self.modifiable = False
		self.name += 'zero'
class at(register):
	def __init__(self):
		register.__init__(self)
		self.number = 1
		self.name += 'at'
class v0(register):
	def __init__(self):
		register.__init__(self)
		self.number = 2
		self.name += 'v0'
class v1(register):
	def __init__(self):
		register.__init__(self)
		self.number = 3
		self.name += 'v1'
class a0(register):
	def __init__(self):
		register.__init__(self)
		self.number = 4
		self.name += 'a0'
class a1(register):
	def __init__(self):
		register.__init__(self)
		self.number = 5
		self.name += 'a1'
class a2(register):
	def __init__(self):
		register.__init__(self)
		self.number = 6
		self.name += 'a2'
class a3(register):
	def __init__(self):
		register.__init__(self)
		self.number = 7
		self.name += 'a3'
class t0(register):
	def __init__(self):
		register.__init__(self)
		self.number = 8
		self.name += 't0'
class t1(register):
	def __init__(self):
		register.__init__(self)
		self.number = 9
		self.name += 't1'
class t2(register):
	def __init__(self):
		register.__init__(self)
		self.number = 10
		self.name += 't2'
class t3(register):
	def __init__(self):
		register.__init__(self)
		self.number = 11
		self.name += 't3'
class t4(register):
	def __init__(self):
		register.__init__(self)
		self.number = 12
		self.name += 't4'
class t5(register):
	def __init__(self):
		register.__init__(self)
		self.number = 13
		self.name += 't5'
class t6(register):
	def __init__(self):
		register.__init__(self)
		self.number = 14
		self.name += 't6'
class t7(register):
	def __init__(self):
		register.__init__(self)
		self.number = 15
		self.name += 't7'
class s0(register):
	def __init__(self):
		register.__init__(self)
		self.number = 16
		self.name += 's0'
class s1(register):
	def __init__(self):
		register.__init__(self)
		self.number = 17
		self.name += 's1'
class s2(register):
	def __init__(self):
		register.__init__(self)
		self.number = 18
		self.name += 's2'
class s3(register):
	def __init__(self):
		register.__init__(self)
		self.number = 19
		self.name += 's3'
class s4(register):
	def __init__(self):
		register.__init__(self)
		self.number = 20
		self.name += 's4'
class s5(register):
	def __init__(self):
		register.__init__(self)
		self.number = 21
		self.name += 's5'
class s6(register):
	def __init__(self):
		register.__init__(self)
		self.number = 22
		self.name += 's6'
class s7(register):
	def __init__(self):
		register.__init__(self)
		self.number = 23
		self.name += 's7'
class t8(register):
	def __init__(self):
		register.__init__(self)
		self.number = 24
		self.name += 't8'
class t9(register):
	def __init__(self):
		register.__init__(self)
		self.number = 25
		self.name += 't9'
class k0(register):
	def __init__(self):
		register.__init__(self)
		self.number = 26
		self.modifiable = False
		self.name += 'k0'
class k1(register):
	def __init__(self):
		register.__init__(self)
		self.number = 27
		self.modifiable = False
		self.name += 'k1'
class gp(register):
	def __init__(self):
		register.__init__(self)
		self.number = 28
		self.name += 'gp'
class sp(register):
	def __init__(self):
		register.__init__(self)
		self.number = 29
		self.value = 0x7ffffffc
		self.name += 'sp'
class fp(register):
	def __init__(self):
		register.__init__(self)
		self.number = 30
		self.name += 'fp'
class ra(register):
	def __init__(self):
		register.__init__(self)
		self.number = 31
		self.modifiable = False
		self.name += 'ra'
class register_index:
	def __init__(self):
		self.register_index = {0 : zero(), 1 : at(), 2 : v0(), 3 : v1(), 4 : a0(), 5 : a1(), 6 : a2(), 7 : a3(), \
		8 : t0(), 9 : t1(), 10 : t2(), 11 : t3(), 12 : t4(), 13 : t5(), 14 : t6(), 15 : t7(), 16 : s0(), 17 : s1(), 18 : s2(), \
		19 : s3(), 20 : s4(), 21 : s5(), 22 : s6(), 23 : s7(), 24 : t8(), 25 : t9(), 26 : k0(), 27 : k1(), 28 : gp(), 29 : sp(), \
		30 : fp(), 31 : ra()}

registers_instance = register_index()