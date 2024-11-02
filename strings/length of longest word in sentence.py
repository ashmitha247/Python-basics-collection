# Prompt the user to enter a sentence
input_sentence = input("Enter a sentence: ")

# Split the sentence into words
words = input_sentence.split()

# Initialize a variable to keep track of the maximum length
max_length = 0

# Iterate through the list of words
for word in words:
    # Update max_length if the current word's length is greater
    if len(word) > max_length:
        max_length = len(word)

# Print the length of the longest word
print("Length of the longest word:", max_length)