def filter_word_lengths(words, min_length):
    lengths = map(len, words)
    filtered_lengths = filter(lambda x: x >= min_length, lengths)
    return list(filtered_lengths)


words = ['apple', 'banana', 'grapefruit', 'kiwi', 'pear']
min_length = 5
result = filter_word_lengths(words, min_length)
print(result)
