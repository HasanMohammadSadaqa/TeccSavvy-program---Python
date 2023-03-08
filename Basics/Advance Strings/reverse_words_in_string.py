str = input("please enter a string to reverse the words: ").split()
if " " in str:
    str = str[::-1]
    str = " ".join(str)
    print(f"the reversed string is: {str}")
else:
    print(f"the string is {str[0]} \n note that the string must have more than word to be reversed ")
