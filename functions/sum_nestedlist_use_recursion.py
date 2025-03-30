'''
Write a Python program to find sum of elements of nested list using recursion.
Ex:

Input String: [9, 1, [3,4], [5,2]]

Output: 24  '''

def sum_of_nestedlist(list1):
  sum=0
  for item in list1:
    if isinstance (item, list):
      sum+=sum_of_nestedlist(item)
    else:
      sum+=item
  return sum

list1 = eval(input("Enter a nested list: "))
total_sum = sum_of_nestedlist(list1)
print("Sum of elements:", total_sum)

'''
The isinstance() function in Python is used to check if an object is an instance of a particular class or a subclass of that class.

Syntax:
isinstance(object, classinfo)

if isinstance(i, list):
Checks if the current element i is itself a list.
If i is a list, it means we've encountered a nested list. '''