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

    def check_product(self, name):
        """Checks to see if the product exists"""
        if name in self.stock_items:
            return self.stock_items[name]
        else:
            print("")
            print(f"Sorry {name} is not an item that is in stock.")
            return None
    
    def add_new_product(self, name, price, quantity, reorder):
        """Add new products to stock"""
        self.stock_items[name] = Product(name, price, quantity, reorder)
        print(f"{name} is added to stock")

    def report(self):
        """List all stock with quantities and stock values along with total value"""
        running_total = 0
        print("\nName\t\t     Price\tQuantity     Reorder Level     Stock Value\n")
        for product in self.stock_items.values():
            print(f"{product.name:<20} £{product.price:<12.2f} {product.quantity:<14} {product.reorder:<14} £{product.stock_value():.2f}")
            running_total += product.stock_value()  
        print(f"\n\t\t\t\t           Total Stock Value:    £{running_total:.2f}\n")


    def reorder_level(self):
        """Lists only the stock at or below reorder level"""
        flag = 0 
        for product in self.stock_items.values():
            if product.level_is_low():
                print(f"\n{product.name:<20}x {product.quantity:<2} in stock - reorder level: {product.reorder}")
                flag += 1        
        
        if flag == 0:
            print(f"\nThere are no products low on stock")
        else:
            print(f"\nTotal number of orders to make for stock: {flag}")

    def stock_to_dict(self):
        """Iterates through all products and passes them through to_dict then adds each product dictionary to a list"""
        saved_stock = []
        for product in self.stock_items.values():
            saved_stock.append(product.to_dict())
        return saved_stock