# Write a program to count the frequency of words in a given string and store the results in a dictionary.
words = input("Enter a string please: ").split()
count={}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(f"The frequency of words in the string is: {count}")