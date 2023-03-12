list = [1,2,3,4,5,6]
new_list = []
for num in list:
    if num < max(list):
        new_list.append(num)
print(f"the second largest number of the array: {list} is: {max(new_list)}")

# second method (the best)
# list.sort(reverse=True)
# second_largest_number = list[1]
# print(f"the second largest number of the array: {list} is: {second_largest_number}")