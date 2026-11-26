import json
from datetime import datetime

STOCK_FILE_PATH = "stock_backup.json"
HISTORY_FILE_PATH = "history_backup.json"

def save_stock(data):
    """Write saved stock dictionary to file."""

    with open(STOCK_FILE_PATH, "w") as file:
        json.dump(data, file, indent= 4)
    

def load_stock(stock):
    """Check if file exists, if not create new blank file. If file exists then load from the file and into stock dictionary."""
    try:
        with open(STOCK_FILE_PATH, "r") as file:
            loaded_data = json.load(file)
            print("\nLoading stock from backup..")
            for item in loaded_data:
                stock.add_new_product(item['name'], item['price'], item['quantity'], item['reorder'])
            print("\n..done")
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nStock backup file not found or corrupt, creating a new backup with default data..")
        data = stock.stock_to_dict()
        save_stock(data)

def save_history(data):
    """Write saved history dictionary to file"""

    with open(HISTORY_FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def load_history(history):
    """Check if file exist or corrupt, if exists then loads history from file using add history function"""
    try:
        with open(HISTORY_FILE_PATH, "r") as file:
            loaded_data = json.load(file)
            print("\nLoading history from backup..")
            for item in loaded_data:
                saved_date = datetime.fromisoformat(item['date'])
                history.add_history(item['status'], item['name'], item['price'], item['quantity'], saved_date)
        print("\n..done")

    except (FileNotFoundError, json.JSONDecodeError):
        print("\nHistory Backup file not found or corrupt, a new backup will be created with any history from to-day.")
