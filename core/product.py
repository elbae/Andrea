class Product():
	"""A generic class for a product"""
	"""Specific product categories"""
	GROCERIES = 0
	FRUITS_AND_VEGETABLES = 1
	FISH = 2
	PASTA = 3
	BEVERAGE = 4
	HOME = 5
	OTHERS = 6

	def __init__(self,code,name,product_type,price):
		"""The init method"""
		self.code=code
		self.name=name
		self.product_type=product_type
		self.price=price

	def print_details(self,quantity):
		"""Prints the product details"""
		print("{0:5}|{1:30}|{2:21}|{3:7}|{4:4}".format(
			self.code,self.name,self.type_to_string(self.product_type),self.price,quantity))

	def type_to_string(self,input_type):
		"""Converts product type to string"""
		if(input_type == 0):
			return("GROCERIES")
		elif(input_type == 1):
			return("FRUITS_AND_VEGETABLES")
		elif(input_type == 2):
			return("FISH")
		elif(input_type == 3):
			return("PASTA")
		elif(input_type == 4):
			return("BEVERAGE")
		elif(input_type == 5):
			return("HOME")
		elif(input_type == 6):
			return("OTHERS")
		else:
			return("UNKNOWN")



	
	
	
	
	
	
	