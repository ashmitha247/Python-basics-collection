#Assume each of the variables set1 and set2 references a set. Write code that creates another set containing
# only the elements that are found in both set1 and set2, and assigns the resulting set to the variable set3.


# Take user input for the first set
user_input1 = input("Enter elements for set1 (separated by spaces): ")
# Create set1 by splitting the input string and converting it to a set
set1 = set(user_input1.split())

# Take user input for the second set
user_input2 = input("Enter elements for set2 (separated by spaces): ")
# Create set2 by splitting the input string and converting it to a set
set2 = set(user_input2.split())

# Create a new set containing only the elements found in both set1 and set2
set3 = set1.intersection(set2)  # Using the intersection method

''' another way:

set3 = set1 & set2 '''

# Print the resulting set
print("The elements found in both sets are:", set3)