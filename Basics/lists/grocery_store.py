import sys


def start():
    operations = {
        1: "Add an item to the grocery list",
        2: "Remove item from a grocery list",
        3: "View the current grocery list",
        4: "Calculate the total cost of the items on the grocery list",
        5: "Log Out"
    }

    print("Welcome to our store, Here what can we help: ")
    for operation in operations.items():
        print(f"{operation[0]}- {operation[1]}")
    try:
        operation_number = int(input("choose an operation from the list: "))
        if operation_number < 1 or operation_number > 5:
            print("Incorrect input, please try again")
            print("____________________________________________")
            start()
        if operation_number == 1:
            adding_item()
        if operation_number == 2:
            remove_item()
        if operation_number == 3:
            display_current_list()
        if operation_number == 4:
            calculate_total_cost()
        if operation_number == 5:
            sys.exit("thanks for using our system!")
            # or i can use this two line to exit
            # print("thanks for using this program!")
            # raise SystemExit

    except ValueError:
        print("please enter a number from the list ex: 1")
        print("______________________________________________")
        start()


# method to add type
def adding_item():
    if len(grocery_lits) == 0:
        print("your list is empty")
    else:
        print(f"Here is your list: \n{grocery_lits}")

    type_to_add = input("please the type you want to add: ")

    # validation for input
    type_input_errors = []
    if type_to_add.isdigit():
        type_input_errors.append("Incorrect input, type can not be numbers")
    if not type_to_add.isalpha():
        type_input_errors.append("Incorrect input, type must be only characters without any number or spaces")

    # display the errors if there is
    while len(type_input_errors) > 0:
        for error in type_input_errors:
            print(error)
            print("___________________________________________")
            adding_item()
        break
    else:
        try:
            price = int(input("please add a price for the type: "))
            if price < 0:
                print("the price should greater than 0")
                print("________________________________________")
                adding_item()
            else:
                type_to_add_number = len(grocery_lits) + 1
                grocery_lits[type_to_add_number] = {"type": type_to_add, "price": price}
                print(f"Here is the new list\n{grocery_lits}")
                print("__________________________________")
                start()
        except ValueError:
            print("price must be numbers")
            print("______________________________________________")
            adding_item()


# method to remove type
def remove_item():
    if len(grocery_lits) == 0:
        print("your list is empty")
        print("_______________________________")
        start()
    else:
        print(f"Here is your list: \n{grocery_lits}")
        try:
            type_to_remove = int(input("please enter the number of type you want to remove: "))
            del grocery_lits[type_to_remove]  # or grocery_lists.pop(type_to_remove)
            if len(grocery_lits) == 0:
                print("your list is empty now")
                print("______________________________")
                start()
            else:
                print(f"Here is the new list\n{grocery_lits}")
                print("___________________________________")
                start()
        except ValueError:
            print("please choose a number from a list")
            remove_item()


# method to display the current list
def display_current_list():
    if len(grocery_lits) == 0:
        print("your list is empty")
        print("_________________________________")
        start()
    else:
        print(f"Here is the current list: \n{grocery_lits}")
        print("________________________________________")
        start()


# method to calculate the total cost of the items
def calculate_total_cost():
    if len(grocery_lits) == 0:
        print("your list is empty and the total cost = 0")
        print("__________________________________")
        start()
    else:
        total_cost = 0
        for item in grocery_lits.items():
            total_cost += item[1]['price']
        print(f"Here is your current list: \n{grocery_lits}\n and the total cost of items is: {total_cost}")
        print("_________________________________")
        start()


if __name__ == '__main__':
    grocery_lits = {}
    start()
