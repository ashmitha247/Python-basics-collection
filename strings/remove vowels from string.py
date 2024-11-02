# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Define the vowels
vowels = "aeiouAEIOU"

# Initialize an empty string to hold the modified string
modified_string = ""

# Iterate through each character in the input string
for char in input_string:
    # If the character is not a vowel, add it to the modified string
    if char not in vowels:
        modified_string += char

# Print the modified string
print("Modified string (without vowels):", modified_string)

'''
if char not in vowels:
        modified_string += char

If the character is not a vowel (i.e., the condition is true),
this line appends (+=) the character to the modified_string. '''