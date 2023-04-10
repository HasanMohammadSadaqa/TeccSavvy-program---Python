"""
This task to Write a Python program to count the number of words in a text file and display the count on the console.
"""
def count_number_of_words():
    with open("words.txt", "r") as file:
        words = file.read().split()
        alphabetic_words = []
        for word in words:
            if word.isalpha():
                alphabetic_words.append(word)
    return len(alphabetic_words)


print(count_number_of_words())
