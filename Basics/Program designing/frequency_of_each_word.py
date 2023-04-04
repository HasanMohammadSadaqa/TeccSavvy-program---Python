"""
This is a program that reads a text and return the frequency of each word in the text
"""


def frequency_words(text):
    """
    :param text: (list) list of words in the text i want to check separated by space
    :return: (dictionary) contains frequency of each word
    """
    words_frequency = {}
    for word in text:
        if word in words_frequency:
            words_frequency[word] += 1
        else:
            words_frequency[word] = 1
    return words_frequency


if __name__ == '__main__':
    while True:
        text_input = input("Please enter a text").split()
        for word_frequency in frequency_words(text_input).items():
            print(f"{word_frequency[0]} - {word_frequency[1]}")
        break
