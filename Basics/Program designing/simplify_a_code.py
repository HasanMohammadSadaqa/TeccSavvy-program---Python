# Given a list of strings, create a new list with the first letter of each string capitalized
words = ['apple', 'banana', 'cherry']

new_words = [word.capitalize()[0] for word in words]

print(new_words)