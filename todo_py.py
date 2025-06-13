import json

tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    save_tasks()
    print("Task added.")


def list_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        for i, t in enumerate(tasks):
            status = "y" if t["done"] else "n"
            print(f"{i+1}. [{status}] {t['task']}")


load_tasks()
print("Tasks loaded:", tasks)

def mark_done():
    list_tasks()  # Show the list first
    if not tasks:
        return

    try:
        num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
            save_tasks()
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    list_tasks()  # Show the tasks first
    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)  # Remove the task
            save_tasks()
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")




load_tasks()
while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")



    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice=='3':
        mark_done()
    elif choice=='4':
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

