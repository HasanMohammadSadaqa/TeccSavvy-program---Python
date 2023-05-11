def square(num):
    return num ** 2


def squares_of_numbers(lst, function):
    result = []
    for num in lst:
        new_num = function(num)
        result.append(new_num)
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(squares_of_numbers(numbers, square))
