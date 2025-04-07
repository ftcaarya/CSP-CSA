# Preloaded list of numbers
numbers = [5, 12, 3, 20, 8]

# Function that handles adding and filtering numbers
def number_menu(num_list):
    while True:
        # Asks the user for what their desired action is, to filter the numbers, to add numbers or exit the program
        action = input("\nType 'filter' to filter numbers, 'add' to add number, or 'quit' to exit: ").lower()

        #Executes if the desired user action is to filter
        if action == "filter":
            # Asks the user for what number they want to filter above and makes it an integer data type
            limit = int(input("Enter limit to filter numbers greater than it: "))
            # Creates a list to hold filtered numbers separately
            filtered = []
            # Goes through every number in the list fo numbers
            for num in num_list:
                # if the number is above the filter limit specified the add it to the filtered list of numbers
                if num > limit:
                    filtered.append(num)
            # Output the filtered list of numbers
            print("Filtered numbers:", filtered)

        # Executes if the desired action is to add a number
        elif action == "add":
            # Asks the user for what number they want to add and makes it an integer data type
            new_number = int(input("Enter a number to add: "))

            """
            Checks to see if the number user wants to add is already in the list of numbers
            If it is then it lets the user know it is already in the list and doesn't add it
            If it isn't then it adds the number to the list and lets user know what number was added
            """
            if new_number in num_list:
                print("Number already exists in the list. Not added.")
            else:
                num_list.append(new_number)
                print(f"{new_number} added to the list.")

        # Executes if the desired user action is to quit and exit the program
        elif action == "quit":
            print("Goodbye!")
            break

        # Handles invalid inputs, prompts the user to try again
        else:
            print("Invalid option. Try again.")

# Calls the function
number_menu(numbers)
