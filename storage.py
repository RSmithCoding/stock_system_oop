import json

FILE_PATH = "stock_backup.json"
FILE_PATH2 = "history_backup.json"

def save_stock(data):
    """Write saved stock dictionary to file."""

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent= 4)
    

def load_stock(stock):
    """Check if file exists, if not create new black file. If file exists then load from the file and into stock dictionary."""
    try:
        with open(FILE_PATH, "r") as file:
            loaded_data = json.load(file)
            print("Loading stock from backup..")
            for item in loaded_data:
                stock.add_new_product(item['name'], item['price'], item['quantity'], item['reorder'])
    except (FileNotFoundError, json.JSONDecodeError):
        print("Back up file not found or currupt, creating a new backup with default data..")
        data = stock.stock_to_dict()
        save_stock(data)

def save_history(data):
    """Write saved history dictionary to file"""

    with open(FILE_PATH2, "w") as file:
        json.dump(data, file, indent=4)

def load_history():
    pass
