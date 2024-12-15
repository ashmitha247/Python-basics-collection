#Write a Python program to sort words in a file and put them in another file.
# The output file should have only lower-case words, so any upper-case words from source must be lowered.

def sortwords_in_file(input_file,output_file):
    try:
        i_f = open(input_file,'r')
        splitted_file = i_f.read().split()
        splitted_words = [words.lower() for words in splitted_file]
        splitted_words.sort()

        o_f = open(output_file,'w')
        for word in splitted_words:
            o_f.write(f"{word}\n")
        print("Contents of input file sorted and moved to output file successfull")
        print("Content of output file:")
        o_f = open(output_file,'r')
        print(o_f.read())
    except FileNotFoundError:
        print("File Not Found!")
    
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")
sortwords_in_file(input_file,output_file)


