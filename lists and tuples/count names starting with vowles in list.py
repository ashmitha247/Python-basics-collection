# Get custom names input from the user
names_list = input("Enter names: ").split()  # No need for map here

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