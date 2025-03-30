#Write a Python program to sort a dictionary by a value

n = int(input("Enter the number of elements in the dictionary: "))
d={}

for i in range (n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key]=value

sorted_dict= {k:v for k,v in sorted(d.items(),key=lambda item:item[1])}
print("Sorted dictionary: ")
for key,value in sorted_dict.items():
    print(f"{key}:{value}")

'''When you call d.items(), where d is a dictionary,
it returns a view of the dictionary's items (key-value pairs) as tuples. Each tuple contains a key and its corresponding values.

1. sorted(d.items(),key=lambda item:item[1]):

d.items(): This converts the dictionary d into a list of key-value pairs (tuples).
sorted(...): This function sorts the list of key-value pairs.
key=lambda item:item[1]: This specifies the sorting criteria.
It uses a lambda function to extract the second element (the value) of each key-value pair (item) for sorting.


2. {k:v for k,v in ...}:

This is a dictionary comprehension. It iterates over the sorted list of key-value pairs.

In this case, lambda item: item[1] means that for each item in the list, the function will return the value at index 1. '''