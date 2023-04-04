"""
this program prompt the user to enter a specific length for a password and print random password with that length
"""
import random
import string
import sys


def string_random_password(length):
    """
    :param length: length of a password
    :return: (list) list of random characters
    """
    return random.choices(string.ascii_letters, k=length // 2)


def integer_random_password(length):
    """
    :param length (int): length of password
    :return: (int) : random integer
    """
    range_start = 10 ** ((length // 2) - 1)
    end_range = (10 ** (length // 2)) - 1
    return random.randint(range_start, end_range)


# while True:
#     try:
#         type_of_password = input("what you type of password you want(string/integer)? ")
#         if type_of_password.lower() == "string":
#             try:
#                 length = int(input("enter the length you want: "))
#                 print("".join(string_random_password(length)))
#                 break
#             except ValueError:
#                 print("Invalid input, please try again")
#         elif type_of_password.lower() == "integer":
#             length = int(input("enter the length you want: "))
#             print(integer_random_password(length))
#             break
#         else:
#             print("please write string or integer")
#     except ValueError:
#         sys.exit("thanks for using the program")


if __name__ == '__main__':
    while True:
        try:
            length = int(input("please enter a length: "))

            # validation for length inputs
            if length < 3:
                print("Length of password must be at least 8 characters")
            else:
                password = "".join(string_random_password(length)) + str(integer_random_password(length))
                shuffled_password = "".join(random.sample(password, len(password)))
                print(shuffled_password)

        except ValueError:
            print("the length must be numbers")


