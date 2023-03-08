string = input("please enter a string to check: ")
while string == string[::-1]:
    print("the string is palindrome")
    break
else:
    print("the string is not palindrome")