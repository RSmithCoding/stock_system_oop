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
        return(f"{self.date:%d/%m/%Y %H:%M} {self.status:<10} {self.name:<15} £ {self.price:<6.2f} {self.quantity:<3} £ {self.line_total():.2f}")    
        
    def line_total(self):
        """Total of each order line"""
        return (self.price * self.quantity)

class History:
    """All order history"""

    def __init__(self):

        self.history_items = []

    def add_history(self, status, name, price, quantity):
        """Adds a sale to the history list"""
        self.history_items.append(HistoryItem(status, name, price, quantity))
   

    def print_history(self, status= "all"):
        """Prints order history depending on 'status' being delivery, sale or all"""
        if not self.history_items:
            print("Sorry no history to show")
        
        else:    
            for item in self.history_items:
                if status == "all" or item.status == status:
                    print(item)
        
            print(f"\n\t\t\t\t\t    Grand Total: £ {self.grand_total(status):.2f}\n")

    def grand_total(self, status= "all"):
        """Total of all orders sold"""
        total = 0
  
        for item in self.history_items:
            if status == "all" or item.status == status:
                total += item.line_total()
                
        return total

