list1 = [1, 2, 3]
list2 = [4, 5, 6]

concatenated_list = list1 + list2
print(f"{list1}\n{list2}\nconcatenated_list is {concatenated_list}")

# second method (better than first one)
list1.extend(list2)
print(list1)
# set(list2)
print(set(list2))

