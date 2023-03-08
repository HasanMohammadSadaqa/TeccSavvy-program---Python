# Write a program to sort a list of strings by the length of each string.
strings = input("write a group of strings: ").split()
sorted_strings = sorted(strings, key=len, reverse=True)
print(f"The sorted list of your sting is:\n {sorted_strings}")

# Explain for sorted() function
# sorted(iterable, key=key, reverse=reverse)
# Parameter   Description
# iterable	    Required. The sequence to sort, list, dictionary, tuple etc.
# key	        Optional. A Function to execute to decide the order. Default is None
# reverse	    Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
