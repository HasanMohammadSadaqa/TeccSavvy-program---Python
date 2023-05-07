"""this program aim to use oop pillars to create simple bank account system, 2 types of classes generally,
firstly: Account class that contain attributes and method and inherits 3 type of account,secondly: Bank class that
manage all accounts"""


class Account:
    def __init__(self, account_number, owner_name, balance=0):
        self.__account_number = account_number
        self.__name = owner_name
        self.__balance = balance

    # Getter
    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def deposit(self, amount):
        self.__balance += amount


class CheckingAccount(Account):
    def __init__(self, account_number, owner_name, balance=0):
        super().__init__(account_number, owner_name, balance)

    def withdrew(self, amount):
        account_balance = self.get_balance()
        print(account_balance)
        if amount > self.get_balance():
            print(f"Amount greater than your balance, your balance is: {account_balance}")
        elif amount < 0:
            print("Amount must be greater than 0")
        else:
            account_balance -= amount
            print("Withdrawn successfully!")
        return account_balance


class SavingAccount(Account):
    def __init__(self, account_number, owner_name, balance=0):
        super().__init__(account_number, owner_name, balance)

    def calculate_interest(self):
        interest_rate = 0.05
        account_balance = self.get_balance()
        interest = account_balance * interest_rate
        account_balance += interest
        print(f"the interest earned on the account balance: {interest}")


class BusinessAccount(Account):
    def __init__(self, account_number, owner_name, balance=0, employees=[]):
        super().__init__(account_number, owner_name, balance)
        self.__employees = employees

    def get_employees(self):
        return self.__employees

    def add_employee(self, employee_name):
        self.__employees.append(employee_name)


class Bank:
    def __init__(self):
        self.__accounts = []

    def get_accounts(self):
        return self.__accounts

    def create_account(self, account_type, account_number, owner_name, balance=0):
        if account_type.lower() == "checking":
            account = CheckingAccount(account_number, owner_name, balance)
        elif account_type.lower() == "saving":
            account = SavingAccount(account_number, owner_name, balance)
        elif account_type.lower() == "business":
            account = BusinessAccount(account_number, owner_name, balance)
        else:
            print("Invalid account type")
            return
        self.__accounts.append(account)
        print("Account created!")

    def delete_account(self, account_number):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                self.__accounts.remove(account)
                print("Account deleted!")
            else:
                print("Account not found")

    def view_all_account(self):
        if len(self.__accounts) > 0:
            for account in self.__accounts:
                print(f"{self.__accounts.index(account) + 1}) Account number: {account.get_account_number()}, Owner "
                      f"name: {account.get_name()}. Balance: {account.get_balance()}")
        else:
            print("No accounts yet!")
            print("__________________________")

    def search_account(self, account_number) :
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                print(f"Account number: {account.get_account_number()}")
                print(f"Owner name: {account.get_name()}")
                print(f"Balance: {account.get_balance()}")


if __name__ == "__main__":
    bank = Bank()
    bank.create_account("Checking", "001", "John Doe", 5000)
    bank.create_account("Saving", "002", "Jane Doe", 50000)
    bank.create_account("Business", "003", "Acme Inc.", 100000)

    # View all accounts:
    bank.view_all_account()

    # search for account:
    bank.search_account("002")

    # withdraw from a checking account:
    checking_account = bank.get_accounts()[0]
    checking_account.withdrew(1000)

    # Calculate interest for a savings account
    savings_account = bank.get_accounts()[1]
    savings_account.calculate_interest()

    # Add an employee to a business account
    business_account = bank.get_accounts()[2]
    business_account.add_employee("Bob Smith")

    # Delete an account
    bank.delete_account("001")





    # operation_list = {
    #     1: "Create account",
    #     2: "Search for account",
    #     3: "View all accounts",
    #     4: "Delete account"
    # }
    # print("Welcome to our system, you can: ")
    # for operation in operation_list.items():
    #     print(f"{operation[0]}) {operation[1]}")
    # while True:
    #     try:
    #         operation_number = int(input("Select a number from the list: "))
    #         if operation_number < 1 or operation_number > 4:
    #             print("Select number from the list")
    #             print("______________________________")
    #         if operation_number == 1:
    #             account_type = input("Enter account type: ")
    #             account_number = input("Enter account number: ")
    #             name = input("Enter your name: ")
    #             balance = int(input("Enter balance: "))
    #             bank.create_account(account_type, account_number, name, balance)
    #             print("_______________________________")
    #         if operation_number == 2:
    #             account_number = input("Enter account number to search: ")
    #             bank.search_account(account_number)
    #             print("______________________________")
    #         if operation_number == 3:
    #             bank.view_all_account()
    #             print("________________________________")
    #         if operation_number == 4:
    #             account_number = input("Enter account number to delete: ")
    #             bank.delete_account(account_number)
    #
    #     except ValueError:
    #         print("Please select number from the list ex: 1")
    #         print("_____________________________")
