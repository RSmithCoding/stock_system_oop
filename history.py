
class HistoryItem:

    def __init__(self, name, price, quantity_sold):

        self.name = name
        self.price = float(price)
        self.quantity_sold = int(quantity_sold)
        
    

class History:
    
    def __init__(self):

        self.history_items = []

