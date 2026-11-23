from stock import Stock

stock = Stock()

def get_name():

    while True:

        ask = input("Please enter the product name: ").lower().strip()
        if ask != "":
            return ask
        else:
            print("Please enter a name for the product.")

def get_price():

    while True:

        try:
            ask = float(input("Please enter the price of the product: "))
            if ask > 0:
                return ask
            else:
                print("Please enter a price above 0")
        except ValueError:
            print("Please enter the amount in £x.xxp format.")

def get_value(prompt):

    while True:

        try:
            ask = int(input(f"Please enter the {prompt}: "))
            if ask > 0:
                return ask
            else:
                print("Please enter a whole number above 0")
        except ValueError:
            print("Please type a whole number")

while True:

    choice = input("Please enter one of the following (sell / receive / add / report / reorder / quit): ").lower().strip()

    if choice == "sell":
        check = input("Please enter the name of the product to sell: ").lower().strip()
        product = stock.check_product(check)
        if product is not None:
            check_amount = get_value("quantity")
            if product.check_stock(check_amount):
                product.down_stock(check_amount)
                print("Order Processed")
                if product.level_is_low():
                    print("Warning Stock is Low")

            else:
                print(f"Not enough stock only {product.quantity} left") 

    elif choice == "receive":
        check_name = input("Please enter the product name that has been received: ").lower().strip()
        product = stock.check_product(check_name)
        if product is not None:
            amount_to_add = product.add_stock(get_value("quantity"))
            print(f"{amount_to_add} x {product.name} have been added to stock")

    elif choice == "add":

        p_name = get_name()
        p_price = get_price()
        p_quantity = get_value("quantity")
        p_reorder = get_value("reorder level")
        stock.add_new_product(p_name, p_price, p_quantity, p_reorder)

    elif choice == "report":
        stock.report()

    elif choice == "reorder":
        stock.reorder_level()

    elif choice == "quit":
        break

    else:
            print("Sorry please choose from the following (sell / receive / add / report / reorder / quit)")  