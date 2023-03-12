list = [1,2,3,4,5,6,7,9]
# method 1
list1 = list[0:3]
list2 = list[3:]
print(f"{list} ======== {list1}, {list2} ")

# method two but it split the list into threes
split_size = 3
splitted_list = [list[i:i+split_size] for i in range(0, len(list), split_size)]
print(splitted_list)