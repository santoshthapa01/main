# Initialize an empty list to store tasks
tasks = []

# Function to display tasks
def display_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. [{status}] {task['task']}")

# Function to add a task
def add_task():
    task_name = input("\nEnter a new task: ")
    tasks.append({"task": task_name, "completed": False})
    print("Task added successfully!")

# Function to delete a task
def delete_task():
    display_tasks()
    try:
        task_num = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as complete
def mark_task_complete():
    display_tasks()
    try:
        task_num = int(input("\nEnter the number of the task to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    while True:
        print("\nTo-Do List App")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Mark task as complete")
        print("5. Quit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_complete()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
main()
