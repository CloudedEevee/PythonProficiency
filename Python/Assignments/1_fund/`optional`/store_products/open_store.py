import product, store

gold_bar_shop = store.Store({'name' : "Gold Bar Shop"})

milk_chocolate = product.Product({'name' : "Milk Chocolate", 'price' : 2, 'category' : "Chocolate"})
dark_chocolate = product.Product({'name' : "Dark Chocolate", 'price' : 1, 'category' : "Chocolate"})
white_chocolate = product.Product({'name' : "White Chocolate", 'price' : 3, 'category' : "Chocolate"})

print("##############################")
gold_bar_shop.add_product(milk_chocolate).add_product(dark_chocolate).add_product(white_chocolate).display_products()

