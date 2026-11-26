import json
from datetime import datetime

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
            print("\nLoading stock from backup..\n")
            for item in loaded_data:
                stock.add_new_product(item['name'], item['price'], item['quantity'], item['reorder'])
            print("\n..done\n")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Stock backup file not found or corrupt, creating a new backup with default data..")
        data = stock.stock_to_dict()
        save_stock(data)

def save_history(data):
    """Write saved history dictionary to file"""

    with open(FILE_PATH2, "w") as file:
        json.dump(data, file, indent=4)

def load_history(history):
    """Check if file exist or corrupt, if exists then loads history from file using add history function"""
    try:
        with open(FILE_PATH2, "r") as file:
            loaded_data = json.load(file)
            print("Loading history from backup..\n")
        for item in loaded_data:
            saved_date = datetime.fromisoformat(item['date'])
            history.add_history(item['status'], item['name'], item['price'], item['quantity'], saved_date)
        print("..done\n")

    except (FileNotFoundError, json.JSONDecodeError):
        print("History Backup file not found or corrupt, a new backup will be created with any history from to-day.")
