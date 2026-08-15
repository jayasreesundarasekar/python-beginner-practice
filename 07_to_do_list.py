# Simple To-Do List

tasks = []


def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\n--- Your Tasks ---")

        for index, task in enumerate(tasks, start=1):
            print(index, ".", task)


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")


def remove_task():
    show_tasks()

    if len(tasks) == 0:
        return

    task_number = int(input("Enter task number to remove: "))

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print("Removed:", removed_task)
    else:
        print("Invalid task number.")


while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")