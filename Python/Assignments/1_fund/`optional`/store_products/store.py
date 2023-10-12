import product

class Store:
    def __init__(self, data):
        self.name = data['name']
        self.products = []

######################## Create Stores Model



######################## Read Stores Model
    def display_products(self):
        for each_product in self.products:
            each_product.print_info()
        return self


######################## Update Stores Model
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        print(f"{self.products[id]} has sold. Removing from Store data.....")
        self.products.pop(id)
        print("Product sold. Have a nice day!")
        return self

######################## Delete Stores Model





