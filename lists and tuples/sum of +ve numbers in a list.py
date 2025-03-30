# Prompt the user to enter a list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Initialize the sum variable
sum_of_positive_numbers = 0

# Iterate through the list
for item in numbers:
    if item> 0:  # Check if the number is positive
        sum_of_positive_numbers += item  # Add to the sum

# Print the result
print("The sum of all positive numbers is:", sum_of_positive_numbers)

'''output:
            Enter a list of numbers separated by spaces: 4 -9 8 -4 7
The sum of all positive numbers is: 19 '''