# Initialize an empty to-do list
to_do_list = {}

# Function to add a task to the to-do list
def add_task():
    task = input("Enter the task: ")
    to_do_list[task] = "Not Done"

# Function to mark a task as done
def mark_done():
    task = input("Enter the task to mark as done: ")
    if task in to_do_list:
        to_do_list[task] = "Done"
    else:
        print("Task not found in the to-do list.")

# Function to display the to-do list
def display_list():
    print("\nTo-Do List:")
    for task, status in to_do_list.items():
        print(f"- {task} [{status}]")

# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Mark a task as done")
    print("3. Display the to-do list")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        mark_done()
    elif choice == "3":
        display_list()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
