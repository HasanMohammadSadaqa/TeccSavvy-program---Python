# Write a program to find the most common character in a string.
# for this exercise I want to use dictionary,
# where I want to put the character  as key and the number of appearance as value
string = input("Please enter a string: ")
count ={}

# Iterate through each character in the string
for char in string:
    # If the character is already in the dictionary, increment its count
    if char in count:
        count[char] += 1
    # Otherwise, add it to the dictionary with a count of 1
    else:
        count[char] = 1
# Find the most common character by iterating through the dictionary
max_count = 0
most_common = ''
for char in count:
    if count[char] > max_count:
        max_count = count[char]
        most_common = char
print(f"the most common character is '{most_common}' with a count of {max_count}")