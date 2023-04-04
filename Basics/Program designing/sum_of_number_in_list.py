# This program reads a list of integers and returns the sum
def summation_of_numbers(nums):
    """
    :param nums: (list) list of numbers to add
    :return: (int) the summation of the numbers in list
    """
    return sum(nums)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(f"The total is: {summation_of_numbers(numbers)}")
