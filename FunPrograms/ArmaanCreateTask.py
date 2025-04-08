# Preloaded list of items with their prices
items = [("Milk", 3.50), ("Bread", 2.00), ("Eggs", 4.25), ("Cereal", 5.75)]

# Function that handles viewing and adding items
def check_prices(price_list):
    while True:
        # Ask the user what action they want to do, view items in budget, add items to list, or quit the whole program
        action = input("\nType 'view' to see items within budget, 'add' to add item, or 'quit' to exit: ").lower()

        # Executes if the user wants to view the items in their budget
        if action == "view":
            # Asks the user for their budget
            limit = float(input("Enter your budget: "))
            print("Items within budget:")
            # Goes through every item and price in the list of items
            for name, price in price_list:
                # Prints the item and the price if it is less than the budget specified
                if price <= limit:
                    print(f"{name}: ${price:.2f}")

        # Executes if the user wants to add items to the list of items
        elif action == "add":
            # Asks user for the name and price of the item they want to add
            name = input("Enter the name of the item: ")
            price = float(input("Enter the price of the item: "))
            # Add new item to list
            price_list.append((name, price))
            # Lets the user know what item they added
            print(f"{name} added with price ${price:.2f}") # Cut the price to only 2 decimal places for realism

        # Executes if the user wants to exit the program
        elif action == "quit":
            print("Goodbye!")
            break

        # Handles invalid options that the user tries to input
        else:
            print("Invalid option. Try again.")

# Calls the function
check_prices(items)
