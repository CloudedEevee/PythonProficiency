class Product:
    def __init__(self, data):
        self.name = data['name']
        self.price = data['price']
        self.category = data['category']

######################## Create Products Model



######################## Read Products Model
    def print_info(self):
        print(f"{self.name}, a {self.category} product, costs ${self.price}")
        return self

######################## Update Products Model
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += percent_change
            return self
        self.price -= percent_change
        return self


######################## Delete Products Model





