# Input string
'''input_string = input("Enter a string: ")

# Split the input string into words
splitted_string = input_string.split()

# Iterate through the words and print those with odd lengths
odd_length_words = [word for word in splitted_string if len(word) % 2 != 0]

# Print the odd length words
print("Odd length words:", odd_length_words)'''

'''line 8 explanation:
             "word" will be inlcuded in the list odd_length_words only if
             "for word in splitted_strings if len(word) %2 !=0" is true.

             Essentially, "for word in" is what allows us to access each individual word in the list.
             the condition len(word) % 2 != 0 checks if the length of the current word is odd.
            However, it does not specify where word comes from. The "for word in" part provides that context.'''


#code with for loop:
 
input_string = input("Enter a string: ")

splitted_string = input_string.split()
    
for item in splitted_string:
    if len(item) % 2 != 0:
        print(item)     
        
                     
'''output:
    Enter a string: heyy how are you!  
    how
    are'''