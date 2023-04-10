"""
This task is a reading integer from the text files and return the sum of these numbers
"""


def summation_of_numbers():
    """
    :return: summation of a numbers from a file
    """
    with open("Integers.txt", "r") as f:
        num_list = []
        for line in f.readlines():
            num_list.append(int(line.strip()))
    print(f"The summation of the integers is: {sum(num_list)}")


if __name__ == '__main__':
    summation_of_numbers()
