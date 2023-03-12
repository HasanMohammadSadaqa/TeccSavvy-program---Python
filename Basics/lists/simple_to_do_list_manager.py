# note that i can use dictionaries for both list of tasks and list of operations but because this exercise on lists
# note that i can use function to make this program more advance but the exercise simple like this
list_of_tasks = [
    "study the list in python",
    "study the Loops in python",
    "study functions in python",
    "make an exercises on each title"
]
print(f"the tasks you have to do are: \n{list_of_tasks}")
operations = {
    1: "Add a task to your list",
    2:"remove a task from your list",
    3: "modify a specific task"
}
print("You can: ")
for operation in operations.items():
    print(f"{operation[0]}) {operation[1]}")
while True:

    try:
        operation_number = int(input("Choose to edit your tasks: "))
        if operation_number <1 or operation_number > 3:
            print("please select from the list ")
        if operation_number == 1:
            print(f"current tasks are: {list_of_tasks}")
            new_task = input("write the new task: ")
            list_of_tasks.append(new_task)
            print(f"new tasks are: {list_of_tasks}")
        if operation_number == 2:
            print(f"current tasks are: {list_of_tasks}")
            task_to_remove = input("write the task you want to remove: ")
            list_of_tasks.remove(task_to_remove)
            print(f"new tasks are: {list_of_tasks}")
        if operation_number == 3:
            print(f"current tasks are: {list_of_tasks}")
            task_to_modify = input("write a task you want to modify: ")
            task_modified = input("write the edited task: ")
            list_of_tasks.remove(task_to_modify)
            list_of_tasks.append(task_modified)
            print(f"new tasks are: {list_of_tasks}")
    except ValueError:
        print("please enter number from operation list ex: 1")

