# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Normalize the string to lowercase
input_string = input_string.lower()

# Create a set of all letters in the English alphabet
alphabet_set = set('abcdefghijklmnopqrstuvwxyz')

# Create a set of characters from the input string
input_set = set(input_string)

# Check if all alphabet letters are in the input set
if alphabet_set.issubset(input_set):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")