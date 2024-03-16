import time

todolist = []

while True:
    print("\nOptions:")
    print("1. Set a Reminder")
    print("2. To-Do List")
    print("3. Close the Program")

    option = input("Enter your option (1/2/3): ")

    if option == "1":
        print("What shall I remind you about?")
        reminder = input()
        print("In how many minutes?")
        minutes = float(input())
        seconds = minutes * 60
        time.sleep(seconds)
        print(reminder)
    elif option == "2":
        while True:
            print("\nTo-Do List Options:")
            print("1. Enter a new task")
            print("2. Delete a task")
            print("3. Display the to-do list")
            print("4. Back to the main menu")

            todo_option = input("Enter your option (1/2/3/4): ")

            if todo_option == "1":
                task = input("Enter your task: ")
                todolist.append(task)
                print("Task added to the list")
            elif todo_option == "2":
                if len(todolist) == 0:
                    print("No tasks available to remove")
                else:
                    print("To-do list:")
                    for i, task in enumerate(todolist, start=1):
                        task_number = int(input("Enter the number of the task to remove: "))
                        if 1 <= task_number <= len(todolist):
                            removed_task = todolist.pop(task_number - 1)
                            print("Task successfully removed.")
                        else:
                            print("Error: Invalid task number. No task was removed")
            elif todo_option == "3":
                if len(todolist) == 0:
                    print("The to-do list is empty.")
                else:
                    print("To-Do List:")
                    for i, task in enumerate(todolist, start=1):
                        print(f"{i}. {task}")
            elif todo_option == "4":
                print("Returning to the main menu...")
                break
            else:
                print("Error: Invalid option. Please select a valid choice (1/2/3/4)")
    elif option == "3":
        print("Closing the program...")
        break
    else:
        print("Error: Invalid option. Please select a valid choice (1/2/3)")
