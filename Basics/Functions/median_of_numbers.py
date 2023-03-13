def median_of_numbers(list):
    sorted_list = sorted(list)
    median = 0
    length = len(sorted_list)
    if length % 2 != 0:
        median = sorted_list[(length - 1) // 2]
    if length % 2 == 0:
        median = (sorted_list[(length // 2) - 1] + sorted_list[length // 2]) / 2
    return median


print(median_of_numbers([1, 4, 2, 5, 0]))

print(median_of_numbers([10, 40, 20, 50]))
