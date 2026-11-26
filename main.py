from stock import Stock
from history import History
import storage

stock = Stock()
history = History()

def get_status():

    while True:

        ask = input("\nPlease choose which history report or enter for 'all' (sale / delivery): ").lower().strip()

        if ask == "": 
            return "all" 
        elif ask == "sale" or ask == "delivery":
            return ask
        else:
            print("\nPlease type a valid choice (sale / delivery) or enter for 'all'")

def get_name():

    while True:

        ask = input("\nPlease enter the product name: ").lower().strip()
        if ask != "":
            return ask
        else:
            print("\nPlease enter a name for the product.")

def get_price():

    while True:

        try:
            ask = float(input("\nPlease enter the price of the product: "))
            if ask > 0:
                return ask
            else:
                print("\nPlease enter a price above 0")
        except ValueError:
            print("\nPlease enter the amount in £x.xxp format.")

def get_value(prompt):

    while True:

        try:
            ask = int(input(f"\nPlease enter the {prompt}: "))
            if ask > 0:
                return ask
            else:
                print("\nPlease enter a whole number above 0")
        except ValueError:
            print("\nPlease type a whole number")

storage.load_stock(stock)
storage.load_history(history)

while True:

    choice = input("\nPlease enter one of the following (sell / receive / add / report / reorder / history / quit): ").lower().strip()

    if choice == "sell":
        check = input("\nPlease enter the name of the product to sell: ").lower().strip()
        product = stock.check_product(check)
        if product is not None:
            check_amount = get_value("quantity")
            if product.check_stock(check_amount):
                product.down_stock(check_amount)
                history.add_history("sale", product.name, product.price, check_amount)
                print("\nOrder Processed and added to history")
                storage.save_stock(stock.stock_to_dict())
                storage.save_history(history.history_to_dict())
                if product.level_is_low():
                    print("\nWarning Stock is Low")

            else:
                print(f"\nNot enough stock only {product.quantity} left") 

    elif choice == "receive":
        check_name = input("\nPlease enter the product name that has been received: ").lower().strip()
        product = stock.check_product(check_name)
        if product is not None:
            amount_to_add = get_value("quantity")
            product.add_stock(amount_to_add)
            history.add_history("delivery", product.name, product.price, amount_to_add)
            print(f"\n{amount_to_add} x {product.name} have been added to stock and saved in history")
            storage.save_stock(stock.stock_to_dict())
            storage.save_history(history.history_to_dict())

    elif choice == "add":

        p_name = get_name()
        p_price = get_price()
        p_quantity = get_value("quantity")
        p_reorder = get_value("reorder level")
        stock.add_new_product(p_name, p_price, p_quantity, p_reorder)
        storage.save_stock(stock.stock_to_dict())

    elif choice == "report":
        stock.report()

    elif choice == "reorder":
        stock.reorder_level()

    elif choice == "history":
        status = get_status()
        history.print_history(status)    

    elif choice == "quit":
        storage.save_stock(stock.stock_to_dict())
        storage.save_history(history.history_to_dict())
        print("\nStock backed up")
        print("\nHistory backed up")
        break

    else:
        print("\nSorry please choose from the following (sell / receive / add / report / reorder / history / quit)")  