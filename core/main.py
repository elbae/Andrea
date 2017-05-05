#!/usr/bin/python3

from shelf import Shelf
from store import Store
from person import Employed,Client
from product import Product

def main():
	#creating the global store
	the_store = Store()
	print("Store created")
	#creating some people
	persons = []
	persons.append(Employed("Andrea","Baesso","admin","admin"))
	persons.append(Employed("Admino","Nimda","admino","admino"))
	persons.append(Client("Tizio","Uno","tizio1","tizio1"))
	persons.append(Client("Tizio","Due","tizio2","tizio2"))
	#creating some shelves
	the_store.create_shelf(Shelf(the_store.shelves_id,Product.GROCERIES,50))
	the_store.create_shelf(Shelf(the_store.shelves_id,Product.FRUITS_AND_VEGETABLES,50))
	the_store.create_shelf(Shelf(the_store.shelves_id,Product.FISH,10))
	the_store.create_shelf(Shelf(the_store.shelves_id,Product.PASTA,100))
	the_store.create_shelf(Shelf(the_store.shelves_id,Product.BEVERAGE,200))
	the_store.create_shelf(Shelf(the_store.shelves_id,Product.HOME,50))
	the_store.create_shelf(Shelf(the_store.shelves_id,Product.OTHERS,50))
	#creating some products for each shelf
	the_store.insert_products(0,Product(the_store.new_product_code(),
		"Bread type 0",Product.GROCERIES,0.50),20)
	the_store.insert_products(0,Product(the_store.new_product_code(),
		"Bread type 1",Product.GROCERIES,0.40),20)
	the_store.insert_products(0,Product(the_store.new_product_code(),
		"Bread type 2",Product.GROCERIES,0.30),20)
	the_store.insert_products(0,Product(the_store.new_product_code(),
		"Bread type 3",Product.GROCERIES,0.20),20)
	# get_products
	for shelf in the_store.get_shelves():
		shelf.get_products()

	# login - persona
		# crea carrello 



if __name__ == "__main__":
    # execute only if run as a script
    main()