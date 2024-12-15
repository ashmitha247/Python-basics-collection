#Write a Python program to add an item in a tuple without converting into a list.

k = tuple(input("Enter a tuple of numbers (comma-separated):").split(","))
k = tuple(int(item) for item in k)

n = int(input("Enter an item to the tuple: "))
k = k+(n,)
updated_tuple = print(f"Updated Tuple: {k}")