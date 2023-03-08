# Write a program to find the key with the maximum value in a dictionary.
dict = {"first": 1, "second": 2, "third": 10, "fourth": 52}
max_value = 0
for val in dict.values():
    if val > max_value:
        max_value = val
key_with_max_value = list(dict.keys())[list(dict.values()).index(max_value)]
print(f"The key with maximum value is: {key_with_max_value}")

# another solution
# dictionary = {"a": 10, "b": 5, "c": 15}
# max_key = max(dictionary, key=dictionary.get)
# print("The key with the maximum value in the dictionary is", max_key)