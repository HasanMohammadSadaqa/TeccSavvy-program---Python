str = input("please enter a string to reverse the words: ")
if " " in str:
    new_str = str.split()
    new_str = new_str[::-1]
    # new_str = " ".join(str)
    print(f"the reversed string is: {new_str}")
else:
    print("note that the string must have more than word to be reversed ")
