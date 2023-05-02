"""this is a simple bank account that aim to create a bank account class has two attribute and two method,
applying encapsulation concept in oop"""
import sys


class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    # Getter and Setter
    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        """
        :param amount: amount the owner want to add to his balance
        :return: new balance
        """
        if amount < 0:
            print("amount must be greater than 0")
        else:
            self.__balance += amount
            print(f"Amount was added successfully, your balance is: {self.get_balance()}")

    def withdrew(self, amount):
        """
        :param amount: amount the owner want to withdraw from balance
        :return: new balance
        """
        if amount > self.get_balance():
            print(f"your balance is: {self.get_balance()}")
        elif amount < 0:
            print("Amount must be greater than 0")
        else:
            self.__balance -= amount
            print(f"Amount withdrawn successfully, your balance is: {self.get_balance()}")


if __name__ == "__main__":
    operation_list = {
        1: "Create account",
        2: "Deposit",
        3: "Withdrew",
        4: "LogOut"
    }
    print("Welcome to our system, you can: ")
    for operation in operation_list.items():
        print(f"{operation[0]}) {operation[1]}")
    while True:
        try:
            operation_number = int(input("Select from the list: "))
            if operation_number < 1 or operation_number > 4:
                print("Please select number from the list")
                print("_______________________________________")
            if operation_number == 1:
                name = input("Enter your name: ")
                account1 = BankAccount(name)
                print("Account created successfully")
                print("_______________________________")
            if operation_number == 2:
                amount_to_add = int(input("Enter amount to deposit: "))
                account1.deposit(amount_to_add)
                print("________________________________")
            if operation_number == 3:
                amount_to_withdraw = int(input("Enter amount to withdraw: "))
                account1.withdrew(amount_to_withdraw)
                print("______________________________")
            if operation_number == 4:
                sys.exit("Thanks to use our system")
        except ValueError:
            print("You have to choose number from the list ex: 1")
            print("________________________________________")
