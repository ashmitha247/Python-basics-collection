#Write a Python program to get a list of even numbers from a given list of numbers. (use only list comprehensions).

l = list(input("Enter a list of numbers: ").split())
even = [int(item) for item in l if int(item)%2==0]
print(f"Even numbers: {even}")

