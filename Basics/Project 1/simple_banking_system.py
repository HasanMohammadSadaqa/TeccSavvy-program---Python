# first of all the user should create his account
users_accounts = {}
print("create new account")
user_name = input("User Name: ")
password = input("Password: ")
account_number = len(users_accounts) + 1
users_accounts[account_number] = {'user name': user_name, "password": password, "balance": 1000}

if account_number in users_accounts:
    print(f"welcome {user_name}!.\nHere yo can 1)Deposit 2)Withdrew 3)Checking your balance 4)transfer funds "
          "for another account")
else:
    print(f"Error, please try again!")


# methods for each operation
# making deposit
def deposit(amount):
    if amount > 0:
        users_accounts[account_number]["balance"] += amount
        print(f"Deposit successful. New balance: {users_accounts[account_number]['balance']}")
    else:
        print("please enter a valid amount ")


# making withdrew:
def withdrew(amount):
    if amount <= users_accounts[account_number]["balance"]:
        users_accounts[account_number]["balance"] -= amount
        print(f"Withdrawal successful. New balance:{users_accounts[account_number]['balance']}")
    else:
        print("Insufficient funds.")


# check the balance
def check_the_balance():
    print(f"current balance: {users_accounts[account_number]['balance']}")


def transfer_a_balance(amount):
    print("create a new account to test this case: ")
    user_name2 = input("User Name: ")
    password2 = input("Password: ")
    account_number2 = len(users_accounts) + 1
    users_accounts[account_number2] = {"user name": user_name2, "password": password2, "balance": 1000}
    if amount > 0:
        if amount <= users_accounts[account_number]["balance"]:
            users_accounts[account_number]["balance"] -= amount
            users_accounts[account_number2]['balance'] += amount
            print(
                f"Transfer successful. New balances:\naccount {account_number}: {users_accounts[account_number]['balance']}\n"
                f"account {account_number2}: {users_accounts[account_number2]['balance']}")
        else:
            print("please enter a valid value")


operation = int(input("please drop the number of operation you want: "))
if operation == 1:
    print(f"Current balance is: {users_accounts[account_number]['balance']}")
    amount = float(input("How much you want to deposit: "))
    deposit(amount)
    # print("\nDo you want to do another operation?")


elif operation == 2:
    print(f"Current balance is: {users_accounts[account_number]['balance']}")
    amount = float(input("How much you want to withdrew: "))
    withdrew(amount)
elif operation == 3:
    check_the_balance()
elif operation == 4:
    print(f"Current balance is: {users_accounts[account_number]['balance']}")
    amount = float(input("How much you want to transfer: "))
    transfer_a_balance(amount)
else:
    print("Kindly, enter a valid operation number")
