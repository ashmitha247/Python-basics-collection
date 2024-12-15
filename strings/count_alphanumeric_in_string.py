#Write a loop that counts the number of alphanumeric characters (letters or digits)
# that appear in the string referenced by mystring.

'''
The goal is to iterate through each character in the string "mystring" and
count how many of those characters are alphanumeric. Alphanumeric characters include:

Letters (both uppercase and lowercase, e.g., 'A', 'b', 'Z')
Digits (e.g., '0', '1', '9') '''



mystring = input("Enter string: ")
count = 0  # Step 1: Initialize the counter

# Step 2: Iterate through each character in the string
for char in mystring:
    # Step 3: Check if the character is alphanumeric
    if char.isalnum():
        count += 1  # Step 4: Increment the counter if it is alphanumeric

# Step 5: Print the result
print(f"Number of alphanumeric characters: {count}")

''' .isalnum() -> For each character,it checks if it is alphanumeric using the isalnum() method,
which returns True if the character is a letter or a digit. '''

''' 
output:
Enter string: hii! how r u 178??
Number of alphanumeric characters: 11  '''