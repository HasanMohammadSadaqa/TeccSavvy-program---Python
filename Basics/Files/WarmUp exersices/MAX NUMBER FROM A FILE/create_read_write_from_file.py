"""This task to  create a new text file, write a list of integers to the file, and then read the contents of the file
and find the maximum integer in the list."""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
file_path = "numbers.txt"
with open(file_path, "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")
    print("Numbers have been written to the file.")
with open(file_path, "r") as read_file:
    list_of_numbers = [int(line.strip()) for line in read_file]
    print(f"The maximum number of the list is: {max(list_of_numbers)}")
