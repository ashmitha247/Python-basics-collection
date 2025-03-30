# Write a Python program to add an item in a tuple without converting into a list.
#you dont directly "enter" a tuple, you enter a strin,split and strip it,ans then convert it to tuple.
# Input a tuple of items (space-separated)
input_string = input("Enter a tuple of items (space-separated): ")
# Split the input string into a list of items, removing any surrounding whitespace
k = tuple(item.strip() for item in input_string.split())

# Input the type of the new item
item_type = input("Enter the type of the item to add (int, float, str): ").strip().lower()
new_item = input("Enter the item to add to the tuple: ")

# Convert the new item based on the specified type
if item_type == 'int':
    new_item = int(new_item)
elif item_type == 'float':
    new_item = float(new_item)
# If the type is 'str', we don't need to convert it

# Add the new item to the tuple
k = k + (new_item,)

# Print the updated tuple
print(f"Updated Tuple: {k}")

'''
Creating a New Tuple with One Item:

The expression (new_item,) creates a new tuple containing a single element, new_item.
The comma after new_item is crucial; it tells Python that this is a tuple with one item.
Without the comma, Python would interpret it as just a parenthesized expression, not a tuple.

If you try to execute the expression (1, 2, 3) + (4) in Python, you will encounter a TypeError.
This is because (4) is not recognized as a tuple; it is treated as just the integer 4 due to the absence of a comma.

Explanation
Tuple Definition:

A tuple with a single element must have a trailing comma.
For example, (4,) is a tuple containing one element, while (4) is just the integer 4 enclosed in parentheses.
Concatenation:

When you write (1, 2, 3) + (4), Python interprets this as trying to add a tuple (1, 2, 3) to an integer 4, which is not allowed.
Tuples can only be concatenated with other tuples.

# Correct way to add an integer to a tuple
result = (1, 2, 3) + (4,)  # This works
print(result)  # Output: (1, 2, 3, 4) '''