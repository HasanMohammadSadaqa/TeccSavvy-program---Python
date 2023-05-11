"""
a Python program to create a list of squares of all even numbers in a given list using list comprehensions.
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [i ** 2 for i in lst if i % 2 == 0]
print(squares)
