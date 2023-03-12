numbers = list(range(1,11))
even_numbers =[]
for num in numbers:
    if num %2 == 0:
        even_numbers.append(num)
print(even_numbers)