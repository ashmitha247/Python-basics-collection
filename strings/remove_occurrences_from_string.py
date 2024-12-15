'''
Get a string from a given string where all occurrences of its first char have been changed to ‘$’, except the first char itself.

Eg:
Input: restart

Output: resta$t  '''

string = input("Enter a string: ")
a = string[0]

modified_string = a+string[1:].replace(a,'$')
print(f"Modified string : {modified_string}")