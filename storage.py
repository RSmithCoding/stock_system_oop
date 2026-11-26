# import json

# FILE_PATH = "stock_backup.json"


# #loading file:
# with open(FILE_PATH, "r") as file:
#     loaded_file = json.load(file)

# #saving file:
# with open(FILE_PATH, "w") as file:
#     json.dump(data, file, indent= 4)

class Product:

    def __init__(self, name, price, quantity, reorder):

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.reorder = reorder

    def to_dict(self):
        """Returns products as a dictionary ready to be saved"""
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "reorder": self.reorder
        }
    
class Stock:

    def __init__(self):
        self.stock_items = {
            "pens": Product("pens", 0.80, 50, 20),
            "notebooks": Product("notebooks", 2.50, 15, 10),
            "staplers": Product("staplers", 6.00, 4, 5)
        }        

    def stock_to_dict(self):
        saved_stock = []
        for product in self.stock_items.values():
            saved_stock.append(product.to_dict())
        return saved_stock

    def test_print(self):
        for product in self.stock_items.values():
            print(f"{product.name} {product.price} {product.quantity} {product.reorder}")


beans = Product("beans",1.99,50,10)
print(f"This is product beans {beans.name} {beans.price} {beans.quantity} {beans.reorder}")

stock = Stock()

print(stock.test_print())

dict = beans.to_dict()

print(dict)

print(stock.stock_to_dict())




def save_stock():
    """Save stock to a dictionary and write to file."""
    pass

def load_stock():
    """Check if file exists, if not create new black file. If file exists then load from the file and into stock dictionary."""
    pass

def save_history():
    pass

def load_history():
    pass