list = [1, 5, 6, 115, 30, -110]
max_num = max(list)
min_num = min(list)
print(f"{list}\nmaximum number is: {max_num}\nminimum number is: {min_num}")

# second method
# max_number = list[0]
# min_number = list[-1]
# for num in list:
#     if num > max_number:
#         max_number = num
#     if num < min_number:
#         min_number = num
# print(f"{list}\nmaximum number is: {max_num}\nminimum number is: {min_num}")

# third method if the list has element not numbers
# list1 = [True, "Hasan", 1,2,3,4,5,6,7,8,9]
# new_list = []
# for item in list1:
#     if type(item) == int:
#         new_list.append(item)
# max_number = max(new_list)
# min_number = min(new_list)
# print(max_number, min_number)