#Write a Python program to sort words in a file and put them in another file.
#The output file should have only lower-case words, so any upper-case words from source must be lowered.

def sortwords_in_file(input_file,output_file):
    try:
        with open(input_file,'r') as i_f:
            split_file = i_f.read().split()
            lower_split_words = [words.lower() for words in split_file]
            lower_split_words.sort()

        with open(output_file,'w') as o_f:
            for word in lower_split_words:
                o_f.write(f"{word}\n")
            print("Contents of input file sorted and moved to output file successfully")

        print("Content of output file:")
        with open(output_file,'r') as o_f:
            print(o_f.read())



    except FileNotFoundError:
        print("File Not Found!")


input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")
sortwords_in_file(input_file,output_file)


