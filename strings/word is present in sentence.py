# Get a sentence input from the user
sentence = input("Enter a sentence: ")

# Get a word input from the user
word = input("Enter a word to check: ")

# Check if the word is present in the sentence
if word in sentence:
    print(f"The word '{word}' is present in the sentence.")
else:
    print(f"The word '{word}' is not present in the sentence.")