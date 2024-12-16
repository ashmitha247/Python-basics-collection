#Write a program that inputs a text file. The program should print all of the unique words in the file in alphabetical order

def uniquewords_in_file(file):
    try:
        with open(file,'r') as file:
            splitted_file = file.read().split()
            splitted_words = sorted(set(splitted_file))
            for i in splitted_words:
                print(f"{i}")
    except:
        print("Error found")
file_name = input("Enter file name: ")
uniquewords_in_file(file_name)

        
