number1 = float(input("please enter the first number: "))
operation = input("please enter the operation: ")
number2 = float(input("please enter the second number: "))
valid_operation = '+-*/'

while operation not in valid_operation:
    operation = input("Enter a valid operator (+, -, *, /): ")
else:
    if operation == '+':
        print("the result is: ", number1+number2)
    elif operation == '-':
        print("the result is: ", number1-number2)
    elif operation == '*':
        print("the result is: ", number1*number2)
    else:
        print("the result is: ", number1/number2)
