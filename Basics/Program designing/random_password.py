"""
this program prompt the user to enter a specific length for a password and print random password with that length
"""
import random
import string


def random_password(length):
    """

    :param length: length of a password
    :return: (string) random integer password
    """
    return random.choices(string.ascii_letters, k=length)


while True:
    try:
        length = int(input("enter the length you want: "))
        print("".join(random_password(length)))
    except ValueError:
        print("Invalid input, please try again")
