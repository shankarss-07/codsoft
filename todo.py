
#simple to_do list using python
to_do_list = []

#user option menu printing
def show_menu():
    print("\nTo-Do List Menu:")
    print("------------------")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

# to add task
def add_task():
    task = input("Enter the task: ")
    to_do_list.append(task)
    print(f"Task '{task}' added to the list.")

#to view task
def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour to-do list:")
        for idx, task in enumerate(to_do_list, 1):
            print(f"{idx}. {task}")

#to remove codition
def remove_task():
    view_tasks()
    if to_do_list:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(to_do_list):
            removed_task = to_do_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")

# main function for user todo list
#and store n number of list
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
