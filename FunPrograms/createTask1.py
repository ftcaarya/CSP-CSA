# List that already starts with some to do tasks
tasks = ["Do homework", "Walk the dog", "Read a book"]

#Procedure to manage the tasks
def manage_tasks():
    while True:
        # Asks the user for their desired action
        action = input("Choose action (add/view/remove/done): ")

        # If the user is done with modifying the to-do list then it exits the while loop
        if action == "done":
            break
        # If the user wants to view the to-do list
        elif action == "view":
            # The program iterates through each of the items in the list and displays them for the viewer to view
            for task in tasks:
                print("- " + task)
        # If the user wants to add an item to the to-do list
        elif action == "add":
            # Asks the user for the name of the task they want to add
            new_task = input("Enter a new task: ")
            # Adds it to the list of to-do items
            tasks.append(new_task)
        # If the user wants to remove an item from the to-do list
        elif action == "remove":
            # Asks the user for what task they want to remove from the to-do list
            task_to_remove = input("Enter task to remove: ")
            # Checks to see if the task they want to remove is really in the list or not to prevent any errors
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
            else:
                print("Task not found.")

# The function is executed.
manage_tasks()