# Write a program to remove all vowels from a string.
string = input("Enter a string please: ")
vowels = "aeiouAEIOU"
string_without_vowels = ""
for char in string:
    if char not in vowels:
        string_without_vowels += char
print(f"The String without vowels is: {string_without_vowels}")


# another solution
# string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# string_without_vowels = "".join([character for character in string if character not in vowels])
# print("The string without vowels is", string_without_vowels)

