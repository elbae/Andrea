import shelf

class Store():
	"""A classic store with shelves"""

	def __init__(self):
		"""The init method"""
		self.shelves=[]
		
	def create_shelf(self):
		"""Method used to add a shelf"""
		new_shelf = shelf.Shelf()
		shelf.shelves.append(new_shelf)

	


