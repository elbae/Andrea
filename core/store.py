from shelf import Shelf
from product import Product

class Store():
	"""A classic store with shelves"""
	product_code = 1

	def __init__(self):
		"""The init method"""
		self.shelves=[]
		self.shelves_id=0
		
	def create_shelf(self,shelf):
		"""Method used to add a shelf"""
		self.shelves.append(shelf)
		self.shelves_id+=1

	def insert_products(self,shelf_id,product,quantity):
		"""Insert a quantity number of product in the shelf shelf_id"""
		self.shelves[shelf_id].insert_products(product,quantity)

	def new_product_code(self):
		new_p_code = "{0:{fill}5}".format(self.product_code,fill=0)
		self.product_code+=1
		return(new_p_code)


	


