'''Write a Python program to find N largest element from given list of integers using functions.

Test case 1:
Enter·a·list·of·integers·(space-separated):·1 2 3 4 5	
Enter·the·value·of·N:·3	
N·largest·elements:·[5,·4,·3]⏎'''


# Input a list of integers from the user
a = list(map(int, input("Enter a list of integers (space-separated): ").split()))

# Input the value of N
b = int(input("Enter the value of N: "))

# Function to find the N largest elements
def largest_n(a, b):
    a.sort()          # Sort the list in ascending order
    a.reverse()       # Reverse the list to get descending order
    c = a[:b]         # Get the first b elements (N largest)
    return c          # Return the N largest elements

# Call the function and store the result
r = largest_n(a, b)

# Print the N largest elements
print("N largest elements:", r)