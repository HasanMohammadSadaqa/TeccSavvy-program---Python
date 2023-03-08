from collections import Counter

string = input("please enter a string: ").split()
frequency_word = Counter(string)
print(frequency_word)