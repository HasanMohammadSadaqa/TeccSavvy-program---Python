# note that I can use dictionaries for both list of tasks and list of operations but because this exercise on lists
# note that I can use function to make this program more advance but the exercise simple like this
import sys

list_of_tasks = ["study the list in python",
                 "study the Loops in python",
                 "study functions in python",
                 "make an exercises on each title"]
print(f"the tasks you have to do are: \n{list_of_tasks}")
operations = {
    1: "Add a task to your list",
    2: "remove a task from your list",
    3: "modify a specific task",
    4: "Quit"
}
print("You can: ")
for operation in operations.items():
    print(f"{operation[0]}) {operation[1]}")
while True:

    try:
        operation_number = int(input("Choose to edit your tasks: "))
        if operation_number < 1 or operation_number > 4:
            print("please select from the list ")
        if operation_number == 1:
            print(f"current tasks are: {list_of_tasks}")
            new_task = input("write the new task: ")
            new_index = int(input("where would you add it (please enter a number): "))
            list_of_tasks.insert(new_index - 1, new_task)
            print(f"new tasks are: {list_of_tasks}")
        if operation_number == 2:
            print(f"current tasks are: {list_of_tasks}")
            index_to_remove = int(input("write the number of task you want to remove: "))
            if index_to_remove < 0:
                print("please enter number greater than 0")
            elif index_to_remove > len(list_of_tasks):
                print("please enter a valid number")
            else:
                list_of_tasks.pop(index_to_remove - 1)
                print(f"new tasks are: {list_of_tasks}")
        if operation_number == 3:
            print(f"current tasks are: {list_of_tasks}")
            index_to_modify = int(input("write the number of task you want to modify: "))
            if index_to_modify <= 0:
                print("InvalidError: number must be greater than 0")
            elif index_to_modify > len(list_of_tasks):
                print("Please input a valid number")
            else:
                task_modified = input("write the edited task: ")
                list_of_tasks[index_to_modify - 1] = task_modified
                print(f"new tasks are: {list_of_tasks}")
        if operation_number == 4:
            sys.exit("Thanks for using our system")
    except ValueError:
        print("please enter number from operation list ex: 1")
