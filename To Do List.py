task = ["Assignment", "Reading", "Meditation", "Workout"]

while True:
    # Display menu options to the user
    print("\nTo Do List Menu:")
    print("1. View Task")
    print("2. Add Task")
    print("3. Remove a Task")
    print("4. Exit")

    choice = input("Which option do you want? ") # Take user choice

    if choice == "1":# Display all tasks in the list
        print(task)

    elif choice == "2":# append() adds a new task at the end of the list by taking user input
        new_task = input("Enter a new Task: ")
        task.append(new_task)
        print("Task Added Successfully.")

    elif choice == "3":# remove() returns None, so we take user input and remove the task only if it exists
        task_name = input("Enter task to remove: ")
        if task_name in task: # Check if task exists to avoid runtime error
            task.remove(task_name)
            print("Task removed successfully.")
        else:
            print("Task not found.")  # Display updated task list

        print(task)

    elif choice == "4": # Exit the infinite loop
        break

    else:# Handle invalid menu choice
        print("Invalid Choice. Please try again.")

# Program termination message
print("Thank You")
