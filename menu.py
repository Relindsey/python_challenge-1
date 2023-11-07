menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

order_list = []
def add_to_order(item, price, quantity):
    order_list.append({
        "item": item,
        "price": price,
        "quantity": quantity
    })

print("Welcome to the Variety Food Truck.")
place_order = True
while place_order:
    print("From which menu would you like to order? ")

    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1
    menu_category = input("Type menu number: ")

    if menu_category.isdigit():
     if int(menu_category) in menu_items.keys():
        menu_category_name = menu_items[int(menu_category)]
        print(f"You selected {menu_category_name}")
        print(f"What {menu_category_name} item would you like to order? ")
        i = 1
        menu_items = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            if type(value) is dict:
                for key2, value2 in value.items():
                    num_item_spaces = 24 - len(key + key2) - 3
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                    menu_items[i] = {
                        "Item name": key + " - " + key2,
                        "Price": value2
                    }
                    i += 1
            else:
                num_item_spaces = 24 - len(key)
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key}{item_spaces} | ${value}")
                menu_items[i] = {
                    "Item name": key,
                    "Price": value
                }
                i += 1
            
        item_number = input("Please enter a menu item number: ")
        if item_number.isdigit():
            item_number = int(item_number)
            if 1 <= item_number <= len(menu_items):
                selected_item = menu_items[item_number]
                item_name = selected_item["Item name"]
                item_price = selected_item["Price"]
                print(f"You selected '{item_name}' for ${item_price}.")
                quantity = input("How many would you like to order?")
                if quantity.isdigit():
                    quantity = int(quantity)
                else:
                    print("You entered an invalid quantity. \nDefaulting the quantity to 1")
                    quantity = 1
                add_to_order(item_name, item_price, quantity)
                print(f"{quantity} '{item_name}' added to your order.")
            else:
                print("Customer input is invalid.")
        else:
            print(f"{menu_category} was not a menu option.")
    else:
        print("You didn't select a number.")
    
    while place_order:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        if keep_ordering.lower() == "yes" or keep_ordering.lower() == "y":
            place_order = True
            break
        if keep_ordering.lower() == "no" or keep_ordering.lower() == "n":
            place_order = False
        else:
            print("Invalid input. Please enter 'Y' or 'N' ")

print ("\nThank you for your order.")

print("\nThis is what we are preparing for you.")

print("Item name                 | Price  | Quantity")

print("--------------------------|--------|----------")

total_cost = sum(item["price"] * item["quantity"] for item in order_list)
for item in order_list:
    item_name = item["item"]
    item_price = item["price"]
    quantity = item["quantity"]
    name_spaces = 26 - len(item_name)
    price_spaces = 8 - len(str(item_price))
    quantity_spaces = 10 - len(str(quantity))
    name_space_str = " " * name_spaces
    price_space_str = " " * price_spaces
    quantity_space_str = " " * quantity_spaces
    print(f"{item_name}{name_space_str}| ${item_price:.2f}{price_space_str}{quantity}{quantity_space_str}")

print("\nTotal cost of your order is: ${:.2f}".format(total_cost))