list = [1, 2, 3, 4, 5, 6, 7, 8, 9,"k"]
summation = 0
for num in list:
    if type(num) == int:
        summation += num
    else:
        pass
print(f"the summation of {list} is {summation}")

# second method
# Sum = sum(list)
# print(f"the summation of {list} is {Sum}")
