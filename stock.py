class Product:

    def __init__(self, name, price, quantity, reorder):

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.reorder = reorder

    def add_stock(self, amount):
        """Ups the quantity of a product"""
        self.quantity += amount
        
    def check_stock(self, amount):
        """Checks quantity for product returns True or False"""
        if self.quantity >= amount:
            return True
        else:
            return False
        
    def down_stock(self, amount):
        """Downs the product quantity"""
        self.quantity -= amount

    def level_is_low(self):
        """Checks if the product stock level is low returns True or False"""
        if self.quantity <= self.reorder:
            return True
        else:
            return False

    def stock_value(self):            
        """Returns the stock value of the product"""
        product_value = self.quantity * self.price
        return product_value


class Stock:

    def __init__(self):
        self.stock_items = {
            "pens": Product("pens", 0.80, 50, 20),
            "notebooks": Product("notebooks", 2.50, 15, 10),
            "staplers": Product("staplers", 6.00, 4, 5)
        }

    def check_product(self):
        """Checks to see if the product exists"""
    
    def add_new_product(self):
        """Add new products to stock"""

    def report(self):
        """List all stock with quantities and stock values along with total value"""

    def reorder_level(self):
        """Lists only the stock at or below reorder level"""



"""Testing"""

stock = Stock()

pens = stock.stock_items["pens"]

print(pens.quantity)

pens.down_stock(35)
print(pens.quantity)
print(pens.level_is_low())

print(pens.check_stock(100))

print(pens.stock_value())
