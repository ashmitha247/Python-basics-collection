#given a list of words, count the no. of words with more than five char

words = list(map(str,input("Enter words: ").split()))
count = 0
for word in words:
    if len(word)>5:
        count+=1
print(f"number of words with more than five letters: {count}")