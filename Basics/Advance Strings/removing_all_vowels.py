string = input("Enter a string: ")
vowels = "aeiouAEIOU"
string_without_vowels = "".join([character for character in string if character not in vowels])
print("The string without vowels is", string_without_vowels)
