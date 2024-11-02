# Get custom names input from the user
'''names_input = input("Enter names separated by commas: ")

# Split the input string into a list of names and strip any extra whitespace
names_list = [name.strip() for name in names_input.split(',')]'''

names_list = list(map(str,input("Enter names: ").split()))

# Define a set of vowels
vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}

# Initialize a counter
count = 0

# Count names that start with a vowel
for item in names_list:
    if item and item[0] in vowels:  # Check if the name is not empty and starts with a vowel
        count += 1

# Print the result
print(f"Number of names that start with a vowel: {count}")


'''  if item 
    This line checks if item is truthy. If item is not empty (i.e., it contains some value), the code inside the if block will execute. 
    If item is empty or evaluates to False, the code inside the block will be skipped.'''