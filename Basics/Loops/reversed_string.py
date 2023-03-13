string = input("please enter a string to reverse: ")
reversed_string = ""
count = len(string)
while count > 0:
    reversed_string +=string[count-1]
    count -=1
print(f"the reversed string is: {reversed_string}")

# second method
# for i in reversed(range(0, len(string))):
#     reversed_string +=string[i]
# print(f"the reversed string is: {reversed_string}")


