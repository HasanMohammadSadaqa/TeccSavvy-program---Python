"""
this code aims to apply map function on a list of int the return a list of square of that int
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = list(map(lambda x: x ** 2, lst))
print(squares)
