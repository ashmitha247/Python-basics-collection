#pangram - A pangram is a sentence using every letter of the alphabet at least once

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

''' You can use either set('abcdefghijklmnopqrstuvwxyz') or { 'a', 'b', 'c', ..., 'z' } to create a set of the English alphabet.
Both methods are valid, but using curly braces is often more concise and readable for small sets.

The set() function takes the string and creates a set of unique characters found in that string. For example,
if the input string is "The quick brown fox",
input_set would contain the characters {'t', 'h', 'e', ' ', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x'}. '''