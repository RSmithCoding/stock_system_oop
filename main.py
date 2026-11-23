from stock import Stock, Product

stock = Stock()


def get_value():

    while True:

        try:
            ask = int(input("Please enter the quantity: "))
            return ask
        except ValueError:
            print("Please type a whole number")

while True:

    choice = input("Please enter enter one of the following (sell / recieve / add / report / reorder / quit): ").lower().strip()

    if choice == "sell":
        check = input("Please enter the name of the product to sell: ")
        product = stock.check_product(check)
        if product is not None:
            check_amount = input("Please enter the amount needed: ")
            if product.check_stock(check_amount):
                product.down_stock(check_amount)
                print("Order Processed")
                if product.level_is_low():
                    print("Warning Stock is Low")

            else:
                print(f"Not enough stock only {product.quantity} left")
        

    elif choice == "recieve":
        check_name = input("Please enter the product name that has been recieved: ").lower().strip()
        product = stock.check_product(check_name)
        if product is not None:
            product.add_stock(get_value())
        

    elif choice == "add":
        p_name = input("Please enter the name of the product to add to stock: ").lower().strip()
        p_price = float(input("Please enter the price of the product to add to stock: "))
        p_quantity = int(input("Please enter the quantity of the product to add to stock: "))
        p_reorder = int(input("Please enter the reorder level of the product to add to stock: "))
        stock.add_new_product(p_name, p_price, p_quantity, p_reorder)

    elif choice == "report":
        stock.report()

    elif choice == "reorder":
        stock.reorder_level()

    elif choice == "quit":
        break