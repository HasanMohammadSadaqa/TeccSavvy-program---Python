string = input("please enter a sting: ")
vowels ="aeiouAEIOU"
number_of_vowels = 0
for char in string:
    if char in vowels:
        number_of_vowels +=1
print(f"the number of vowel is: {number_of_vowels}")