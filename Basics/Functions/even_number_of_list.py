def even_number(list):
    even_number_list = []
    for num in list:
        if num % 2 == 0:
            even_number_list.append(num)
    return even_number_list


print(even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
