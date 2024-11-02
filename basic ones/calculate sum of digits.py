# Input from the user
number = int(input("Enter a number: "))

# Initialize the sum variable
sum_of_digits = 0

# Convert the number to its absolute value (to handle negative numbers)
number = abs(number)

# Loop to calculate the sum of digits
while number > 0:
    digit = number % 10  # Get the last digit
    sum_of_digits += digit  # Add the digit to the sum
    number //= 10  # Remove the last digit from the number

# Print the result
print("The sum of the digits is:", sum_of_digits)

'''output:
Enter a number: 78
The sum of the digits is: 15'''