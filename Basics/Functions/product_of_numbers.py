def product_of_numbers(list):
    product = 1
    for num in list:
        product = product * num
    return product


print(product_of_numbers([1, 2, 3, 4, 5, 6]))
