#!/usr/bin/python3
from product import Product

class Shelf():
	"""A generic class for a shelf"""


	def __init__(self,id,product_type,capacity):
		"""The init method"""
		self.id=id
		self.product_type=product_type
		self.capacity=capacity
		self.products={} # dict with shape (product,quantity)

	def get_products(self):
		"""Prints details of the products in the shelf"""
		for product,quantity in self.products.items():
			product.print_details(quantity)


	def insert_products(self,product,quantity):
		"""Insert a Product if there is enough space and the product_type corresponds"""
		if self.capacity < quantity:
			print("[Shelf {0}] not enough space for {1} | {2}, only {3} slot/s available/s".format(
				self.id,quantity,product.name,self.capacity))
		elif product.product_type != self.product_type:
			print("[Shelf {0}] with type {1}, mismatch with product {2} and type {3}".format(
				self.id,self.product_type,product.name, product.product_type))
		else:
			if product in self.products:
				self.products[product] += quantity
			else:
				self.products[product] = quantity





