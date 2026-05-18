
from todo_func import show_menu , add_tasks , view_tasks , mark_done , delete_tasks , save_tasks, tasks

class todo:
    while True:
        show_menu()
        try:
            choice = int(input("Enter option [1:5] : "))
        except ValueError:
            print("invalid option... 😞")
        
        if choice == 1:
            add_tasks()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_done()
        elif choice == 4:
            delete_tasks()
        elif choice == 5:
            print("Tasks Saved... 👍")
            save_tasks(tasks)
            break

if __name__ == "__main__":
    todo()