class Person():
	"""A generic class for a person"""

	def __init__(self,name,surname,username,password):
		"""The init method"""
		self.name=name
		self.surname=surname
		self.username=username
		self.password=password

class Client(Person):
	"""A generic class for a client"""

	def __init__(self,name,surname,username,password):
		"""The init method"""
		super().__init__(name,surname,username,password)
		self.points=0.0

class Employed(Person):
	"""A generic class for an employed"""

	def __init__(self,name,surname,username,password):
		"""The init method"""
		super().__init__(name,surname,username,password)
		self.discount=5
		