#Write a program that inputs a text file. The program should print all of the unique words in the file in alphabetical order

def uniquewords_in_file(file):
    try:
        with open(file,'r') as file:
            split_file = file.read().split()
            split_words = sorted(set(split_file))
            for i in split_words:
                print(f"{i}")
    except Exception as e:
        print(f"Error found: {e}")
file_name = input("Enter file name: ")
uniquewords_in_file(file_name)

#split_words.count(i) beside {i} if we also want the number
'''
set(splitted_file): This converts the list of words into a set,
which automatically removes any duplicate words, leaving only unique words.

The split() method then splits this string into a list of words based on whitespace (spaces, newlines, etc.).
The result is stored in the variable splitted_file.

**1. Function vs. Method**
sorted():

sorted() is a built-in function.
It can be used on any iterable (like lists, tuples, strings, etc.).
It returns a new sorted list from the elements of the iterable.
sort():

sort() is a method that is specific to list objects.
It can only be called on lists.
It sorts the list in place and returns None.


**2. Return Value**
sorted():

Returns a new list containing the sorted elements.
The original iterable remains unchanged.
sort():

Returns None (it modifies the list in place).
The original list is changed to be sorted.

'''