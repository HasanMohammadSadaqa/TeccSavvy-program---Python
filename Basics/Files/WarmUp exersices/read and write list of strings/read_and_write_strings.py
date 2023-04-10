"""This task to Write a Python program to read a list of strings from a text file, sort the strings in alphabetical
order, and write the sorted list of strings to another text file."""


def read_and_write_strings():
    with open("oldest_strings.txt", "r") as f:
        list_of_strings = [line.strip() for line in f.readlines()]
        list_of_strings.sort()
    with open("newest_strings.txt", "w") as file:
        for line in list_of_strings:
            file.write(line + "\n")


if __name__ == '__main__':
    read_and_write_strings()
