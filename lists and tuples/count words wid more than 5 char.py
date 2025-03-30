#given a list of words, count the no. of words with more than five char

input_string = input("Enter words").split()
count = 0

for item in input_string:
    if len(item)>5:
        count+=1
print(f"No. of words with more than five char are: {count}")