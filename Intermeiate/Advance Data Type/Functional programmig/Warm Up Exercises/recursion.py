def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
