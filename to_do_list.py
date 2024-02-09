# Create a to-do list program :

import time

# Create a list to store tasks.
to_do_list = []
# Create a variable to store the sleep time.
sl=1.2

# Add a task to the to-do list.
def add_task():
    task = input("Enter a task: ")
    to_do_list.append(task)
    print("Task added.")
    time.sleep(sl)
    print("_"*100)

# View all tasks in the to-do list.
def view_tasks():
    if len(to_do_list) != 0:
        for task in to_do_list:
            print(task)
    else:
        print("No tasks to view.")
    print("_"*100)
    time.sleep(sl)

# Mark a task as done.
def mark_task():
    if len(to_do_list) != 0:
        task = input("Enter a task to mark as done: ")
        if task in to_do_list:
            task_index = to_do_list.index(task) # get the index of the task because list index(to_do_list[task] #error)task:need to be an integer not string
            new_task = to_do_list[task_index]+ " " +"Done" 
            to_do_list[task_index] = new_task 
            print("Task marked as done.")
        else:
            print("Task not found.")
    else:
        print("No tasks to mark as done.")
    print("_"*100)
    time.sleep(sl)

# Remove a task from the to-do list.
def remove_task():
    if len(to_do_list) != 0:
        task = input("Enter a task to remove: ")
        if task in to_do_list:
            to_do_list.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")
    else:
        print("No tasks to remove.")
    print("_"*100)
    time.sleep(sl)

# Create a menu that presents options to the user. Common menu options include: add, view, mark as done, remove, and quit.
def main():
    while(True):
        print("_"*100)
        print("choose the following options: ")
        print(" ")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as done")
        print("4. Remove a task")
        print("5. Quit the program")
        print("_"*100)
    
    # Get the user's choice.
        print(" ")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("_"*100)
            print("You are sure for quit the program?")
            choice=input("Enter your choice yes or no: ")
            if choices=="yes":
                print("Goodbye!")
                break
            else :
                print("Continue to the program")
                time.sleep(0.5)
                main()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(sl)
        

main()
