import factorial_of_n

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    from factorial_of_n import calc_fact

# Example usage
number = int(input("Enter a number to calculate its factorial: "))
#result = calculate_factorial(number)
print(f"The factorial of {number} is {factorial_of_n.calc_fact}")