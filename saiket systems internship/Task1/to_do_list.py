def add_task(tasks):
    task_id = len(tasks) + 1
    description = input("\n""Enter task description: ")

    tasks[task_id] = {
        "description": description,
        "completed": False
    }

    print(f"\n Task added with ID {task_id}!") 


def mark_completed(tasks):
    try:
        task_id = int(input("\n""Enter Task ID to mark completed: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if task_id in tasks:
        tasks[task_id]["completed"] = True
        print(f"\n Task ID {task_id} marked as completed!")
    else:
        print(" Task ID not found.")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n""Your To-Do List status:")
    for task_id, details in tasks.items():
        status = "Completed" if details["completed"] else "Pending"
        print(f"ID {task_id}: {details['description']} → {status}")


def delete_task(tasks):
    try:
        task_id = int(input("\nEnter Task ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")    
        return

    if task_id in tasks:
        removed = tasks.pop(task_id)
        print(f"\n Task deleted: '{removed['description']}'")
    else:
        print(" Task ID not found.")


def menu():
    tasks = {}

    while True:
        print("\nTo-Do List Application")
        print("\n""1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View All Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            mark_completed(tasks)

        elif choice == "3":
            view_tasks(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\n Exiting…")
            break

        else:
            print("\n Invalid choice, Please try again.")

if __name__ == "__main__":
    menu()