sentence = input("Enter the sentence: ")
#break down the sentence into words by splitting the sentence
words = sentence.split()
#reverse the words 
reversed_words = words[-1::-1]
#join the reversed words in a list
reversed_sentence = ' '.join(reversed_words)
#print reversed sentence
print(reversed_sentence)

''' output:
Enter the sentence: hi my name is blah
blah is name my hi'''