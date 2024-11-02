input_string = input("Enter a string: ")
result = ""

for char in input_string:
    if char not in result:
        result += char

print(result)  

'''output
Enter a string: prograaming
progamin'''

'''if char not in result:
        result += char

        if the character is not already in result, this line appends (+=) the character to the result string.
          This means that only the first occurrence of each character will be added to result.'''