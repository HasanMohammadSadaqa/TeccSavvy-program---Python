numbers = list(range(1,11))
for num in numbers:
    if num %2 != 0:
        numbers.remove(num)
print(numbers)
