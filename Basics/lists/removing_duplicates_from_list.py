list = input("enter the items of a list: ").split()
new_list =[]
for item in list:
    if item not in new_list:
        new_list.append(item)
print(new_list)