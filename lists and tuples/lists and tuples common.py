#common approach for creating a list and a tuple:

#LIST:

# Step 1: Prompt the user for input
input_string = input("Enter a list of items (space-separated): ")

# Step 2: Split the input string into a list of items, removing any surrounding whitespace
# Step 3: Strip whitespace and create a list
k = [item.strip() for item in input_string.split()]
# Optional: Print the resulting list
print("The resulting list is:", k)


#split() creates list so u dont need to use list() but for tuples you gotta use tuple()

#TUPLE:

# Step 1: Prompt the user for input
input_string = input("Enter a tuple of items (space-separated): ")

# Step 2: Split the input string into a list of items, removing any surrounding whitespace
# Step 3: Strip whitespace and convert to tuple
k = tuple(item.strip() for item in input_string.split())

# Optional: Print the resulting tuple
print("The resulting tuple is:", k)
