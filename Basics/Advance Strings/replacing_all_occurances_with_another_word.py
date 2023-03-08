# str = input("please enter a string: ")
# def replace_word(string, old_word, new_word):
#     # split the string into words
#     words = string.split()
#
#     # loop through the words
#     for i in range(len(words)):
#         # if the current word matches the old word, replace it with the new word
#         if words[i] == old_word:
#             words[i] = new_word
#
#     # join the words back together into a string and return it
#     return ' '.join(words)
# old_word = input("please enter the word you want to replace: ")
# while old_word not in str:
#         old_word = input("please enter an exist word: ")
#
# new_word = input("please enter new word: ")
# print("the new string is: ", replace_word(str, old_word, new_word))


# another solution
str = input("please enter a string: ")
words = str.split()
old_word = input("please enter the word you want to replace: ")
while old_word not in str:
    old_word = input("please enter an exist word: ")
new_word = input("please enter new word: ")
new_string = str.replace(old_word, new_word)
print(f"the new string is: {new_string}")