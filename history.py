from datetime import datetime

class HistoryItem:
    """Each history item"""

    def __init__(self, status, name, price, quantity, date=None):
        if date is None:
            self.date = datetime.now()
        else:
            self.date = date
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
    
    def to_dict(self):
        """Returns items as a dictionary ready to be saved"""
        date = self.date.isoformat()
        return {
            "date": date,
            "status": self.status,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

class History:
    """All order history"""

    def __init__(self):

        self.history_items = []

    def add_history(self, status, name, price, quantity):
        """Adds a sale to the history list"""
        self.history_items.append(HistoryItem(status, name, price, quantity))
   

    def print_history(self, status= "all"):
        """Prints order history depending on 'status' being delivery, sale or all"""

        status_match = []    
        for item in self.history_items:
            if status == "all" or item.status == status:
                status_match.append(item)

        if status_match:
            for match in status_match:
                print(match)

            print(f"\n\t\t\t\t\t    Grand Total: £ {self.grand_total(status):.2f}\n")
        
        else:
            print("No history available for the selected status")

    def grand_total(self, status= "all"):
        """Total of all orders sold"""
        total = 0
  
        for item in self.history_items:
            if status == "all" or item.status == status:
                total += item.line_total()
                
        return total

    def history_to_dict(self):
        """Iterates through all items and passes them through to_dict then adds each product dictionary to a list"""
        saved_history = []
        for item in self.history_items.values():
            saved_history.append(item.to_dict())
        return saved_history