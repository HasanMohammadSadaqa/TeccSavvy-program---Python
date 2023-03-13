string = input("please enter a sentence: ")
count = 1
for i in string:
    if i == " ":
        count +=1
print(count)



# second method
# string = input("please enter a sentence: ").split()
# print(len(string))