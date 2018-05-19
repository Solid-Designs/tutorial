class Product:
    def __init__(self, i, p, q):
        self.identification = i
        self.price = p
        self.quantity = q
        self.item_dictionary = {'ID: ': self.identification, 'Price: ': self.price, 'Quantity: ': self.quantity}


class Inventory:
    def __init__(self):
        self.identification, self.price_list, self.quantity_list = [], [], []
        self.products = [
            product_1.item_dictionary,
            product_2.item_dictionary
        ]  # Make list of item dictionaries

        for i in self.products:
            self.identification.append(i['ID: '])
            self.price_list.append(i['Price: '])
            self.quantity_list.append(i['Quantity: '])
            # Make unique lists of ID, Price, and Quantity

        print(sum(self.price_list))


product_1 = Product(32, 23, 2)
product_2 = Product(23, 65, 3)


inventory_1 = Inventory()

