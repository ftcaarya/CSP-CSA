# Preloaded list of grades
grades = [85.5, 90.0, 72.5, 88.0]

# Function to interact with grades
def grade_menu(grade_list):
    while True:
        # Asks the user for their desired action of choice.
        action = input("\nType 'average' to calculate average, 'add' to add a grade, or 'quit' to exit: ").lower()

        # Executes if the action the user desires is to calculate the average of the grades in the list
        if action == "average":
            # Asks the user for a threshold to check if the average is below or above it
            threshold = float(input("Enter threshold: "))
            total = 0
            count = 0

            # Goes through every grade in the list of grades
            for grade in grade_list:
                # If the grade is greater than or equal to the threshold then add it to the total and increase count by 1
                if grade >= threshold:
                    total += grade
                    count += 1
            # If there are grades that are above the threshold print the average of the grades above the threshold
            if count > 0:
                print("Average above threshold:", total / count)
            else:
                # If there are no grades above the threshold then output letting the user know no grades meet the threshold
                print("No grades met the threshold.")

        # Executes if the action the user desires is to add a grade
        elif action == "add":
            # Asks the user for the new grade they want to add to the list of grades
            new_grade = float(input("Enter the new grade: "))
            # Adds the new grade to the list of grades
            grade_list.append(new_grade)
            # Lets the user know which grade was added
            print(f"Grade {new_grade} added.")

        # Executes if the action the user desires is to quit the program
        elif action == "quit":
            print("Goodbye!")
            break

        # Handles invalid inputs and makes the user try again
        else:
            print("Invalid option. Try again.")

# Calls the whole function
grade_menu(grades)
