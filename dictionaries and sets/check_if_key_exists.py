#Write a python program to check whether the key 'James' exists in the dictionary.
#If so, display the value that is associated with that key. If the key is not in the dictionary, display a message indicating so.

'''
NOTE:

The while True: construct in Python is used to create an infinite loop.
This means that the loop will continue to execute indefinitely
until it is explicitly broken out of using a break statement or until the program is terminated.

In the context of the provided code,
while True: is used to repeatedly prompt the user for input until they indicate that they are done entering key-value pairs. '''


# Step 1: Initialize an empty dictionary
my_dict = {}

# Step 2: Get user input for key-value pairs
print("Enter key-value pairs for the dictionary (type 'done' when finished):")

while True:
    # Prompt the user for a key
    key = input("Enter key: ")
    if key.lower() == 'done':
        break  # Exit the loop if the user types 'done'
    
    # Prompt the user for a value
    value = input("Enter value: ")
    
    # Store the key-value pair in the dictionary
    my_dict[key] = value

# Step 3: Check if the key 'James' exists in the dictionary
if 'James' in my_dict:
    # Step 4: If it exists, display the associated value
    print("The value associated with 'James' is:", my_dict['James'])
else:
    # Step 5: If it does not exist, display a message
    print("The key 'James' does not exist in the dictionary.")
    