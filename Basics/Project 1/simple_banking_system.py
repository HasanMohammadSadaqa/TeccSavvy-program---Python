# note that the assumption in this system is no accounts added, so the first operation must be creating account
# the flow of this code that there is main function contains all the function needed in system
import random


# methods of the system
def start():
    operations = {
        1: "Create account",
        2: "Deposit",
        3: "Withdrew",
        4: "check balance",
        5: "transfer to another account",
        6: "logOut"
    }

    print("----------------------- operation list ---------------------")
    for operation in operations.items():
        print(f'{operation[0]}) {operation[1]}')
    #     operation input validation
    try:
        operation_number = int(input("Select operation number from the list: "))
        if operation_number < 1 or operation_number > 6:
            print("please choose number from the list ")
            start()
        elif operation_number == 1:
            create_account()
        elif operation_number == 2:
            deposit()
        elif operation_number == 3:
            withdrew()
        elif operation_number == 4:
            check_balance()
        elif operation_number == 5:
            transfer()
        elif operation_number == 6:
            if len(users_accounts) > 1:
                print("thanks for using our system")
            else:
                print("you didn't create account")
                start()
    except ValueError:
        print("You have to choose number from the list ex: 1 ")
        start()


# create account
def create_account():
    print("------------------------------- create new account ---------------------------------")
    user_name = input("User Name: ")

    # validation for username
    user_name_errors = []
    if len(user_name) < 3:
        user_name_errors.append("UserName must be at least 3 character")
    if user_name.islower():
        user_name_errors.append("UserName must have an uppercase character")
    if user_name.isupper():
        user_name_errors.append("UserName must have a lowercase character")
    if user_name.isdigit():
        user_name_errors.append("UserName must be only characters")
    if not user_name.isalpha():
        user_name_errors.append("UserName must be only characters, no spaces ")

    # display the user_name_errors
    while len(user_name_errors) > 0:
        for error in user_name_errors:
            print(error)
            create_account()
        break
    else:
        password = input("Password: ")

        # Validation for password
        password_errors = []
        if len(password) < 8:
            password_errors.append("Password must be at least 8 characters")
        if not password.isalnum():
            password_errors.append("Password must be group of characters and numbers")
        if password.isalpha():
            password_errors.append("Password must contains numbers")

        while len(password_errors) > 0:
            for error in password_errors:
                print(error)
                create_account()
            break
        else:
            account_number = random.randint(116000, 117000)
            users_accounts[account_number] = {"user name": user_name, "passwrd": password, "balance": 0}
            if account_number in users_accounts:
                print(f"Welcome {user_name}, your account number is {account_number}")
                start()


# method for deposit
def deposit():
    account_number = int(input("Enter account number: "))
    if account_number in users_accounts:
        amount = int(input("enter the amount you want to deposit: "))
        if amount > 0:
            users_accounts[account_number]["balance"] += amount
            print(f"Deposit successfully, your balance is {users_accounts[account_number]['balance']}")
            start()
        else:
            print("Invalid Error: amount must be greater than 0")
            deposit()
    else:
        print("this account not found, pleas try again")
        deposit()


# method for withdrew
def withdrew():
    account_number = int(input("Enter your account number: "))
    if account_number in users_accounts:
        amount = int(input("enter the amount you want to withdrew: "))
        if amount > 0:
            if amount <= users_accounts[account_number]['balance']:
                users_accounts[account_number]["balance"] -= amount
                print(f"Withdrew successfully, your balance is {users_accounts[account_number]['balance']}")
                start()
            else:
                print(f"your balance is {users_accounts[account_number]['balance']}")
                withdrew()
        else:
            print("Invalid Error: amount must be greater than 0")
            withdrew()
    else:
        print("this account not found, pleas try again")
        withdrew()


# method for check balance
def check_balance():
    account_number = int(input("Enter your account number: "))
    if account_number in users_accounts:
        print(f"your balance is {users_accounts[account_number]['balance']}")
        start()
    else:
        print("Account not found")
        check_balance()


# method for transfer to another account
def transfer():
    from_account_number = int(input("Enter your account number: "))

    if from_account_number in users_accounts:
        to_account_number = int(input("enter account number you want to transfer to: "))
        if to_account_number in users_accounts:
            amount = int(input("Enter the amount you want to transfer: "))
            if amount > 0:
                if amount <= users_accounts[from_account_number]["balance"]:
                    users_accounts[from_account_number]["balance"] -= amount
                    users_accounts[to_account_number]["balance"] += amount
                    print(
                        f"transformation process succeed, your balance is {users_accounts[from_account_number]['balance']}")
                    start()
                else:
                    print(f"your balance is {users_accounts[from_account_number]['balance']}")
                    transfer()
            else:
                print("amount must be greater than 0")
                transfer()
        else:
            print("Account not found")
            transfer()
    else:
        print("Account not found")
        transfer()


if __name__ == '__main__':
    users_accounts = {
        116000: {"user name" :"test account", "password": "hasan12345", "balance": 0}
    }
    start()
