# Write a program to generate the Fibonacci sequence up to a given number.
num = int(input("please enter a number: "))
fib = [0, 1]
while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])
print(f"the fibonacci of {num} is \n {fib}")


# another solution
# num = int(input("Enter a number: "))
# def fibonacci(num):
#     if num <= 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
#
#
# print(fibonacci(num))