import json
import os

FILENAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []


def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)


tasks = load_tasks()


def show_menu():
    print("\n--- Task Manager ---\n")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def add_task():
    task = input("Enter the task: ")
    tasks.append({
        "task": task,
        "completed": False
    })

    save_tasks()

    print(f"Task '{task}' added successfully!")


def show_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"

            print(f"{index + 1}. {task['task']} - {status}")


def mark_task_completed():
    show_tasks()

    if not tasks:
        return

    try:
        task_number = int(
            input("Enter the task number to mark as completed: ")
        )

        if 0 < task_number <= len(tasks):

            tasks[task_number - 1]["completed"] = True

            save_tasks()

            print(
                f"Task '{tasks[task_number - 1]['task']}' marked as completed!"
            )

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid task number.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        task_number = int(
            input("Enter the task number to delete: ")
        )

        if 0 < task_number <= len(tasks):

            removed_task = tasks.pop(task_number - 1)

            save_tasks()

            print(
                f"Task '{removed_task['task']}' deleted successfully!"
            )

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid task number.")


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()

    elif choice == '2':
        show_tasks()

    elif choice == '3':
        mark_task_completed()

    elif choice == '4':
        delete_task()

    elif choice == '5':
        print("Exiting Task Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")