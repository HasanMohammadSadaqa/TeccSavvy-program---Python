"""
this is a program that prompts the user to enter a list of numbers
and return sum, mean, standard deviation of the numbers
"""
import math


def summation(numbers):
    """
    :param numbers: (list): a list of numbers to sum
    :return: (int): the sum of a numbers in a list
    """
    return sum(numbers)


def mean(numbers):
    """
    :param numbers: list of numbers to calculate the mean
    :return: (float) the mean of numbers in a list
    """
    return summation(numbers) / len(numbers)


def standard_deviation(numbers):
    """
    :param numbers: list of numbers to calculate the standard deviation
    :return:(float) standard deviation of a numbers in a list
    """
    return math.sqrt(sum([((x - mean(numbers)) ** 2) for x in numbers]) / len(numbers))


if __name__ == '__main__':
    """
 first of all prompts the user to enter a list of numbers (there is two methods to do this
 I will use the first method and put the second in comment)

 """
    # first method
valid_input = False
while not valid_input:
    user_input = input("please enter as list of numbers, separated by commas: ")
    num_list = user_input.split(",")
    number_list = []

    if len(num_list) == 0:
        print("Error: list can not empty")
    for num in num_list:
        try:
            number_list.append(float(num))

        except ValueError:
            print(f"Error: list must contains only numbers")
            break
    else:
        valid_input = True
print(f"the sum of the numbers is: {summation(number_list)}")
print(f"the mean of the numbers is: {mean(number_list)}")
print(f"the standard deviation of the numbers is: {standard_deviation(number_list)}")



#     second method for input validation of a list (using built-in functions):
# while True:
#     user_input = input("Enter a list of numbers, separated by commas: ")
#     num_list = list(map(float, user_input.split(",")))
#     if len(num_list) == 0:
#         print("Error: list can not be empty")
#     elif not all(isinstance(num, (int, float)) for num in num_list):
#         print("Error: list must contain only numbers")
#     else:
#         break