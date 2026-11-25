from datetime import datetime

class HistoryItem:
    """Each history item"""

    def __init__(self, status, name, price, quantity):

        self.date = datetime.now()
        self.status = status
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return(f"{self.date:%d/%m/%Y %H:%M}{self.status:<2}{self.name:<4}{self.price:<4.2f}{self.quantity:<2}{self.line_total():.2f}")    
        
    def line_total(self):
        """Total of each order line"""
        return float(self.price * self.quantity)

class History:
    """All order history"""

    def __init__(self):

        self.history_items = []

    def add_history(self, status, name, price, quantity):
        """Adds a sale to the history list"""
        self.history_items.append(self.date, status, name, price, quantity)
        pass

    def print_history(self, status= "all"):
        """Prints order history depending on 'status' being delivery, sale or all"""
        for item in self.history_items:
            if status == "all" or item.status == status:
                print(item)
        print(f"{self.grand_total():.2f}")
        
    def grand_total(self):
        """Total of all orders sold"""
        return sum(self.line_total())

