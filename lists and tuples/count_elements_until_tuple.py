#Write a Python program to count the elements in a list until an element is a tuple.

l = list(map(int,input("Enter a list of elements, separated by spaces: ").strip().split()))
count = 0

for i in l:
    if i is tuple:
        break
    count+=1
print(f"Count of elements before encountering a tuple: {count}")






