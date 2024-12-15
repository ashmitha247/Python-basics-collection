#Create a python program that asks the user for the name of a file. The program should display the contents of the file
#with each line preceded with a line number followed by a colon. The line numbering should start at 1.

# Ask the user for the name of the file
file_name = input("Please enter the name of the file (with extension): ")

try:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read all lines from the file
        lines_list = file.readlines()

        # Loop through the lines and print each with a line number
        for line_number, corresponding_line in enumerate(lines_list, start=1):
            print(f"{line_number}: {corresponding_line.strip()}")  # Use strip() to remove any extra newline characters

except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

'''

###readlines():

This is a method of the file object that reads all the lines from the file and returns them as a LIST. 
Each element of the list corresponds to a line in the file, including the newline character (\n) at the end of each line (if present).

###Using enumerate:

The enumerate function is a built-in Python function that adds a counter to an iterable (in this case, the list of lines).
The basic syntax of enumerate is:

enumerate(iterable, start=0)

iterable: The collection you want to iterate over (here, it's lines).
start: The starting value of the counter (default is 0, but we set it to 1).
By using enumerate(lines, start=1), we get pairs of (index, value) where the index starts at 1. '''

