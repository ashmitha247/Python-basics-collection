input_string = input("Enter a string: ")

splitted_string = input_string.split()
    
for item in splitted_string:
    if len(item) % 2 != 0:
        print(item)     
        
                     
'''output:
    Enter a string: heyy how are you!  
    how
    are'''