# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words using split() method
words = sentence.split()

# Initialize a counter for the number of words
word_count = 0

# Iterate through the list of words and count them
for word in words:
    word_count += 1  # Increment the counter for each word

# Print the result
print("The number of words in the sentence is:", word_count)

'''output:

Enter a sentence: hi my name is
The number of words in the sentence is: 4  '''