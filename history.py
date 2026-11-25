from datetime import datetime

class HistoryItem:
    """Each history item"""

    def __init__(self, status, name, price, quantity):

        self.date = datetime.now()
        self.status = status
        self.name = name
        self.price = float(price)
        self.quantity_sold = int(quantity)
        
    def line_total(self):
        """Total of each order line"""
        pass

class History:
    """All order history"""

    def __init__(self):

        self.history_items = []

    def add_history(self, status, name, price, quantity):
        """Adds a sale to the history list"""
        pass

    def print_history(self, status= "all"):
        """Prints order history depending on 'status' being delivery, sale or all"""
        pass

    def grand_total(self):
        """Total of all orders sold"""
        pass

