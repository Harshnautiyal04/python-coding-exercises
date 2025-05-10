#Simple task manager 
# takes list

tasks = []

#function to display menu

def show_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Task")
    print("4. Exit")

# Fucntion to add a task 

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# fucntion to remove a task 

def remove_task():
    if not tasks:
        print("No tasks to remove!")
        return 
    view_tasks()
    try:
        index =int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number! ")
    except ValueError:
        print("Please enter a valid number!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks available!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

            
# main loop

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting Task manager, Have a great day!")
        break
    else:
        print("Invalid choice! please enter a number between 1 and 4.")
