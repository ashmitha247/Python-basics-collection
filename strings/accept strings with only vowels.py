str = input("Enter string: ")
#change the string into lowercase
str = str.lower()
vowels = "aeiou " #its VERY imp to give space in the end cuz it wont accept example this: "oe i"
                  #when we give space, it also accepts "oe i" or "ae iu" etc
count = 0 #his variable will be used to count the number of characters in the input string that are either vowels or spaces.
for i in str:
    if i in vowels:
        count+=1
    else:
        break
if(count==len(str)):
    print("String accepted")
else:
    print(("Not accepted"))

    '''If a character is encountered that is not a vowel or space, the loop breaks immediately. 
    This means that the program only counts leading vowels and spaces. Once it hits a non-vowel character, it stops counting.'''
 