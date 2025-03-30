# Write a Python program to count the elements in a list until an element is a tuple.

# Get input from the user and split it into a list of strings using commas
elements = input("Enter the content of the list (use parentheses for tuples, e.g., (1, 2)): ").split(',')

count = 0

# Count elements until a tuple is found
for item in elements:
    # Check if the item is a tuple by evaluating its format
    if item.startswith('(') and item.endswith(')'):
        break  # Stop counting if a tuple is found
    count += 1  # Increment count for non-tuple elements

# Print the result
print(f"The number of elements until the element is a tuple is: {count}")