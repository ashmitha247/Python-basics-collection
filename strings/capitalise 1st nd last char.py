#capitalise first and last char in every word of the sentence

given_string = input("Enter string: ")

'''The Python title() function is used to change the initial character IN EACH WORD 
to Uppercase and the subsequent characters to Lowercase and then returns a new string.
next, we have to convert last letter of EACH WORD to capital'''

given_string = given_string.title() #imp; on both sides its given_string and the wont work unless its that
#separating each word in S
splitted_string = given_string.split()
final_string=""

for i in splitted_string:
    final_string = final_string + i[:-1] + i[-1].upper() + ' '

print("Converted string: ",final_string)

'''output:
          Enter string: how you doin
Converted string:  HoW YoU DoiN '''



'''Explanation of line 13:

final_string is an empty string originally. 
1) we put i[:-1] in that, which is:
    every char from zero index will be printed, till the last, but one.
    till the elast ,but one, cuz -1 is the last one and in index slicing, the end parameter is excluded so -1 is excluded.
2) the last char i.e i[-1] is capitalised with upper().
3) space is given at last cuz in the for loop, we are accessing the "splitted string" items.
   we require space between each item we access so we use " ".  '''
