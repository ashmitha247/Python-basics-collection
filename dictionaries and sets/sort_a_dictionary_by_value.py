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
it returns a view of the dictionary's items (key-value pairs) as tuples. Each tuple contains a key and its corresponding value.'''