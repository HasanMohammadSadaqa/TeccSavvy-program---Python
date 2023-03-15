"""
this program prompt the user to enter a specific length for a password and print random password with that length
"""
import random
import string
import sys


def string_random_password(length):
    """

    :param length: length of a password
    :return: (string) random integer password
    """
    return random.choices(string.ascii_letters, k=length)

def integer_random_password(length):
    range_start = 10**(length-1)
    end_range = (10**length)-1
    return random.randint(range_start, end_range)
while True:
    try:
        type_of_password = input("what you type of password you want(string/integer)? ")
        if type_of_password.lower() == "string":
            try:
                length = int(input("enter the length you want: "))
                print("".join(string_random_password(length)))
                break
            except ValueError:
                print("Invalid input, please try again")
        elif type_of_password.lower() == "integer":
            length = int(input("enter the length you want: "))
            print(integer_random_password(length))
            break
        else:
            print("please write string or integer")
    except ValueError:
        sys.exit("thanks for using the program")

