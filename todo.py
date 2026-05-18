
from todo_func import show_menu , add_task , view_tasks , mark_done ,unmark_done, delete_task , save_tasks, tasks

class todo:
    while True:
        show_menu()
        try:
            choice = int(input("Enter option [1:6] : "))
        except ValueError:
            print("invalid option... 😞")
        
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_done()
        elif choice == 4:
            unmark_done()
        elif choice == 5:
            delete_task()  
        elif choice == 6:
            print("Tasks Saved... 👍")
            save_tasks(tasks)
            break

if __name__ == "__main__":
    todo()