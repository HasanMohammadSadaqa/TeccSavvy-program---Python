# Count the number of occurrences of each word in a string.


string = input("Please enter a string: ")

# create an empty dictionary to store word counts
word_counts = {}

# split the string into words
words = string.split()

# loop through the words
for word in words:
    # if the word is already in the dictionary, increment its count
    if word in word_counts:
         word_counts[word] += 1
    # if the word is not in the dictionary, add it with a count of 1
    else:
        word_counts[word] = 1

# return the dictionary of word counts
print(f"Here is the number of occurrence of each word in your string: \n {word_counts}")
