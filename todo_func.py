import json

def save_tasks(tasks):
    with open("todo.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open("todo.json") as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []  


tasks = load_tasks()

def show_menu():
    print("\n ----------todo menu----------\n")
    print("1. Add task \n2. View Tasks \n3. Mark task as done \n4. Delete task \n5. Quit\n")

def add_tasks():
    task = input("Which task do you want to add : ")
    tasks.append({"task": task, "status": False})
    save_tasks(tasks)

def view_tasks():
    if not tasks:
        print("Task not found... 😢")
        return
    print("\nYour tasks :")
    for index,task in enumerate(tasks, start = 1):
        status_emoji = "✅" if task["status"] else "⬜"
        print(f"{index}. {task["task"]} {status_emoji}")

def mark_done():
    view_tasks()
    if not tasks:
        print("no tasks added yet")
        return
    try :
        index = int(input("Enter the task no : ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["status"] = True
            print("task completed... 👍")
            save_tasks(tasks)
        else:
            print("invalid option : ")
    except ValueError :
        print("Please enter a valid option")

def delete_tasks ():
    view_tasks()
    if not tasks:
        print("no tasks added yet")
        return
    try :
        index = int(input("Enter 1the task no : ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("task removed... 🎉")
            save_tasks(tasks)
        else:
            print("Invalid option... 😞")
    except ValueError :
        print("Please enter a valid option")