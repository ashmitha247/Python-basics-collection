#Write a Python program to display the count of individual vowels in the input string-using dictionary.

string = input("Enter a string: ")
vowel_counts = {'a':0,'e':0,'i':0,'o':0,'u':0}

for char in string:
    if char in vowel_counts:
        vowel_counts[char]+=1
print(f"Vowel counts: {vowel_counts}")
