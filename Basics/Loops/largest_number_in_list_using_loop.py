list = list(range(1, 11))
max_number = list[1]
for i in list:
    if i > max_number:
        max_number = i
print(f"the largest number of this list {list} is: {max_number}")
